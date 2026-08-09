import discord
from discord.ext import commands
import asyncio
import time

WAR_COLOR = 0xFF0000
MUSIC_COLOR = 0x00AAFF
FUN_COLOR = 0x00FF00
UTILITY_COLOR = 0xFFFF00
SPECIAL_COLOR = 0x800080

class UIHelper:
    @staticmethod
    def progress_bar(current, total, length=20):
        filled = int(length * current / total) if total > 0 else 0
        bar = "█" * filled + "░" * (length - filled)
        percent = int(100 * current / total) if total > 0 else 0
        return f"`[{bar}] {percent}%`"

class UISystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="menu")
    async def _main_menu(self, ctx):
        """Menu chính đẹp"""
        menu = f"""```ansi
\033[1;35m💫 DOMAIN EXPANSION: INFINITE VOID 💫\033[0m

\033[1;37m**Lãnh địa đã sẵn sàng!** Chọn thuật thức bên dưới:\033[0m

\033[1;31m⚔️ WAR\033[0m     \033[1;30m  {self.bot.command_prefix}raid\033[0m    \033[1;30m- Menu chiến tranh\033[0m
\033[1;34m🎵 MUSIC\033[0m   \033[1;30m  {self.bot.command_prefix}nhac\033[0m   \033[1;30m- Menu nhạc\033[0m
\033[1;32m🎮 FUN\033[0m     \033[1;30m  {self.bot.command_prefix}traloi\033[0m \033[1;30m- Menu giải trí\033[0m
\033[1;33m🛠️ UTILITY\033[0m \033[1;30m  {self.bot.command_prefix}chucu\033[0m  \033[1;30m- Menu tiện ích\033[0m
\033[1;35m🛡️ ADMIN\033[0m   \033[1;30m  {self.bot.command_prefix}quanly\033[0m \033[1;30m- Menu quản lý\033[0m
\033[1;36m🃏 TROLL\033[0m   \033[1;30m  {self.bot.command_prefix}troll\033[0m  \033[1;30m- Menu troll\033[0m

\033[1;30mJJK-VVNK Bot | {len(self.bot.guilds)} servers\033[0m
```"""
        await ctx.send(menu)

    @commands.command(name="warmenu")
    async def _war_menu_embed(self, ctx):
        """Menu war bằng ANSI"""
        menu = f"""```ansi
\033[1;31m⚔️ WAR MENU ⚔️\033[0m

\033[1;37m {self.bot.command_prefix}vohahan [delay] [text]\033[0m   \033[1;30m  Spam tùy chỉnh\033[0m
\033[1;37m {self.bot.command_prefix}thuong [delay]\033[0m            \033[1;30m  Spam ngon.txt\033[0m
\033[1;37m {self.bot.command_prefix}lienke [delay]\033[0m            \033[1;30m  Spam nhay.txt\033[0m
\033[1;37m {self.bot.command_prefix}hacmon [url] [delay] [text]\033[0m \033[1;30m  Webhook spam\033[0m
\033[1;37m {self.bot.command_prefix}khaitram\033[0m                 \033[1;30m  Xóa toàn bộ kênh\033[0m
\033[1;37m {self.bot.command_prefix}huydiet\033[0m                 \033[1;30m  Nuke server\033[0m
\033[1;37m {self.bot.command_prefix}ngung\033[0m                   \033[1;30m  Dừng tất cả\033[0m
```"""
        await ctx.send(menu)

    @commands.command(name="musicmenu")
    async def _music_menu_embed(self, ctx):
        """Menu nhạc bằng ANSI"""
        menu = f"""```ansi
\033[1;34m🎵 MUSIC MENU 🎵\033[0m

\033[1;37m {self.bot.command_prefix}play [link/tên]\033[0m            \033[1;30m  Phát nhạc YouTube\033[0m
\033[1;37m {self.bot.command_prefix}play-sa / {self.bot.command_prefix}play-sh / {self.bot.command_prefix}play-amk / {self.bot.command_prefix}play-sp\033[0m \033[1;30m  Nhạc có sẵn\033[0m
\033[1;37m {self.bot.command_prefix}queue\033[0m                    \033[1;30m  Xem hàng chờ\033[0m
\033[1;37m {self.bot.command_prefix}skip / {self.bot.command_prefix}stop / {self.bot.command_prefix}now\033[0m       \033[1;30m  Điều khiển\033[0m
\033[1;37m {self.bot.command_prefix}volume [1-100]\033[0m            \033[1;30m  Âm lượng\033[0m
\033[1;37m {self.bot.command_prefix}loop / {self.bot.command_prefix}pause / {self.bot.command_prefix}resume\033[0m   \033[1;30m  Loop & Pause\033[0m
```"""
        await ctx.send(menu)

    @commands.command(name="funmenu")
    async def _fun_menu_embed(self, ctx):
        """Menu giải trí bằng ANSI"""
        menu = f"""```ansi
\033[1;32m🎮 FUN MENU 🎮\033[0m

\033[1;37m {self.bot.command_prefix}8ball / {self.bot.command_prefix}rps / {self.bot.command_prefix}trivia / {self.bot.command_prefix}coinflip / {self.bot.command_prefix}number\033[0m \033[1;30m  Mini games\033[0m
\033[1;37m {self.bot.command_prefix}daily / {self.bot.command_prefix}bal / {self.bot.command_prefix}pay / {self.bot.command_prefix}shop / {self.bot.command_prefix}inventory\033[0m   \033[1;30m  Economy\033[0m
\033[1;37m {self.bot.command_prefix}fact / {self.bot.command_prefix}quote / {self.bot.command_prefix}meme / {self.bot.command_prefix}insult / {self.bot.command_prefix}compliment\033[0m \033[1;30m  Fun\033[0m
\033[1;37m {self.bot.command_prefix}avatar / {self.bot.command_prefix}banner\033[0m                \033[1;30m  Avatar & Banner\033[0m
```"""
        await ctx.send(menu)

    @commands.command(name="progress")
    async def _test_progress(self, ctx, current: int = 50, total: int = 100):
        """Test progress bar"""
        bar = UIHelper.progress_bar(current, total)
        await ctx.send(f"📊 **Progress:** {bar}")

async def setup(bot):
    await bot.add_cog(UISystem(bot))
