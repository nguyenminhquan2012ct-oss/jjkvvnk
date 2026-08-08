import os
import sys
import subprocess
from importlib import metadata

# Các thư viện bắt buộc (nếu thiếu sẽ tự cài)
REQUIRED_PACKAGES = [
    "discord.py-self", "aiohttp", "pynacl", "pytz",
    "psutil", "requests", "colour", "python-dateutil"
]

def load_env_file(file=".env"):
    """Nạp file .env (nếu có) vào biến môi trường, không cần thư viện phụ."""
    if not os.path.exists(file):
        return
    try:
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key and key not in os.environ:
                    os.environ[key] = value
    except Exception:
        pass

def ensure_packages():
    installed = set()
    try:
        for dist in metadata.distributions():
            name = dist.metadata.get("Name")
            if name:
                installed.add(name.lower())
    except Exception:
        pass
    missing = [p for p in REQUIRED_PACKAGES if p.lower() not in installed]
    if not missing:
        return
    print(f"[!] Đang cài đặt thiếu: {', '.join(missing)}...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
        print("[+] Đã cài xong thư viện.")
    except Exception as e:
        print(f"[-] Lỗi cài đặt: {e}")
        sys.exit(1)

def main():
    load_env_file()
    check_env()
    ensure_packages()
    main_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "main.py")
    if not os.path.exists(main_file):
        print(f"[-] Không tìm thấy file chính: {main_file}")
        sys.exit(1)
    print(f"[>] Khởi động: {main_file}")
    try:
        sys.exit(subprocess.call([sys.executable, main_file]))
    except KeyboardInterrupt:
        print("\n[!] Đã đóng lãnh địa.")

def check_env():
    """Cảnh báo sớm nếu thiếu token, tiết kiệm lỗi khi chạy"""
    if os.environ.get("DISCORD_TOKEN") or os.environ.get("DISCORD_BOT_TOKEN") or os.path.exists("config.json"):
        return
    print("[!] Chưa có Token: đặt biến môi trường DISCORD_TOKEN hoặc tạo config.json.")

if __name__ == "__main__":
    main()