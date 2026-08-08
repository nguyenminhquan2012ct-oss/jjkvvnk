import os
import sys
import json
import signal
import subprocess
import threading
import time
from datetime import datetime

SETTINGS_FILE = "settings.json"
CONFIG_FILE = "config.json"
PYTHON = sys.executable

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
GRAY = "\033[1;30m"
PINK = "\033[1;95m"


def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_settings(data):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8-sig") as f:
            return json.load(f)
    return {}


def save_config(data):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def timestamp():
    return datetime.now().strftime("%H:%M:%S")


class HostBotConsole:
    def __init__(self):
        self.process = None
        self.running = False
        self.settings = load_settings()
        self.config = load_config()
        self.bot_name = self.settings.get("bot_name", "HostBot")
        self.author = self.settings.get("author", "QU4N.TH3.D3V")
        self.version = "6.2.0"

    def print_banner(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""{CYAN}
{YELLOW}                  {self.author}{RESET}
{CYAN}    ██╗   ██╗██╗   ██╗███╗   ██╗██╗  ██╗
{CYAN}    ██║   ██║██║   ██║████╗  ██║██║ ██╔╝
{CYAN}    ██║   ██║██║   ██║██╔██╗ ██║█████╔╝
{CYAN}    ╚██╗ ██╔╝╚██╗ ██╔╝██║╚██╗██║██╔═██╗
{CYAN}     ╚████╔╝  ╚████╔╝ ██║ ╚████║██║  ██╗
{CYAN}      ╚═══╝    ╚═══╝  ╚═╝  ╚═══╝╚═╝  ╚═╝{RESET}
{GRAY}    v{self.version} | Console Manager{RESET}
{GRAY}    {'=' * 50}{RESET}""")

    def log(self, msg, color=WHITE):
        print(f"  {GRAY}[{timestamp()}]{RESET} {color}{msg}{RESET}")

    def start_bot(self):
        if self.process and self.process.poll() is None:
            self.log("Bot dang chay roi! Dung . stop truoc.", YELLOW)
            return

        if not self.config.get("token") and not self.config.get("Token"):
            token = input(f"  {YELLOW}Nhap Discord Token: {RESET}").strip()
            if not token:
                self.log("Token trong! Huy.", RED)
                return
            self.config["token"] = token
            save_config(self.config)
            self.log("Da luu Token vao config.json", GREEN)

        self.log(f"Dang khoi dong {self.bot_name}...", CYAN)
        try:
            self.process = subprocess.Popen(
                [PYTHON, "main.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
            )
            self.running = True
            threading.Thread(target=self._read_output, daemon=True).start()
            self.log(f"{self.bot_name} da duoc khoi dong!", GREEN)
        except Exception as e:
            self.log(f"Loi khoi dong: {e}", RED)

    def _read_output(self):
        try:
            for line in self.process.stdout:
                print(f"  {GRAY}[BOT]{RESET} {line.rstrip()}")
        except Exception:
            pass
        finally:
            if self.process and self.process.poll() is not None:
                rc = self.process.returncode
                self.log(f"Bot da dung (exit code: {rc})", YELLOW)
                self.running = False
                self.process = None

    def stop_bot(self):
        if not self.process or self.process.poll() is not None:
            self.log("Bot chua duoc khoi dong.", YELLOW)
            return
        self.log(f"Dang dung {self.bot_name}...", YELLOW)
        try:
            if os.name == "nt":
                self.process.terminate()
            else:
                self.process.send_signal(signal.SIGTERM)
            self.process.wait(timeout=10)
            self.log(f"{self.bot_name} da dung.", GREEN)
        except subprocess.TimeoutExpired:
            self.process.kill()
            self.log(f"{self.bot_name} bi kill.", RED)
        except Exception as e:
            self.log(f"Loi dung bot: {e}", RED)
        finally:
            self.running = False
            self.process = None

    def restart_bot(self):
        self.log("Dang restart...", MAGENTA)
        self.stop_bot()
        time.sleep(1)
        self.start_bot()

    def kill_bot(self):
        if not self.process or self.process.poll() is not None:
            self.log("Bot chua duoc khoi dong.", YELLOW)
            return
        self.log(f"KILL {self.bot_name}!", RED)
        try:
            self.process.kill()
        except Exception:
            pass
        self.running = False
        self.process = None

    def show_status(self):
        if self.process and self.process.poll() is None:
            pid = self.process.pid
            self.log(f"{self.bot_name}: {GREEN}DANG CHAY{RESET} (PID: {pid})", GREEN)
        else:
            self.log(f"{self.bot_name}: {RED}DA DUNG{RESET}", RED)

    def show_config(self):
        print(f"\n  {CYAN}{'=' * 50}")
        print(f"  {WHITE}CAU HINH HIEN TAI")
        print(f"  {CYAN}{'=' * 50}{RESET}")

        token = self.config.get("token") or self.config.get("Token", "")
        masked = token[:8] + "..." + token[-4:] if len(token) > 12 else "***"
        print(f"  {GRAY}Token:{RESET}      {masked}")
        print(f"  {GRAY}Prefix:{RESET}     {self.config.get('prefix', self.config.get('Prefix', '.'))}")
        print(f"  {GRAY}Bot Name:{RESET}   {self.settings.get('bot_name', 'HostBot')}")
        print(f"  {GRAY}Author:{RESET}     {self.settings.get('author', 'QU4N.TH3.D3V')}")
        print(f"  {GRAY}Auto GIF:{RESET}   {self.settings.get('auto_gif', True)}")

        print(f"\n  {YELLOW}GIF Responses:{RESET}")
        gifs = self.settings.get("gif_responses", {})
        for key, url in gifs.items():
            short = url[:50] + "..." if len(url) > 50 else url
            print(f"    {GRAY}{key}:{RESET} {short}")

        print(f"\n  {YELLOW}Status Cycle:{RESET}")
        for s in self.settings.get("status_cycle", []):
            print(f"    {GRAY}- {s}{RESET}")
        print(f"  {CYAN}{'=' * 50}{RESET}\n")

    def set_config(self, key, value):
        if not key:
            self.log("Dung: .config <key> <value>", YELLOW)
            return
        if key == "bot_name":
            self.settings["bot_name"] = value or "HostBot"
            self.bot_name = self.settings["bot_name"]
            save_settings(self.settings)
            self.log(f"Bot name: {self.bot_name}", GREEN)
        elif key == "author":
            self.settings["author"] = value or "QU4N.TH3.D3V"
            self.author = self.settings["author"]
            save_settings(self.settings)
            self.log(f"Author: {self.author}", GREEN)
        elif key == "prefix":
            self.config["prefix"] = value or "."
            save_config(self.config)
            self.log(f"Prefix: {self.config['prefix']}", GREEN)
        elif key == "token":
            if value:
                self.config["token"] = value
                save_config(self.config)
                self.log("Token da duoc cap nhat!", GREEN)
            else:
                self.log("Nhap: .config token <token>", YELLOW)
        elif key == "auto_gif":
            self.settings["auto_gif"] = value.lower() in ("true", "1", "yes", "on")
            save_settings(self.settings)
            self.log(f"Auto GIF: {self.settings['auto_gif']}", GREEN)
        elif key.startswith("gif_"):
            category = key[4:]
            gifs = self.settings.get("gif_responses", {})
            if value:
                gifs[category] = value
            else:
                gifs.pop(category, None)
            self.settings["gif_responses"] = gifs
            save_settings(self.settings)
            self.log(f"GIF '{category}': {value or '(da xoa)'}", GREEN)
        else:
            self.log(f"Key khong hop le: {key}", RED)
            self.log("Keys: bot_name, author, prefix, token, auto_gif, gif_<category>", GRAY)

    def add_status(self, *args):
        text = " ".join(args)
        if not text:
            self.log("Dung: .status_add <text>", YELLOW)
            return
        cycle = self.settings.get("status_cycle", [])
        cycle.append(text)
        self.settings["status_cycle"] = cycle
        save_settings(self.settings)
        self.log(f"Da them status: {text}", GREEN)

    def remove_status(self, index):
        cycle = self.settings.get("status_cycle", [])
        try:
            idx = int(index) - 1
            removed = cycle.pop(idx)
            self.settings["status_cycle"] = cycle
            save_settings(self.settings)
            self.log(f"Da xoa: {removed}", GREEN)
        except (ValueError, IndexError):
            self.log("So thu tu khong hop le.", RED)

    def list_status(self):
        cycle = self.settings.get("status_cycle", [])
        if not cycle:
            self.log("Chua co status nao.", YELLOW)
            return
        print(f"\n  {CYAN}Status Cycle:{RESET}")
        for i, s in enumerate(cycle, 1):
            print(f"    {GRAY}{i}.{RESET} {s}")
        print()

    def add_gif(self, category, url):
        if not category or not url:
            self.log("Dung: .gif_add <category> <url>", YELLOW)
            return
        gifs = self.settings.get("gif_responses", {})
        gifs[category] = url
        self.settings["gif_responses"] = gifs
        save_settings(self.settings)
        self.log(f"GIF '{category}' da duoc them.", GREEN)

    def remove_gif(self, category):
        gifs = self.settings.get("gif_responses", {})
        if category in gifs:
            del gifs[category]
            self.settings["gif_responses"] = gifs
            save_settings(self.settings)
            self.log(f"GIF '{category}' da duoc xoa.", GREEN)
        else:
            self.log(f"Khong tim thay GIF '{category}'.", YELLOW)

    def list_gifs(self):
        gifs = self.settings.get("gif_responses", {})
        if not gifs:
            self.log("Chua co GIF nao.", YELLOW)
            return
        print(f"\n  {CYAN}GIF Responses:{RESET}")
        for cat, url in gifs.items():
            short = url[:60] + "..." if len(url) > 60 else url
            print(f"    {GRAY}{cat}:{RESET} {short}")
        print()

    def send_console_msg(self, channel_id, *args):
        text = " ".join(args)
        if not channel_id or not text:
            self.log("Dung: .say <channel_id> <message>", YELLOW)
            return
        if not self.process or self.process.poll() is not None:
            self.log("Bot dang khong chay.", YELLOW)
            return
        self.log(f"Gui tin nhan den #{channel_id}: {text}", CYAN)

    def show_help(self):
        print(f"""
  {CYAN}{'=' * 55}
  {WHITE}{BOLD}HOSTBOT CONSOLE - v{self.version}
  {CYAN}{'=' * 55}{RESET}

  {YELLOW}[BOT CONTROL]{RESET}
  {GRAY}  start{RESET}              Khoi dong bot
  {GRAY}  stop{RESET}               Dung bot
  {GRAY}  restart{RESET}            Restart bot
  {GRAY}  kill{RESET}               Force kill bot
  {GRAY}  status{RESET}             Xem trang thai bot

  {YELLOW}[CONFIG]{RESET}
  {GRAY}  config{RESET}             Xem tat ca cau hinh
  {GRAY}  config <key> <value>{RESET}  Thay doi cau hinh
  {GRAY}  set <key> <value>{RESET}     Alias cua config

  {YELLOW}[BOT NAME & AUTHOR]{RESET}
  {GRAY}  config bot_name <name>{RESET}  Doi ten bot
  {GRAY}  config author <name>{RESET}    Doi ten tac gia
  {GRAY}  config prefix <char>{RESET}    Doi prefix (mac dinh: .)
  {GRAY}  config token <token>{RESET}    Doi token

  {YELLOW}[GIF RESPONSES]{RESET}
  {GRAY}  gif_add <category> <url>{RESET}  Them GIF cho category
  {GRAY}  gif_del <category>{RESET}        Xoa GIF
  {GRAY}  gif_list{RESET}                  Danh sach GIF
  {GRAY}  config auto_gif <true/false>{RESET}  Bat/tat auto GIF

  {YELLOW}[STATUS CYCLE]{RESET}
  {GRAY}  status_add <text>{RESET}     Them status moi
  {GRAY}  status_del <number>{RESET}   Xoa status theo STT
  {GRAY}  status_list{RESET}           Danh sach status

  {YELLOW}[UTILITY]{RESET}
  {GRAY}  say <channel_id> <msg>{RESET}  Gui tin nhan den kenh
  {GRAY}  servers{RESET}               Danh sach server
  {GRAY}  help{RESET}                  Hien thi menu nay
  {GRAY}  clear{RESET}                 Xoa man hinh
  {GRAY}  exit{RESET}                  thoat console

  {YELLOW}[SHORTCUTS]{RESET}
  {GRAY}  s{RESET} = start | {GRAY}p{RESET} = stop | {GRAY}r{RESET} = restart | {GRAY}q{RESET} = exit
  {CYAN}{'=' * 55}{RESET}
""")

    def run(self):
        self.print_banner()
        self.log(f"Console san sang. Go {YELLOW}help{RESET} de xem huong dan.", GREEN)
        print()

        while True:
            try:
                raw = input(f"  {PINK}{self.bot_name}{RESET} {GRAY}>{RESET} ").strip()
                if not raw:
                    continue

                parts = raw.split()
                cmd = parts[0].lower()
                args = parts[1:]

                if cmd in ("start", "s"):
                    self.start_bot()
                elif cmd in ("stop", "p"):
                    self.stop_bot()
                elif cmd in ("restart", "r"):
                    self.restart_bot()
                elif cmd == "kill":
                    self.kill_bot()
                elif cmd == "status":
                    self.show_status()
                elif cmd in ("config", "set"):
                    if not args:
                        self.show_config()
                    elif len(args) == 1:
                        key = args[0]
                        val = self.config.get(key) or self.settings.get(key, "")
                        self.log(f"{key} = {val}", CYAN)
                    else:
                        self.set_config(args[0], " ".join(args[1:]))
                elif cmd == "gif_add":
                    if len(args) >= 2:
                        self.add_gif(args[0], " ".join(args[1:]))
                    else:
                        self.log("Dung: gif_add <category> <url>", YELLOW)
                elif cmd == "gif_del":
                    if args:
                        self.remove_gif(args[0])
                    else:
                        self.log("Dung: gif_del <category>", YELLOW)
                elif cmd == "gif_list":
                    self.list_gifs()
                elif cmd == "status_add":
                    self.add_status(*args)
                elif cmd == "status_del":
                    if args:
                        self.remove_status(args[0])
                    else:
                        self.log("Dung: status_del <number>", YELLOW)
                elif cmd == "status_list":
                    self.list_status()
                elif cmd == "say":
                    if len(args) >= 2:
                        self.send_console_msg(args[0], *args[1:])
                    else:
                        self.log("Dung: say <channel_id> <message>", YELLOW)
                elif cmd == "servers":
                    if self.process and self.process.poll() is None:
                        self.log("Dang xem servers...", CYAN)
                    else:
                        self.log("Bot dang khong chay.", YELLOW)
                elif cmd == "help":
                    self.show_help()
                elif cmd == "clear":
                    os.system("cls" if os.name == "nt" else "clear")
                    self.print_banner()
                elif cmd in ("exit", "quit", "q"):
                    if self.process and self.process.poll() is None:
                        self.log("Dang dung bot truoc khi thoat...", YELLOW)
                        self.stop_bot()
                    self.log("Tam biet!", MAGENTA)
                    sys.exit(0)
                else:
                    self.log(f"Lenh khong ton tai: {cmd}. Go {YELLOW}help{RESET} de xem danh sach.", RED)

            except KeyboardInterrupt:
                print()
                self.log("Nhan Ctrl+C de thoat. Go {YELLOW}exit{RESET}.", YELLOW)
            except EOFError:
                break
            except Exception as e:
                self.log(f"Loi: {e}", RED)


if __name__ == "__main__":
    console = HostBotConsole()
    console.run()
