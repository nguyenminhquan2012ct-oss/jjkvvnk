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
    def war_embed(title, description, **kwargs):
        return discord.Embed(title=title, description=description, color=WAR_COLOR, **kwargs)

    @staticmethod
    def music_embed(title, description, **kwargs):
        return discord.Embed(title=title, description=description, color=MUSIC_COLOR, **kwargs)

    @staticmethod
    def fun_embed(title, description, **kwargs):
        return discord.Embed(title=title, description=description, color=FUN_COLOR, **kwargs)

    @staticmethod
    def utility_embed(title, description, **kwargs):
        return discord.Embed(title=title, description=description, color=UTILITY_COLOR, **kwargs)

    @staticmethod
    def special_embed(title, description, **kwargs):
        return discord.Embed(title=title, description=description, color=SPECIAL_COLOR, **kwargs)

    @staticmethod
    def progress_bar(current, total, length=20):
        filled = int(length * current / total) if total > 0 else 0
        bar = "█" * filled + "░" * (length - filled)
        percent = int(100 * current / total) if total > 0 else 0
        return f"`[{bar}] {percent}%`"

    @staticmethod
    def pagination_embed(items, page, per_page, title="Danh sách", color=UTILITY_COLOR):
        total_pages = max(1, (len(items) + per_page - 1) // per_page)
        page = max(0, min(page, total_pages - 1))
        start = page * per_page
        end = start + per_page
        page_items = items[start:end]
        embed = discord.Embed(title=f"{title} (Trang {page + 1}/{total_pages})", color=color)
        return embed, page_items, page, total_pages

class UIPaginator:
    def __init__(self, ctx, pages, timeout=60):
        self.ctx = ctx
        self.pages = pages
        self.current = 0
        self.timeout = timeout
        self.message = None

    async def start(self):
        if not self.pages:
            return
        await self._show_page()
        self.message = self.ctx.sent_message if hasattr(self.ctx, "sent_message") else None

    async def _show_page(self):
        if hasattr(self.ctx, "send"):
            pass

class UISystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="menu")
    async def _main_menu(self, ctx):
        """Menu chính đẹp"""
        await ctx.message.delete()
        embed = discord.Embed(
            title="💫 DOMAIN EXPANSION: INFINITE VOID 💫",
            description="**Lãnh địa đã sẵn sàng!** Chọn thuật thức bên dưới:",
            color=SPECIAL_COLOR
        )
        embed.add_field(name="⚔️ WAR", value="`.raid` - Menu chiến tranh", inline=True)
        embed.add_field(name="🎵 MUSIC", value="`.nhac` - Menu nhạc", inline=True)
        embed.add_field(name="🎮 FUN", value="`.traloi` - Menu giải trí", inline=True)
        embed.add_field(name="🛠️ UTILITY", value="`.chucu` - Menu tiện ích", inline=True)
        embed.add_field(name="🛡️ ADMIN", value="`.quanly` - Menu quản lý", inline=True)
        embed.add_field(name="🃏 TROLL", value="`.troll` - Menu troll", inline=True)
        embed.set_footer(text=f"JJK-VVNK Bot | {len(self.bot.guilds)} servers")
        await ctx.send(embed=embed)

    @commands.command(name="warmenu")
    async def _war_menu_embed(self, ctx):
        """Menu war bằng Embed"""
        await ctx.message.delete()
        embed = discord.Embed(title="⚔️ WAR MENU", description="Thuật thức chiến tranh", color=WAR_COLOR)
        embed.add_field(name="`.vohahan [delay] [text]`", value="Spam tùy chỉnh", inline=False)
        embed.add_field(name="`.thuong [delay]`", value="Spam ngon.txt", inline=False)
        embed.add_field(name="`.lienke [delay]`", value="Spam nhay.txt", inline=False)
        embed.add_field(name="`.hacmon [url] [delay] [text]`", value="Webhook spam", inline=False)
        embed.add_field(name="`.khaitram`", value="Xóa toàn bộ kênh", inline=False)
        embed.add_field(name="`.huydiet`", value="Nuke server", inline=False)
        embed.add_field(name="`.ngung`", value="Dừng tất cả", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="musicmenu")
    async def _music_menu_embed(self, ctx):
        """Menu nhạc bằng Embed"""
        await ctx.message.delete()
        embed = discord.Embed(title="🎵 MUSIC MENU", description="Thuật thức âm thanh", color=MUSIC_COLOR)
        embed.add_field(name="`.play [link/tên]`", value="Phát nhạc YouTube", inline=False)
        embed.add_field(name="`.play-sa / play-sh / play-amk / play-sp`", value="Nhạc có sẵn", inline=False)
        embed.add_field(name="`.queue`", value="Xem hàng chờ", inline=False)
        embed.add_field(name="`.skip / .stop / .now`", value="Điều khiển", inline=False)
        embed.add_field(name="`.volume [1-100]`", value="Âm lượng", inline=False)
        embed.add_field(name="`.loop / .pause / .resume`", value="Loop & Pause", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="funmenu")
    async def _fun_menu_embed(self, ctx):
        """Menu giải trí bằng Embed"""
        await ctx.message.delete()
        embed = discord.Embed(title="🎮 FUN MENU", description="Mini games & Fun", color=FUN_COLOR)
        embed.add_field(name="`.8ball / .rps / .trivia / .coinflip / .number`", value="Mini games", inline=False)
        embed.add_field(name="`.daily / .bal / .pay / .shop / .inventory`", value="Economy", inline=False)
        embed.add_field(name="`.fact / .quote / .meme / .insult / .compliment`", value="Fun", inline=False)
        embed.add_field(name="`.avatar / .banner`", value="Avatar & Banner", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="progress")
    async def _test_progress(self, ctx, current: int = 50, total: int = 100):
        """Test progress bar"""
        await ctx.message.delete()
        bar = UIHelper.progress_bar(current, total)
        await ctx.send(f"📊 **Progress:** {bar}")

async def setup(bot):
    await bot.add_cog(UISystem(bot))
