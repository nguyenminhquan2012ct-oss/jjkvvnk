import discord
from discord.ext import commands
import asyncio
import random
import os
import time

BUILT_IN_SONGS = {
    "stay alive": "stay_alive.mp3",
    "styx helix": "styx_helix.mp3",
    "akuma no ko": "akuma_no_ko.mp3",
    "specialz": "specialz.mp3",
    "sa": "stay_alive.mp3",
    "sh": "styx_helix.mp3",
}

class MusicSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queues = {}
        self.now_playing = {}
        self.loop_mode = {}
        self.volumes = {}
        self.idle_timers = {}
        self.ffmpeg_path = "ffmpeg" if os.name != "nt" else os.path.join(os.getcwd(), "ffmpeg", "ffmpeg.exe")

    def get_queue(self, guild_id):
        if guild_id not in self.queues:
            self.queues[guild_id] = []
        return self.queues[guild_id]

    async def play_next(self, guild_id):
        queue = self.get_queue(guild_id)
        if not queue:
            self.now_playing.pop(guild_id, None)
            return
        song = queue.pop(0)
        if self.loop_mode.get(guild_id):
            queue.append(song)
        self.now_playing[guild_id] = song
        await self._play_file(guild_id, song["path"])

    async def _play_file(self, guild_id, path):
        vc = self.bot.get_guild(guild_id).voice_client
        if not vc or not vc.is_connected():
            return
        vol = self.volumes.get(guild_id, 1.0)
        source = discord.FFmpegPCMAudio(path, executable=self.ffmpeg_path)
        source = discord.PCMVolumeTransformer(source, volume=vol)
        vc.play(source, after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(guild_id), self.bot.loop))
        self._reset_idle_timer(guild_id)

    def _reset_idle_timer(self, guild_id):
        if guild_id in self.idle_timers:
            self.idle_timers[guild_id].cancel()
        self.idle_timers[guild_id] = self.bot.loop.call_later(300, lambda: asyncio.run_coroutine_threadsafe(self._auto_disconnect(guild_id), self.bot.loop))

    async def _auto_disconnect(self, guild_id):
        vc = self.bot.get_guild(guild_id).voice_client
        if vc and not vc.is_playing():
            try:
                await vc.disconnect()
            except Exception:
                pass
            self.queues.pop(guild_id, None)
            self.now_playing.pop(guild_id, None)

    @commands.command(name="nhac")
    async def _music_menu(self, ctx):
        """Menu Nhạc"""
        await ctx.message.delete()
        menu = f"""```ansi
\033[1;34m🎵 PHÁP ĐÀN ÂM THANH: CHÚ THUẬT NHẠC 🎵\033[0m

\033[1;34m[🎶] ĐIỀU KHIỂN NHẠC\033[0m
\033[1;37m {self.bot.command_prefix}play [link/tên]\033[0m   \033[1;30m  Phát nhạc từ YouTube\033[0m
\033[1;37m {self.bot.command_prefix}play-sa\033[0m            \033[1;30m  Phát "Stay Alive"\033[0m
\033[1;37m {self.bot.command_prefix}play-sh\033[0m            \033[1;30m  Phát "Styx Helix"\033[0m
\033[1;37m {self.bot.command_prefix}play-amk\033[0m           \033[1;30m  Phát "Akuma no Ko"\033[0m
\033[1;37m {self.bot.command_prefix}play-sp\033[0m            \033[1;30m  Phát "Specialz"\033[0m

\033[1;32m[📋] HÀNG ĐỢI\033[0m
\033[1;37m {self.bot.command_prefix}queue\033[0m              \033[1;30m  Xem danh sách chờ\033[0m
\033[1;37m {self.bot.command_prefix}skip\033[0m               \033[1;30m  Bỏ qua bài hiện tại\033[0m
\033[1;37m {self.bot.command_prefix}stop\033[0m               \033[1;30m  Dừng nhạc + rời voice\033[0m
\033[1;37m {self.bot.command_prefix}now\033[0m                \033[1;30m  Bài đang phát\033[0m
\033[1;37m {self.bot.command_prefix}loop\033[0m               \033[1;30m  Bật/tắt lặp bài\033[0m

\033[1;33m[🔊] ĐIỀU CHỈNH\033[0m
\033[1;37m {self.bot.command_prefix}volume [1-100]\033[0m     \033[1;30m  Điều chỉnh âm lượng\033[0m
\033[1;37m {self.bot.command_prefix}pause\033[0m              \033[1;30m  Tạm dừng\033[0m
\033[1;37m {self.bot.command_prefix}resume\033[0m             \033[1;30m  Tiếp tục\033[0m

\033[1;35m🎵 Nhạc có sẵn: stay_alive, styx_helix, akuma_no_ko, specialz\033[0m
```"""
        await ctx.send(menu)

    @commands.command(name="play")
    async def _play(self, ctx, *, query: str = None):
        """Phát nhạc từ YouTube hoặc built-in"""
        if not query:
            return await ctx.send("❌ Gõ `.play [link hoặc tên bài]`!", delete_after=5)
        if not ctx.author.voice:
            return await ctx.send("❌ Bạn phải vào Voice Channel!", delete_after=5)

        query_lower = query.lower()
        if query_lower in BUILT_IN_SONGS:
            filename = BUILT_IN_SONGS[query_lower]
            path = os.path.join("music", filename)
            if not os.path.isfile(path):
                return await ctx.send(f"❌ File `{filename}` không có trong thư mục music/", delete_after=5)
            queue = self.get_queue(ctx.guild.id)
            queue.append({"title": query.title(), "path": path, "url": None})
            if not ctx.guild.voice_client or not ctx.guild.voice_client.is_playing():
                await self.play_next(ctx.guild.id)
            await ctx.send(f"🎵 **Đã thêm vào hàng chờ:** `{query.title()}`")
            return

        if not query.startswith("http"):
            query = f"ytsearch:{query}"

        try:
            import yt_dlp
        except ImportError:
            return await ctx.send("❌ Thiếu `yt-dlp`! Gõ: `pip install yt-dlp`", delete_after=5)

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "music_cache/%(id)s.%(ext)s",
            "quiet": True,
            "no_warnings": True,
        }
        os.makedirs("music_cache", exist_ok=True)
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(query, download=True)
                if "entries" in info:
                    info = info["entries"][0]
                filename = ydl.prepare_filename(info)
        except Exception as e:
            return await ctx.send(f"❌ Lỗi tải nhạc: {e}", delete_after=5)

        queue = self.get_queue(ctx.guild.id)
        queue.append({"title": info.get("title", "Unknown"), "path": filename, "url": info.get("webpage_url")})
        if not ctx.guild.voice_client or not ctx.guild.voice_client.is_playing():
            await self.play_next(ctx.guild.id)
        await ctx.send(f"🎵 **Đã thêm:** `{info.get('title', 'Unknown')}`")

    async def _connect_voice(self, ctx):
        if ctx.guild.voice_client and ctx.guild.voice_client.is_connected():
            return ctx.guild.voice_client
        return await ctx.author.voice.channel.connect(reconnect=True)

    @commands.command(name="play-sa")
    async def _play_sa(self, ctx):
        """Phát Stay Alive"""
        await ctx.invoke(self._play, query="stay alive")

    @commands.command(name="play-sh")
    async def _play_sh(self, ctx):
        """Phát Styx Helix"""
        await ctx.invoke(self._play, query="styx helix")

    @commands.command(name="play-amk")
    async def _play_amk(self, ctx):
        """Phát Akuma no Ko"""
        await ctx.invoke(self._play, query="akuma no ko")

    @commands.command(name="play-sp")
    async def _play_sp(self, ctx):
        """Phát Specialz"""
        await ctx.invoke(self._play, query="specialz")

    @commands.command(name="queue")
    async def _queue(self, ctx):
        """Xem hàng chờ"""
        await ctx.message.delete()
        queue = self.get_queue(ctx.guild.id)
        now = self.now_playing.get(ctx.guild.id)
        if not queue and not now:
            return await ctx.send("📋 Hàng chờ trống!", delete_after=5)
        lines = ["📋 **Hàng chờ:**\n"]
        if now:
            lines.append(f"▶️ **Đang phát:** {now['title']}")
        for i, song in enumerate(queue[:10], 1):
            lines.append(f"{i}. {song['title']}")
        if len(queue) > 10:
            lines.append(f"... và {len(queue) - 10} bài nữa")
        await ctx.send("\n".join(lines))

    @commands.command(name="skip")
    async def _skip(self, ctx):
        """Bỏ qua bài hiện tại"""
        await ctx.message.delete()
        vc = ctx.guild.voice_client
        if vc and vc.is_playing():
            vc.stop()

    @commands.command(name="stop")
    async def _stop(self, ctx):
        """Dừng nhạc + rời voice"""
        await ctx.message.delete()
        self.queues.pop(ctx.guild.id, None)
        self.now_playing.pop(ctx.guild.id, None)
        vc = ctx.guild.voice_client
        if vc:
            if vc.is_playing():
                vc.stop()
            await vc.disconnect()
        await ctx.send("⏹️ **Đã dừng nhạc và rời voice!**", delete_after=3)

    @commands.command(name="now")
    async def _now(self, ctx):
        """Bài đang phát"""
        await ctx.message.delete()
        now = self.now_playing.get(ctx.guild.id)
        if now:
            await ctx.send(f"🎵 **Đang phát:** {now['title']}")
        else:
            await ctx.send("🔇 Không có bài nào đang phát!", delete_after=3)

    @commands.command(name="loop")
    async def _loop(self, ctx):
        """Bật/tắt lặp bài"""
        await ctx.message.delete()
        current = self.loop_mode.get(ctx.guild.id, False)
        self.loop_mode[ctx.guild.id] = not current
        state = "🟢 **BẬT**" if not current else "🔴 **TẮT**"
        await ctx.send(f"🔁 Lặp bài: {state}")

    @commands.command(name="volume")
    async def _volume(self, ctx, vol: int = None):
        """Điều chỉnh âm lượng"""
        await ctx.message.delete()
        if vol is None:
            current = int(self.volumes.get(ctx.guild.id, 1.0) * 100)
            return await ctx.send(f"🔊 Âm lượng hiện tại: **{current}%**", delete_after=5)
        vol = max(1, min(100, vol))
        self.volumes[ctx.guild.id] = vol / 100
        vc = ctx.guild.voice_client
        if vc and vc.source and hasattr(vc.source, "volume"):
            vc.source.volume = vol / 100
        await ctx.send(f"🔊 **Âm lượng:** {vol}%")

    @commands.command(name="pause")
    async def _pause(self, ctx):
        """Tạm dừng"""
        await ctx.message.delete()
        vc = ctx.guild.voice_client
        if vc and vc.is_playing():
            vc.pause()
            await ctx.send("⏸️ **Tạm dừng!**", delete_after=3)

    @commands.command(name="resume")
    async def _resume(self, ctx):
        """Tiếp tục"""
        await ctx.message.delete()
        vc = ctx.guild.voice_client
        if vc and vc.is_paused():
            vc.resume()
            await ctx.send("▶️ **Tiếp tục!**", delete_after=3)

async def setup(bot):
    await bot.add_cog(MusicSystem(bot))
