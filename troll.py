import os
import discord
from discord.ext import commands
import random
import asyncio

class TrollSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="troll")
    async def _troll_menu(self, ctx):
        """Menu troll"""
        p = self.bot.command_prefix
        lines = [
            f"\033[1;34m🎮 MINI GAMES\033[0m",
            f"  {p}batdiet             \033[1;30mNhan pham\033[0m",
            f"  {p}xucxac             \033[1;30mXuc xac\033[0m",
            "",
            f"\033[1;32m🎶 AM THANH\033[0m",
            f"  {p}amhon [url]        \033[1;30mPhat nhac\033[0m",
            f"  {p}truhon            \033[1;30mRoi voice\033[0m",
            "",
            f"\033[1;31m🔥 TROLL\033[0m",
            f"  {p}fake [@user] [t]  \033[1;30mGia mao tin nhan\033[0m",
            f"  {p}donguyen         \033[1;30mXem suc manh\033[0m",
            f"  {p}vonghon          \033[1;30mNhai tin nhan\033[0m",
            f"  {p}nguyenrua [@u]   \033[1;30mAm que\033[0m",
            f"  {p}batkhuat         \033[1;30mTu phan hoi khi bi tag\033[0m",
        ]
        w = 46
        border = "═" * w
        menu = f"```ansi\n"
        menu += f"\033[1;36m╔{border}╗\033[0m\n"
        menu += f"\033[1;36m║\033[0m \033[1;37m{'PHAP DAN GIAI TRI':^{w-2}}\033[0m \033[1;36m║\033[0m\n"
        menu += f"\033[1;36m╠{border}╣\033[0m\n"
        for line in lines:
            menu += f"\033[1;36m║\033[0m {line:<{w-2}} \033[1;36m║\033[0m\n"
        menu += f"\033[1;36m╚{border}╝\033[0m\n"
        menu += "```"
        await ctx.send(menu)

    # --- [🎮] GAME ---
    @commands.command(name="batdiet")
    async def _batdiet(self, ctx):
        outcome = random.choice(["Sống sót", "Bị thanh tẩy", "Thăng cấp Đặc cấp", "Hết chú lực"])
        await ctx.send(f"🔮 **Nguyền hồn phán:** `{outcome}`")

    @commands.command(name="xucxac")
    async def _xucxac(self, ctx):
        await ctx.send(f"🎲 **Xúc xắc:** `{random.randint(1,6)}` điểm")

    @commands.command(name="amhon")
    async def _amhon(self, ctx, channel_id: int, audio_name: str, deafen: str = "N", camera: str = "N"):
        """[Âm Hồn] Phát nhạc từ file cục bộ (Yêu cầu FFmpeg)"""
        
        # Kiểm tra định dạng file
        valid_exts = ['.mp3', '.wav', '.ogg']
        if not any(audio_name.lower().endswith(ext) for ext in valid_exts):
            return await ctx.send(f"❌ File phải thuộc định dạng: {', '.join(valid_exts)}", delete_after=3)

        # Thiết lập đường dẫn linh hồn (Path)
        music_folder = os.path.join(os.getcwd(), 'music')
        audio_path = os.path.join(music_folder, audio_name)
        ffmpeg_path = "ffmpeg" if os.name != "nt" else os.path.join(os.getcwd(), 'ffmpeg', 'ffmpeg.exe')

        if not os.path.isfile(audio_path):
            return await ctx.send(f"❌ Không tìm thấy chú vật tại: `{audio_name}` trong thư mục /music", delete_after=5)

        # Triệu hồi kết giới Voice
        channel = self.bot.get_channel(channel_id)
        if not channel or not isinstance(channel, discord.VoiceChannel):
            return await ctx.send("❌ Tọa độ Voice ID không hợp lệ!", delete_after=3)

        voice_client = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        try:
            # Kết nối hoặc di chuyển
            if voice_client and voice_client.is_connected():
                if voice_client.channel != channel:
                    await voice_client.move_to(channel)
                if voice_client.is_playing():
                    voice_client.stop()
            else:
                voice_client = await channel.connect(timeout=10.0)

            # Trạng thái ẩn thân (Deafen/Camera)
            await ctx.guild.change_voice_state(
                channel=channel,
                self_deaf=deafen.lower() == 'y',
                self_video=camera.lower() == 'y'
            )

            # Khai triển thuật thức âm thanh
            source = discord.FFmpegPCMAudio(audio_path, executable=ffmpeg_path)
            voice_client.play(source)

            await ctx.send(f"🌀 **Âm Hồn Khai Triển!**\n🎶 Đang phát: `{audio_name}`\n📍 Tại: `{channel.name}`\n🎧 Điếc: `{deafen.upper()}` | 📷 Cam: `{camera.upper()}`")

            # Tự động rời khi hát xong (hoặc sau 10p)
            timeout = 600
            while voice_client.is_playing() and timeout > 0:
                await asyncio.sleep(1)
                timeout -= 1
            
            if not voice_client.is_playing():
                await voice_client.disconnect()

        except Exception as e:
            await ctx.send(f"❌ Thuật thức thất bại: `{str(e)}`", delete_after=5)
            if voice_client: await voice_client.disconnect()

    @commands.command(name="truhon")
    async def _truhon(self, ctx):
        if ctx.guild.voice_client:
            await ctx.guild.voice_client.disconnect()
            await ctx.send("🌪️ **Trục Hồn** thành công!", delete_after=2)

    # --- [🔥] TROLL ---
    @commands.command(name="fake")
    async def _fake(self, ctx, member: discord.Member, *, text):
        webhook = await ctx.channel.create_webhook(name=member.display_name)
        avatar = member.avatar.url if member.avatar else None
        await webhook.send(text, avatar_url=avatar)
        await webhook.delete()

    @commands.command(name="donguyen")
    async def _donguyen(self, ctx):
        power = random.randint(1, 1000000)
        rank = "Đặc Cấp" if power > 800000 else "Cấp 1" if power > 400000 else "Cấp 4"
        await ctx.send(f"📊 **Linh Lực:** `{power:,}` | **Xếp hạng:** `{rank}`")

    @commands.command(name="vonghon")
    async def _vonghon(self, ctx):
        await ctx.send("🗣️ **Vọng Hồn** đã kích hoạt!", delete_after=2)
        msg = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
        await ctx.send(f"📢 `{msg.content}`")

    @commands.command(name="nguyenrua")
    async def _nguyenrua(self, ctx, member: discord.Member):
        for i in range(3):
            await ctx.send(f"{member.mention} Bạn đã bị ám bởi Nguyền Hồn!")

    @commands.command(name="batkhuat")
    async def _batkhuat(self, ctx):
        await ctx.send("🛡️ **Bất Khuất** đã kích hoạt!")

async def setup(bot):
    await bot.add_cog(TrollSystem(bot))