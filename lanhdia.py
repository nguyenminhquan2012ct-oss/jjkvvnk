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
        """Menu chinh"""
        p = self.bot.command_prefix
        lines = [
            f"\033[1;37mChu thuat su: \033[1;32m{self.bot.user.name}\033[0m",
            "",
            f"\033[1;33m🔵 {p}thuong       \033[1;30mNhay ngon.txt\033[0m",
            f"\033[1;31m🔴 {p}he            \033[1;30mDam tag nhay.txt\033[0m",
            f"\033[1;31m⚔️  {p}ngutoa        \033[1;30mChem nhat Server\033[0m",
            f"\033[1;34m✨ {p}info          \033[1;30mSoi thong so\033[0m",
            f"\033[1;37m🧹 {p}tayue         \033[1;30mXoa tin nhan\033[0m",
            f"\033[1;32m🔄 {p}hoiphuc       \033[1;30mRestart bot\033[0m",
            f"\033[1;37m⚪ {p}ngung         \033[1;30mStop\033[0m",
            "",
            f"\033[1;30mType {p}menu de xem tat ca\033[0m",
        ]
        w = 46
        border = "═" * w
        menu = f"```ansi\n"
        menu += f"\033[1;35m╔{border}╗\033[0m\n"
        menu += f"\033[1;35m║\033[0m \033[1;37m{'DOMAIN EXPANSION':^{w-2}}\033[0m \033[1;35m║\033[0m\n"
        menu += f"\033[1;35m╠{border}╣\033[0m\n"
        for line in lines:
            menu += f"\033[1;35m║\033[0m {line:<{w-2}} \033[1;35m║\033[0m\n"
        menu += f"\033[1;35m╚{border}╝\033[0m\n"
        menu += "```"
        await ctx.send(menu)
        await ctx.send("https://cdn.discordapp.com/attachments/1447965096214007872/1449264465970331789/C4A0F6F1-28DA-4945-AE12-4A258A305084.gif")

    # --- Thuật thức 2: .info (Bảng thông số kỹ thuật style diff) ---
    @commands.command(name="info")
    async def _bot_info(self, ctx):
        try:
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