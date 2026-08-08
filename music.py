import discord
from discord.ext import commands
import asyncio
import random
import os
import sys

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
        if os.name == "nt":
            self.ffmpeg_path = os.path.join(os.getcwd(), "ffmpeg", "ffmpeg.exe")
            if not os.path.isfile(self.ffmpeg_path):
                self.ffmpeg_path = "ffmpeg"
        else:
            self.ffmpeg_path = "ffmpeg"

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
        if not os.path.isfile(path):
            self.now_playing.pop(guild_id, None)
            return
        vol = self.volumes.get(guild_id, 1.0)
        source = discord.FFmpegPCMAudio(path, executable=self.ffmpeg_path)
        source = discord.PCMVolumeTransformer(source, volume=vol)
        vc.play(source, after=lambda e: asyncio.run_coroutine_threadsafe(
            self.play_next(guild_id), self.bot.loop
        ))
        self._reset_idle_timer(guild_id)

    def _reset_idle_timer(self, guild_id):
        if guild_id in self.idle_timers:
            self.idle_timers[guild_id].cancel()
        self.idle_timers[guild_id] = self.bot.loop.call_later(
            300,
            lambda: asyncio.run_coroutine_threadsafe(
                self._auto_disconnect(guild_id), self.bot.loop
            ),
        )

    async def _auto_disconnect(self, guild_id):
        vc = self.bot.get_guild(guild_id).voice_client
        if vc and not vc.is_playing():
            try:
                await vc.disconnect()
            except Exception:
                pass
            self.queues.pop(guild_id, None)
            self.now_playing.pop(guild_id, None)

    async def _ensure_voice(self, ctx):
        if ctx.guild.voice_client and ctx.guild.voice_client.is_connected():
            return ctx.guild.voice_client
        if ctx.author.voice and ctx.author.voice.channel:
            return await ctx.author.voice.channel.connect(reconnect=True)
        return None

    @commands.command(name="nhac")
    async def _music_menu(self, ctx):
        """Menu Nhac"""
        await ctx.message.delete()
        p = self.bot.command_prefix
        menu = f"""```ansi
\033[1;34m PHAP DAN AM THANH: CHU THUAT NHAC \033[0m

\033[1;34m[ Dieu khien nhac ]\033[0m
\033[1;37m {p}play [link/ten]\033[0m           \033[1;30m  Phat nhac tu YouTube\033[0m
\033[1;37m {p}play-sa\033[0m                 \033[1;30m  Phat "Stay Alive"\033[0m
\033[1;37m {p}play-sh\033[0m                 \033[1;30m  Phat "Styx Helix"\033[0m
\033[1;37m {p}play-amk\033[0m                \033[1;30m  Phat "Akuma no Ko"\033[0m
\033[1;37m {p}play-sp\033[0m                 \033[1;30m  Phat "Specialz"\033[0m

\033[1;32m[ Hang choi ]\033[0m
\033[1;37m {p}queue\033[0m                   \033[1;30m  Xem danh sach cho\033[0m
\033[1;37m {p}skip\033[0m                    \033[1;30m  Bo qua bai hien tai\033[0m
\033[1;37m {p}stop\033[0m                    \033[1;30m  Dung nhac + roi voice\033[0m
\033[1;37m {p}now\033[0m                     \033[1;30m  Bai dang phat\033[0m
\033[1;37m {p}loop\033[0m                    \033[1;30m  Bat/tat lap bai\033[0m

\033[1;33m[ Dieu chinh ]\033[0m
\033[1;37m {p}volume [1-100]\033[0m          \033[1;30m  Dieu chinh am luong\033[0m
\033[1;37m {p}pause\033[0m                   \033[1;30m  Tam dung\033[0m
\033[1;37m {p}resume\033[0m                  \033[1;30m  Tiep tuc\033[0m
```"""
        await ctx.send(menu)

    @commands.command(name="play")
    async def _play(self, ctx, *, query: str = None):
        """Phat nhac tu YouTube hoac built-in"""
        p = self.bot.command_prefix
        if not query:
            return await ctx.send(f"❌ Go `{p}play [link hoac ten bai]`!", delete_after=5)

        vc = await self._ensure_voice(ctx)
        if not vc:
            return await ctx.send("❌ Ban phai vao Voice Channel truoc!", delete_after=5)

        query_lower = query.lower()

        if query_lower in BUILT_IN_SONGS:
            filename = BUILT_IN_SONGS[query_lower]
            path = os.path.join("music", filename)
            if os.path.isfile(path):
                queue = self.get_queue(ctx.guild.id)
                queue.append({"title": query.title(), "path": path, "url": None})
                if not ctx.guild.voice_client.is_playing():
                    await self.play_next(ctx.guild.id)
                return await ctx.send(f"🎵 **Da them vao hang cho:** `{query.title()}`")
            else:
                query = query.title()

        if not query.startswith("http"):
            query = f"ytsearch:{query}"

        try:
            import yt_dlp
        except ImportError:
            return await ctx.send("❌ Thieu `yt-dlp`! Go: `pip install yt-dlp`", delete_after=5)

        os.makedirs("music_cache", exist_ok=True)
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "music_cache/%(id)s.%(ext)s",
            "quiet": True,
            "no_warnings": True,
            "default_search": "ytsearch",
            "noplaylist": True,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(query, download=True)
                if not info:
                    return await ctx.send("❌ Khong tim thay bai hat!", delete_after=5)
                if "entries" in info:
                    info = info["entries"][0]
                filename = ydl.prepare_filename(info)
        except Exception as e:
            return await ctx.send(f"❌ Loi tai nhac: {e}", delete_after=5)

        if not os.path.isfile(filename):
            return await ctx.send("❌ File nhac khong ton tai sau khi tai!", delete_after=5)

        queue = self.get_queue(ctx.guild.id)
        queue.append({
            "title": info.get("title", "Unknown"),
            "path": filename,
            "url": info.get("webpage_url"),
        })
        if not ctx.guild.voice_client.is_playing():
            await self.play_next(ctx.guild.id)
        await ctx.send(f"🎵 **Da them:** `{info.get('title', 'Unknown')}`")

    @commands.command(name="play-sa")
    async def _play_sa(self, ctx):
        await ctx.invoke(self._play, query="stay alive")

    @commands.command(name="play-sh")
    async def _play_sh(self, ctx):
        await ctx.invoke(self._play, query="styx helix")

    @commands.command(name="play-amk")
    async def _play_amk(self, ctx):
        await ctx.invoke(self._play, query="akuma no ko")

    @commands.command(name="play-sp")
    async def _play_sp(self, ctx):
        await ctx.invoke(self._play, query="specialz")

    @commands.command(name="queue")
    async def _queue(self, ctx):
        await ctx.message.delete()
        queue = self.get_queue(ctx.guild.id)
        now = self.now_playing.get(ctx.guild.id)
        if not queue and not now:
            return await ctx.send("📋 Hang cho trong!", delete_after=5)
        lines = ["📋 **Hang cho:**\n"]
        if now:
            lines.append(f"▶️ **Dang phat:** {now['title']}")
        for i, song in enumerate(queue[:10], 1):
            lines.append(f"{i}. {song['title']}")
        if len(queue) > 10:
            lines.append(f"... va {len(queue) - 10} bai nua")
        await ctx.send("\n".join(lines))

    @commands.command(name="skip")
    async def _skip(self, ctx):
        await ctx.message.delete()
        vc = ctx.guild.voice_client
        if vc and vc.is_playing():
            vc.stop()

    @commands.command(name="stop")
    async def _stop(self, ctx):
        await ctx.message.delete()
        self.queues.pop(ctx.guild.id, None)
        self.now_playing.pop(ctx.guild.id, None)
        vc = ctx.guild.voice_client
        if vc:
            if vc.is_playing():
                vc.stop()
            await vc.disconnect()
        await ctx.send("⏹️ **Da dung nhac va roi voice!**", delete_after=3)

    @commands.command(name="now")
    async def _now(self, ctx):
        await ctx.message.delete()
        now = self.now_playing.get(ctx.guild.id)
        if now:
            await ctx.send(f"🎵 **Dang phat:** {now['title']}")
        else:
            await ctx.send("🔇 Khong co bai nao dang phat!", delete_after=3)

    @commands.command(name="loop")
    async def _loop(self, ctx):
        await ctx.message.delete()
        current = self.loop_mode.get(ctx.guild.id, False)
        self.loop_mode[ctx.guild.id] = not current
        state = "🟢 **BAT**" if not current else "🔴 **TAT**"
        await ctx.send(f"🔁 Lap bai: {state}")

    @commands.command(name="volume")
    async def _volume(self, ctx, vol: int = None):
        await ctx.message.delete()
        if vol is None:
            current = int(self.volumes.get(ctx.guild.id, 1.0) * 100)
            return await ctx.send(f"🔊 Am luong hien tai: **{current}%**", delete_after=5)
        vol = max(1, min(100, vol))
        self.volumes[ctx.guild.id] = vol / 100
        vc = ctx.guild.voice_client
        if vc and vc.source and hasattr(vc.source, "volume"):
            vc.source.volume = vol / 100
        await ctx.send(f"🔊 **Am luong:** {vol}%")

    @commands.command(name="pause")
    async def _pause(self, ctx):
        await ctx.message.delete()
        vc = ctx.guild.voice_client
        if vc and vc.is_playing():
            vc.pause()
            await ctx.send("⏸️ **Tam dung!**", delete_after=3)

    @commands.command(name="resume")
    async def _resume(self, ctx):
        await ctx.message.delete()
        vc = ctx.guild.voice_client
        if vc and vc.is_paused():
            vc.resume()
            await ctx.send("▶️ **Tiep tuc!**", delete_after=3)


async def setup(bot):
    await bot.add_cog(MusicSystem(bot))
