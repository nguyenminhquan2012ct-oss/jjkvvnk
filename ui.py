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
        await ctx.message.delete()
        menu = f"""```ansi
\033[1;35m💫 DOMAIN EXPANSION: INFINITE VOID 💫\033[0m

\033[1;37m**Lãnh địa đã sẵn sàng!** Chọn thuật thức bên dưới:\033[0m

\033[1;31m⚔️ WAR\033[0m     \033[1;30m|\033[0m \033[1;37m.raid\033[0m    \033[1;30m- Menu chiến tranh\033[0m
\033[1;34m🎵 MUSIC\033[0m   \033[1;30m|\033[0m \033[1;37m.nhac\033[0m   \033[1;30m- Menu nhạc\033[0m
\033[1;32m🎮 FUN\033[0m     \033[1;30m|\033[0m \033[1;37m.traloi\033[0m \033[1;30m- Menu giải trí\033[0m
\033[1;33m🛠️ UTILITY\033[0m \033[1;30m|\033[0m \033[1;37m.chucu\033[0m  \033[1;30m- Menu tiện ích\033[0m
\033[1;35m🛡️ ADMIN\033[0m   \033[1;30m|\033[0m \033[1;37m.quanly\033[0m \033[1;30m- Menu quản lý\033[0m
\033[1;36m🃏 TROLL\033[0m   \033[1;30m|\033[0m \033[1;37m.troll\033[0m  \033[1;30m- Menu troll\033[0m

\033[1;30mJJK-VVNK Bot | {len(self.bot.guilds)} servers\033[0m
```"""
        await ctx.send(menu)

    @commands.command(name="warmenu")
    async def _war_menu_embed(self, ctx):
        """Menu war bằng ANSI"""
        await ctx.message.delete()
        menu = f"""```ansi
\033[1;31m⚔️ WAR MENU ⚔️\033[0m

\033[1;37m .vohahan [delay] [text]\033[0m \033[1;30m|\033[0m Spam tùy chỉnh
\033[1;37m .thuong [delay]\033[0m          \033[1;30m|\033[0m Spam ngon.txt
\033[1;37m .lienke [delay]\033[0m          \033[1;30m|\033[0m Spam nhay.txt
\033[1;37m .hacmon [url] [delay] [text]\033[0m \033[1;30m|\033[0m Webhook spam
\033[1;37m .khaitram\033[0m               \033[1;30m|\033[0m Xóa toàn bộ kênh
\033[1;37m .huydiet\033[0m               \033[1;30m|\033[0m Nuke server
\033[1;37m .ngung\033[0m                 \033[1;30m|\033[0m Dừng tất cả
```"""
        await ctx.send(menu)

    @commands.command(name="musicmenu")
    async def _music_menu_embed(self, ctx):
        """Menu nhạc bằng ANSI"""
        await ctx.message.delete()
        menu = f"""```ansi
\033[1;34m🎵 MUSIC MENU 🎵\033[0m

\033[1;37m .play [link/tên]\033[0m          \033[1;30m|\033[0m Phát nhạc YouTube
\033[1;37m .play-sa / .play-sh / .play-amk / .play-sp\033[0m \033[1;30m|\033[0m Nhạc có sẵn
\033[1;37m .queue\033[0m                  \033[1;30m|\033[0m Xem hàng chờ
\033[1;37m .skip / .stop / .now\033[0m     \033[1;30m|\033[0m Điều khiển
\033[1;37m .volume [1-100]\033[0m          \033[1;30m|\033[0m Âm lượng
\033[1;37m .loop / .pause / .resume\033[0m \033[1;30m|\033[0m Loop & Pause
```"""
        await ctx.send(menu)

    @commands.command(name="funmenu")
    async def _fun_menu_embed(self, ctx):
        """Menu giải trí bằng ANSI"""
        await ctx.message.delete()
        menu = f"""```ansi
\033[1;32m🎮 FUN MENU 🎮\033[0m

\033[1;37m .8ball / .rps / .trivia / .coinflip / .number\033[0m \033[1;30m|\033[0m Mini games
\033[1;37m .daily / .bal / .pay / .shop / .inventory\033[0m   \033[1;30m|\033[0m Economy
\033[1;37m .fact / .quote / .meme / .insult / .compliment\033[0m \033[1;30m|\033[0m Fun
\033[1;37m .avatar / .banner\033[0m              \033[1;30m|\033[0m Avatar & Banner
```"""
        await ctx.send(menu)

    @commands.command(name="progress")
    async def _test_progress(self, ctx, current: int = 50, total: int = 100):
        """Test progress bar"""
        await ctx.message.delete()
        bar = UIHelper.progress_bar(current, total)
        await ctx.send(f"📊 **Progress:** {bar}")

async def setup(bot):
    await bot.add_cog(UISystem(bot))
