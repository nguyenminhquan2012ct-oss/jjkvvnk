import os
import sys
import json
import re
import asyncio
import aiohttp

import discord
from discord.ext import commands
from pytz import timezone

import rate_utils

# --- 1. CẤU HÌNH (Kết giới): ưu tiên Biến môi trường, fallback config.json ---
TOKEN = os.environ.get("DISCORD_TOKEN") or os.environ.get("DISCORD_BOT_TOKEN") or os.environ.get("BOT_TOKEN")
PREFIX = os.environ.get("DISCORD_PREFIX", ".")

if not TOKEN and os.path.exists('config.json'):
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    TOKEN = config.get('token')
    PREFIX = config.get('prefix') or PREFIX

if not TOKEN:
    if not os.path.exists('config.json'):
        with open('config.json', 'w', encoding='utf-8') as f:
            json.dump({"token": "DÁN_TOKEN_VÀO_ĐÂY", "prefix": PREFIX}, f, indent=4)
    print("\033[1;31m[!] Không tìm thấy Token!\033[0m")
    print("\033[1;33m  -> Cách 1: đặt Biến môi trường DISCORD_TOKEN (hoặc DISCORD_BOT_TOKEN)\033[0m")
    print("\033[1;33m  -> Cách 2: dán Token vào config.json rồi chạy lại\033[0m")
    sys.exit(1)

# --- 2. BIẾN TRẠNG THÁI (Thuật thức bổ trợ) ---
vietnam_tz = timezone('Asia/Ho_Chi_Minh')
active_features = {
    'cyclestatus': False, 
    'auto_react': False, 
    'thuong': False, 
    'he': False, 
    'forcedisconnect': False,
    'nitro_sniper': True 
}

# --- 3. HEADER VIP (Giả lập Windows để né Discord quét) ---
def get_main_headers():
    return {
        'accept': '*/*',
        'authorization': TOKEN,
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.1072 Chrome/120.0.6099.291 Safari/537.36',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJwdGIiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC4xMDcyIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDQiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjEwNzIgQ2hyb21lLzEyMC4wLjYwOTkuMjkxIEVsZWN0cm9uLzI4LjIuMTAgU2FmYXJpLzUzNy4zNiJ9'
    }

# --- 4. KHỞI TẠO THỰC THỂ BOT ---
bot = commands.Bot(command_prefix=PREFIX, self_bot=True, help_command=None)

# --- 5. SỰ KIỆN KHAI TRIỂN LÃNH ĐỊA (On Ready) ---
@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""\033[1;35m
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃        🤞 DOMAIN EXPANSION: INFINITE VOID 🤞         ┃
    ┃              (BÀNH TRƯỚNG LÃNH ĐỊA)                  ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0m"""
    print(banner)
    print(f"\033[1;36m[>] CHÚ THUẬT SƯ:\033[0m \033[1;32m{bot.user}\033[0m")
    print(f"\033[1;36m[>] ĐỊNH DANH ID:\033[0m \033[1;32m{bot.user.id}\033[0m")
    print(f"\033[1;35m{'-'*54}\033[0m")
    
    # Tự động nạp Cogs (file .py cùng thư mục, ngoại trừ main.py)
    skip = {'main.py', 'index.py', 'rate_utils.py', '__init__.py'}
    for filename in os.listdir('.'):
        if filename.endswith('.py') and filename not in skip:
            try:
                await bot.load_extension(filename[:-3])
                print(f"\033[1;32m    + Đã nạp thuật thức: {filename}\033[0m")
            except Exception as e:
                print(f"\033[1;31m    - Lỗi nạp {filename}: {e}\033[0m")
    
    print(f"\033[1;35m{'-'*54}\033[0m")
    print(f"\033[1;32m[SUCCESS] Lãnh địa đã sẵn sàng. Gõ {PREFIX}lanhdia để mở Menu.\033[0m")

# --- 6. THUẬT THỨC TẤT TRÚNG (Nitro Sniper) ---
@bot.event
async def on_message(message):
    if active_features['nitro_sniper']:
        if 'discord.gift/' in message.content or 'discordapp.com/gifts/' in message.content:
            match = re.search(r"(discord\.gift\/|discordapp\.com\/gifts\/)(\w+)", message.content)
            if not match:
                return
            code = match.group(2)
            url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}/redeem"
            resp = None
            for _ in range(3):
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=get_main_headers()) as resp:
                        if resp.status != 429:
                            break
                        await rate_utils.handle_429_response(resp)
            if resp is not None and resp.status == 200:
                print(f"\033[1;32m[+] ĐÃ HÚP ĐƯỢC NITRO: {code}\033[0m")
            else:
                print(f"\033[1;31m[-] Hụt Nitro: {code}\033[0m")
    
    await bot.process_commands(message)

# --- 7. KHỞI CHẠY ---
async def main():
    async with bot:
        await bot.start(TOKEN)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\033[1;31m\n[!] Đã thu hồi lãnh địa.\033[0m")
    except Exception as e:
        print(f"\033[1;31m[!] Lỗi hệ thống: {e}\033[0m")