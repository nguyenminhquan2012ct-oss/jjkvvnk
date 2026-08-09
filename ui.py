import discord
from discord.ext import commands
import asyncio
import time

class UIHelper:
    @staticmethod
    def progress_bar(current, total, length=20):
        filled = int(length * current / total) if total > 0 else 0
        bar = "█" * filled + "░" * (length - filled)
        percent = int(100 * current / total) if total > 0 else 0
        return f"`[{bar}] {percent}%`"

    @staticmethod
    def box(title, lines, color="36"):
        """Tao menu voi box-drawing characters"""
        w = 46
        border = "═" * w
        result = f"```ansi\n"
        result += f"\033[1;{color}m╔{border}╗\033[0m\n"
        result += f"\033[1;{color}m║\033[0m \033[1;37m{title:^{w-2}}\033[0m \033[1;{color}m║\033[0m\n"
        result += f"\033[1;{color}m╠{border}╣\033[0m\n"
        for line in lines:
            result += f"\033[1;{color}m║\033[0m {line:<{w-2}} \033[1;{color}m║\033[0m\n"
        result += f"\033[1;{color}m╚{border}╝\033[0m\n"
        result += "```"
        return result

class UISystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="menu")
    async def _main_menu(self, ctx):
        """Menu chinh"""
        p = self.bot.command_prefix
        lines = [
            f"\033[1;31m⚔️  {p}raid\033[0m      \033[1;30mWar / Spam\033[0m",
            f"\033[1;34m🎵  {p}nhac\033[0m      \033[1;30mAm thanh\033[0m",
            f"\033[1;32m🎮  {p}traloi\033[0m    \033[1;30mGiai tri\033[0m",
            f"\033[1;33m🛠️  {p}chucu\033[0m     \033[1;30mTien ich\033[0m",
            f"\033[1;35m🛡️  {p}quanly\033[0m    \033[1;30mQuan ly\033[0m",
            f"\033[1;36m🃏  {p}troll\033[0m     \033[1;30mTroll\033[0m",
            "",
            f"\033[1;30m{len(self.bot.guilds)} servers | {p}ngung = dung tat ca\033[0m",
        ]
        await ctx.send(UIHelper.box("DOMAIN EXPANSION: INFINITE VOID", lines, "35"))

    @commands.command(name="warmenu")
    async def _war_menu(self, ctx):
        """Menu war"""
        p = self.bot.command_prefix
        lines = [
            f"\033[1;31m⚡ SPAM\033[0m",
            f"  {p}vohahan [delay] [text]  \033[1;30m100 tin\033[0m",
            f"  {p}thuong [delay]         \033[1;30m100 tin ngon.txt\033[0m",
            f"  {p}lienke [delay] [@user] \033[1;30m100 tin nhay.txt\033[0m",
            f"  {p}hacmon [url] [d] [txt] \033[1;30mWebhook spam\033[0m",
            "",
            f"\033[1;34m🔊 VOICE\033[0m",
            f"  {p}ngucmon [id]           \033[1;30mTreo Voice\033[0m",
            f"  {p}loanvuc [id] [delay]   \033[1;30mSpam join/leave\033[0m",
            "",
            f"\033[1;31m🧨 DESTROY\033[0m",
            f"  {p}anpham [so] [emoji]    \033[1;30mReaction hang loat\033[0m",
            f"  {p}khaitram               \033[1;30mXoa toan bo kenh\033[0m",
            f"  {p}huydiet                \033[1;30mNuke server\033[0m",
            "",
            f"\033[1;33m{p}ngung = dung tat ca\033[0m",
        ]
        await ctx.send(UIHelper.box("PHUC MA NGU TOA: CHIEN TRANH", lines, "31"))

    @commands.command(name="musicmenu")
    async def _music_menu(self, ctx):
        """Menu nhac"""
        p = self.bot.command_prefix
        lines = [
            f"\033[1;34m🎶 PHAT NHAC\033[0m",
            f"  {p}play [link/ten]        \033[1;30mYouTube\033[0m",
            f"  {p}play-sa / play-sh      \033[1;30mCo san\033[0m",
            f"  {p}play-amk / play-sp     \033[1;30mCo san\033[0m",
            "",
            f"\033[1;32m📋 DIEU KHIEN\033[0m",
            f"  {p}queue                  \033[1;30mHang cho\033[0m",
            f"  {p}skip / stop / now      \033[1;30mTiec che\033[0m",
            f"  {p}loop / pause / resume  \033[1;30mLap / Tam dung\033[0m",
            f"  {p}volume [1-100]         \033[1;30mAm luong\033[0m",
        ]
        await ctx.send(UIHelper.box("PHAP DAN AM THANH", lines, "34"))

    @commands.command(name="funmenu")
    async def _fun_menu(self, ctx):
        """Menu giai tri"""
        p = self.bot.command_prefix
        lines = [
            f"\033[1;32m🎮 MINI GAMES\033[0m",
            f"  {p}8ball / rps / trivia    \033[1;30mGame\033[0m",
            f"  {p}coinflip / number      \033[1;30mDoan so\033[0m",
            "",
            f"\033[1;33m💰 ECONOMY\033[0m",
            f"  {p}daily / bal / pay      \033[1;30mVang\033[0m",
            f"  {p}shop / inventory       \033[1;30mCua hang\033[0m",
            "",
            f"\033[1;35m😂 FUN\033[0m",
            f"  {p}fact / quote / meme    \033[1;30mVui\033[0m",
            f"  {p}insult / compliment    \033[1;30mTroll\033[0m",
            f"  {p}avatar / banner        \033[1;30mAnh\033[0m",
        ]
        await ctx.send(UIHelper.box("PHAP DAN GIAI TRI", lines, "32"))

    @commands.command(name="progress")
    async def _test_progress(self, ctx, current: int = 50, total: int = 100):
        """Test progress bar"""
        bar = UIHelper.progress_bar(current, total)
        await ctx.send(f"📊 **Progress:** {bar}")

async def setup(bot):
    await bot.add_cog(UISystem(bot))
