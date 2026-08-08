import discord
from discord.ext import commands
import psutil
import time
import platform
from datetime import datetime

class LanhDiaSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()
        self.version = "6.1.0"

    # --- Thuật thức 1: .lanhdia (Menu chính theo style JJK ông thích) ---
    @commands.command(name="lanhdia")
    async def _lanhdia_menu(self, ctx):
        try:
            await ctx.message.delete()
            
            style_menu = f"""
```ansi
\033[1;35m💫 DOMAIN EXPANSION: INFINITE VOID 💫\033[0m

\033[1;34m[+] CHÚ THUẬT SƯ:\033[0m \033[1;32m{self.bot.user.name}\033[0m

\033[1;31m[!] DANH SÁCH THUẬT THỨC\033[0m
\033[1;37m 🔵 .thuong\033[0m   \033[1;30m|\033[0m [Thương] Nhây ngôn từ (ngon.txt)
\033[1;37m 🔴 .he\033[0m       \033[1;30m|\033[0m [Hách] Đấm tag liên hồi (nhay.txt)
\033[1;37m ⚔️ .ngutoa\033[0m   \033[1;30m|\033[0m [Ngự Tọa] Chém nát Server (Raid)
\033[1;37m ✨ .info\033[0m     \033[1;30m|\033[0m [Lục Nhãn] Soi thông số kết giới
\033[1;37m 🧹 .tayue\033[0m    \033[1;30m|\033[0m [Tẩy Uế] Thanh tẩy tin nhắn (Clear)
\033[1;37m 🔄 .hoiphuc\033[0m  \033[1;30m|\033[0m [Phản Phục] Tái thiết kết giới (Restart)
\033[1;37m ⚪ .ngung\033[0m    \033[1;30m|\033[0m [Ngưng] Giải ấn chú thuật (Stop)

\033[1;35m"Trong lãnh địa của ta, mọi đòn tấn công đều là tất trúng."\033[0m
```"""
            gif_url = "https://cdn.discordapp.com/attachments/1447965096214007872/1449264465970331789/C4A0F6F1-28DA-4945-AE12-4A258A305084.gif"
            await ctx.send(style_menu)
            await ctx.send(gif_url)
        except Exception as e:
            print(f"Lỗi .lanhdia: {e}")

    # --- Thuật thức 2: .info (Bảng thông số kỹ thuật style diff) ---
    @commands.command(name="info")
    async def _bot_info(self, ctx):
        try:
            await ctx.message.delete()
            
            # Tính toán Uptime chính xác
            uptime_delta = datetime.fromtimestamp(time.time()) - datetime.fromtimestamp(self.start_time)
            days = uptime_delta.days
            hours, remainder = divmod(uptime_delta.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            uptime_str = f"{days}d {hours}h {minutes}m {seconds}s"
            
            ping = round(self.bot.latency * 1000)
            
            diff_style = f"""```diff
+ {self.version}
- Bot Name: {self.bot.user.name}
- Bot ID: {self.bot.user.id}
- Total Servers: {len(self.bot.guilds)}
- Bot Latency: {ping}ms
- Uptime: {uptime_str}
- Host Python Version: {platform.python_version()}
- Discord.py Version: {discord.__version__}
```"""
            await ctx.send(diff_style)
        except Exception as e:
            print(f"Lỗi .info: {e}")

async def setup(bot):
    await bot.add_cog(LanhDiaSystem(bot))