import subprocess
import os
import sys
import time
from importlib import metadata

# Danh sách thư viện (Thuật thức bổ trợ)
packages = [
    "discord.py-self", "requests", "pynacl", "python-dateutil",
    "instaloader", "psutil", "pytz", "protobuf==3.20.3", "colour"
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def domain_visual():
    clear_console()
    # Hiệu ứng chữ chạy khi khai triển lãnh địa
    text = """
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃        🤞 DOMAIN EXPANSION: INFINITE VOID 🤞        ┃
    ┃              (BÀNH TRƯỚNG LÃNH ĐỊA)                  ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """
    print(f"\033[1;35m{text}\033[0m") # Màu tím Gojo

def check_and_install():
    installed = set()
    try:
        for dist in metadata.distributions():
            name = dist.metadata.get("Name")
            if name:
                installed.add(name.lower())
    except Exception:
        pass
    missing = [p for p in packages if p.split('==')[0].lower() not in installed]
    
    if missing:
        print(f"\033[1;33m[!] Đang chuẩn bị thuật thức (Cài đặt): {missing}...\033[0m")
        python = sys.executable
        try:
            subprocess.check_call([python, "-m", "pip", "install", *missing], stdout=subprocess.DEVNULL)
            print("✅ Thuật thức đã sẵn sàng.")
        except Exception as e:
            print(f"❌ Lỗi kết giới: {e}")
            sys.exit()
    else:
        print("\033[1;32m[+] Kết giới ổn định. Đang tiến vào lãnh địa...\033[0m")
        time.sleep(1)

def run_bot():
    main_file = "main.py" 
    
    if os.path.exists(main_file):
        try:
            print(f"\033[1;36m[>] Triệu hồi: {main_file}...\033[0m")
            print("-" * 50)
            # Chạy bot chính
            subprocess.check_call([sys.executable, main_file])
        except subprocess.CalledProcessError as e:
            print(f"\033[1;31m❌ Lãnh địa bị vỡ: {e}\033[0m")
    else:
        print(f"\033[1;31m❌ Không tìm thấy 'Vật tế' ({main_file})!\033[0m")

def main():
    domain_visual()
    check_and_install()
    run_bot()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Đã đóng lãnh địa.\033[0m")