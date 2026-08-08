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
DEFAULTS_FILE = "settings.default.json"
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


def load_json(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def deep_merge(base, override):
    result = base.copy()
    for k, v in override.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = v
    return result


def timestamp():
    return datetime.now().strftime("%H:%M:%S")


DEFAULT_SETTINGS = {
    "bot_name": "HostBot",
    "author": "QU4N.TH3.D3V",
    "auto_gif": True,
    "gif_responses": {
        "raid": "https://media.tenor.com/images/memes/sukuna-memes/sukuna-meme.gif",
        "spam": "https://media.tenor.com/images/memes/sukuna-memes/sukuna-meme.gif",
        "nuke": "https://media.tenor.com/images/memes/sukuna-memes/sukuna-meme.gif",
        "music": "https://media.tenor.com/images/memes/sukuna-memes/sukuna-meme.gif",
        "fun": "https://media.tenor.com/images/memes/sukuna-memes/sukuna-meme.gif",
        "troll": "https://media.tenor.com/images/memes/sukuna-memes/sukuna-meme.gif",
        "admin": "https://media.tenor.com/images/memes/sukuna-memes/sukuna-meme.gif",
    },
    "status_cycle": [".menu de mo Menu", "HostBot v6.2", "Dung .help de tro giup"],
    "menu": {
        "title": "DOMAIN EXPANSION: INFINITE VOID",
        "description": "Lanh dia da san sang! Chon thuat thuc ben duoi:",
        "footer": "HostBot | {servers} servers",
        "color_main": "0x800080",
        "sections": {
            "war": {"name": "WAR", "emoji": "⚔️", "color": "0xFF0000", "command": "raid", "desc": "Menu chien tranh"},
            "music": {"name": "MUSIC", "emoji": "🎵", "color": "0x00AAFF", "command": "nhac", "desc": "Menu nhac"},
            "fun": {"name": "FUN", "emoji": "🎮", "color": "0x00FF00", "command": "traloi", "desc": "Menu giai tri"},
            "utility": {"name": "UTILITY", "emoji": "🛠️", "color": "0xFFFF00", "command": "chucu", "desc": "Menu tien ich"},
            "admin": {"name": "ADMIN", "emoji": "🛡️", "color": "0xFF0000", "command": "quanly", "desc": "Menu quan ly"},
            "troll": {"name": "TROLL", "emoji": "🃏", "color": "0x00FFFF", "command": "troll", "desc": "Menu troll"},
        },
    },
    "command_aliases": {},
}


class HostBotConsole:
    def __init__(self):
        self.process = None
        self.running = False
        self.settings = load_json(SETTINGS_FILE)
        self.config = load_json(CONFIG_FILE)
        self.bot_name = self.settings.get("bot_name", "HostBot")
        self.author = self.settings.get("author", "QU4N.TH3.D3V")
        self.version = "6.3.0"

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
            self.log("Bot dang chay roi! Dung stop truoc.", YELLOW)
            return
        if not self.config.get("token") and not self.config.get("Token"):
            token = input(f"  {YELLOW}Nhap Discord Token: {RESET}").strip()
            if not token:
                self.log("Token trong! Huy.", RED)
                return
            self.config["token"] = token
            save_json(CONFIG_FILE, self.config)
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
                self.log(f"Bot da dung (exit: {self.process.returncode})", YELLOW)
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
            self.log(f"{self.bot_name}: {GREEN}DANG CHAY{RESET} (PID: {self.process.pid})", GREEN)
        else:
            self.log(f"{self.bot_name}: {RED}DA DUNG{RESET}", RED)

    def show_config(self):
        print(f"\n  {CYAN}{'=' * 55}")
        print(f"  {WHITE}CAU HINH HIEN TAI")
        print(f"  {CYAN}{'=' * 55}{RESET}")
        token = self.config.get("token") or self.config.get("Token", "")
        masked = token[:8] + "..." + token[-4:] if len(token) > 12 else "***"
        print(f"  {GRAY}Token:{RESET}          {masked}")
        print(f"  {GRAY}Prefix:{RESET}         {self.config.get('prefix', self.config.get('Prefix', '.'))}")
        print(f"  {GRAY}Bot Name:{RESET}       {self.settings.get('bot_name', 'HostBot')}")
        print(f"  {GRAY}Author:{RESET}         {self.settings.get('author', 'QU4N.TH3.D3V')}")
        print(f"  {GRAY}Auto GIF:{RESET}       {self.settings.get('auto_gif', True)}")
        print(f"\n  {YELLOW}[ Menu ]{RESET}")
        menu = self.settings.get("menu", {})
        print(f"    {GRAY}Title:{RESET}       {menu.get('title', 'N/A')}")
        print(f"    {GRAY}Description:{RESET} {menu.get('description', 'N/A')}")
        print(f"    {GRAY}Color:{RESET}       {menu.get('color_main', 'N/A')}")
        sections = menu.get("sections", {})
        for key, sec in sections.items():
            print(f"    {GRAY}{key}:{RESET} {sec.get('emoji','')} {sec.get('name','')} -> {sec.get('command','')} ({sec.get('desc','')})")
        print(f"\n  {YELLOW}[ Command Aliases ]{RESET}")
        aliases = self.settings.get("command_aliases", {})
        if aliases:
            for cmd, alias in list(aliases.items())[:10]:
                print(f"    {GRAY}{cmd}{RESET} -> {alias}")
            if len(aliases) > 10:
                print(f"    {GRAY}... va {len(aliases) - 10} lenh khac{RESET}")
        else:
            print(f"    {GRAY}Chua co alias nao{RESET}")
        print(f"  {CYAN}{'=' * 55}{RESET}\n")

    def set_config(self, key, value):
        if not key:
            self.log("Dung: config <key> <value>", YELLOW)
            return
        handlers = {
            "bot_name": lambda v: (self.settings.__setitem__("bot_name", v or "HostBot"), self.__dict__.__setitem__("bot_name", v or "HostBot")),
            "author": lambda v: (self.settings.__setitem__("author", v or "QU4N.TH3.D3V"), self.__dict__.__setitem__("author", v or "QU4N.TH3.D3V")),
            "prefix": lambda v: self.config.__setitem__("prefix", v or "."),
            "token": lambda v: self.config.__setitem__("token", v) if v else None,
            "auto_gif": lambda v: self.settings.__setitem__("auto_gif", v.lower() in ("true", "1", "yes", "on")),
        }
        if key in handlers:
            handlers[key](value)
            save_json(SETTINGS_FILE, self.settings)
            save_json(CONFIG_FILE, self.config)
            self.log(f"{key} = {value or '(mac dinh)'}", GREEN)
        elif key.startswith("gif_"):
            cat = key[4:]
            gifs = self.settings.get("gif_responses", {})
            if value:
                gifs[cat] = value
            else:
                gifs.pop(cat, None)
            self.settings["gif_responses"] = gifs
            save_json(SETTINGS_FILE, self.settings)
            self.log(f"GIF '{cat}': {value or '(da xoa)'}", GREEN)
        else:
            self.log(f"Key khong hop le: {key}", RED)

    def add_status(self, *args):
        text = " ".join(args)
        if not text:
            self.log("Dung: status_add <text>", YELLOW)
            return
        cycle = self.settings.get("status_cycle", [])
        cycle.append(text)
        self.settings["status_cycle"] = cycle
        save_json(SETTINGS_FILE, self.settings)
        self.log(f"Da them status: {text}", GREEN)

    def remove_status(self, index):
        cycle = self.settings.get("status_cycle", [])
        try:
            idx = int(index) - 1
            removed = cycle.pop(idx)
            self.settings["status_cycle"] = cycle
            save_json(SETTINGS_FILE, self.settings)
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
            self.log("Dung: gif_add <category> <url>", YELLOW)
            return
        gifs = self.settings.get("gif_responses", {})
        gifs[category] = url
        self.settings["gif_responses"] = gifs
        save_json(SETTINGS_FILE, self.settings)
        self.log(f"GIF '{category}' da duoc them.", GREEN)

    def remove_gif(self, category):
        gifs = self.settings.get("gif_responses", {})
        if category in gifs:
            del gifs[category]
            self.settings["gif_responses"] = gifs
            save_json(SETTINGS_FILE, self.settings)
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

    # ================= MENU CUSTOMIZATION =================

    def set_menu(self, key, value):
        menu = self.settings.get("menu", {})
        if key == "title":
            menu["title"] = value
        elif key == "desc":
            menu["description"] = value
        elif key == "footer":
            menu["footer"] = value
        elif key == "color":
            menu["color_main"] = value
        else:
            self.log("Keys: title, desc, footer, color", YELLOW)
            return
        self.settings["menu"] = menu
        save_json(SETTINGS_FILE, self.settings)
        self.log(f"Menu {key} = {value}", GREEN)

    def set_section(self, section, key, value):
        menu = self.settings.get("menu", {})
        sections = menu.get("sections", {})
        if section not in sections:
            self.log(f"Section khong ton tai: {section}", RED)
            self.log("Sections: war, music, fun, utility, admin, troll", GRAY)
            return
        if key not in ("name", "emoji", "command", "desc", "color"):
            self.log("Keys: name, emoji, command, desc, color", YELLOW)
            return
        sections[section][key] = value
        menu["sections"] = sections
        self.settings["menu"] = menu
        save_json(SETTINGS_FILE, self.settings)
        self.log(f"Section '{section}' {key} = {value}", GREEN)

    def list_sections(self):
        menu = self.settings.get("menu", {})
        sections = menu.get("sections", {})
        print(f"\n  {CYAN}Menu Sections:{RESET}")
        for key, sec in sections.items():
            print(f"    {GRAY}{key}:{RESET} {sec.get('emoji','')} {sec.get('name','')} -> {sec.get('command','')} ({sec.get('desc','')})")
        print()

    # ================= COMMAND ALIASES =================

    def set_alias(self, command, alias):
        if not command or not alias:
            self.log("Dung: alias <command> <alias>", YELLOW)
            return
        aliases = self.settings.get("command_aliases", {})
        aliases[command] = alias
        self.settings["command_aliases"] = aliases
        save_json(SETTINGS_FILE, self.settings)
        self.log(f"Alias: {command} -> {alias}", GREEN)

    def remove_alias(self, command):
        aliases = self.settings.get("command_aliases", {})
        if command in aliases:
            del aliases[command]
            self.settings["command_aliases"] = aliases
            save_json(SETTINGS_FILE, self.settings)
            self.log(f"Da xoa alias: {command}", GREEN)
        else:
            self.log(f"Khong tim thay alias: {command}", YELLOW)

    def list_aliases(self):
        aliases = self.settings.get("command_aliases", {})
        if not aliases:
            self.log("Chua co alias nao.", YELLOW)
            return
        print(f"\n  {CYAN}Command Aliases:{RESET}")
        for cmd, alias in aliases.items():
            print(f"    {GRAY}{cmd}{RESET} -> {alias}")
        print()

    # ================= RESET DEFAULTS =================

    def reset_all(self):
        save_json(SETTINGS_FILE, DEFAULT_SETTINGS)
        self.settings = DEFAULT_SETTINGS.copy()
        self.bot_name = self.settings["bot_name"]
        self.author = self.settings["author"]
        self.log("Da dat lai tat ca cau hinh ve mac dinh!", GREEN)

    def reset_menu(self):
        self.settings["menu"] = DEFAULT_SETTINGS["menu"].copy()
        save_json(SETTINGS_FILE, self.settings)
        self.log("Da dat lai menu ve mac dinh!", GREEN)

    def reset_gifs(self):
        self.settings["gif_responses"] = DEFAULT_SETTINGS["gif_responses"].copy()
        save_json(SETTINGS_FILE, self.settings)
        self.log("Da dat lai GIF ve mac dinh!", GREEN)

    def reset_aliases(self):
        self.settings["command_aliases"] = {}
        save_json(SETTINGS_FILE, self.settings)
        self.log("Da xoa tat ca alias!", GREEN)

    # ================= HELP =================

    def show_help(self):
        print(f"""
  {CYAN}{'=' * 60}
  {WHITE}{BOLD}HOSTBOT CONSOLE - v{self.version}
  {CYAN}{'=' * 60}{RESET}

  {YELLOW}[ DIEU KHIEN BOT ]{RESET}
  {GRAY}  start{RESET}                    Khoi dong bot
  {GRAY}  stop{RESET}                     Dung bot
  {GRAY}  restart{RESET}                  Restart bot
  {GRAY}  kill{RESET}                     Force kill bot
  {GRAY}  status{RESET}                   Xem trang thai bot

  {YELLOW}[ CAU HINH CO BAN ]{RESET}
  {GRAY}  config{RESET}                   Xem tat ca cau hinh
  {GRAY}  config bot_name <ten>{RESET}     Doi ten bot
  {GRAY}  config author <ten>{RESET}       Doi ten tac gia
  {GRAY}  config prefix <ky tu>{RESET}     Doi prefix
  {GRAY}  config token <token>{RESET}      Doi token
  {GRAY}  config auto_gif <true/false>{RESET}  Bat/tat auto GIF

  {YELLOW}[ TUY CHINH MENU ]{RESET}
  {GRAY}  menu set title <text>{RESET}     Doi title menu chinh
  {GRAY}  menu set desc <text>{RESET}      Doi mo ta menu
  {GRAY}  menu set footer <text>{RESET}    Doi footer menu
  {GRAY}  menu set color <hex>{RESET}      Doi mau menu chinh
  {GRAY}  menu section <sec> <key> <val>{RESET}  Sua section
  {GRAY}  menu list{RESET}                 Xem cac section

  {YELLOW}[ TEN LENH ]{RESET}
  {GRAY}  alias <lenh> <ten_moi>{RESET}    Doi ten lenh
  {GRAY}  alias del <lenh>{RESET}          Xoa ten lenh
  {GRAY}  alias list{RESET}                Xem tat ca ten lenh

  {YELLOW}[ GIF TU DONG ]{RESET}
  {GRAY}  gif_add <category> <url>{RESET}  Them GIF
  {GRAY}  gif_del <category>{RESET}        Xoa GIF
  {GRAY}  gif_list{RESET}                  Danh sach GIF

  {YELLOW}[ STATUS CYCLE ]{RESET}
  {GRAY}  status_add <text>{RESET}         Them status
  {GRAY}  status_del <so>{RESET}           Xoa status
  {GRAY}  status_list{RESET}               Danh sach status

  {YELLOW}[ DAT LAI MAC DINH ]{RESET}
  {GRAY}  reset all{RESET}                 Dat lai tat ca
  {GRAY}  reset menu{RESET}                Dat lai menu
  {GRAY}  reset gif{RESET}                 Dat lai GIF
  {GRAY}  reset alias{RESET}               Xoa tat ca alias

  {YELLOW}[ TIEN ICH ]{RESET}
  {GRAY}  help{RESET}                      Hien thi menu nay
  {GRAY}  clear{RESET}                     Xoa man hinh
  {GRAY}  exit{RESET}                      Thoat console

  {YELLOW}[ PHIM TAT ]{RESET}
  {GRAY}  s{RESET} = start | {GRAY}p{RESET} = stop | {GRAY}r{RESET} = restart | {GRAY}q{RESET} = exit
  {CYAN}{'=' * 60}{RESET}
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
                elif cmd == "menu":
                    if not args:
                        self.show_config()
                    elif args[0] == "set" and len(args) >= 3:
                        self.set_menu(args[1], " ".join(args[2:]))
                    elif args[0] == "section" and len(args) >= 4:
                        self.set_section(args[1], args[2], " ".join(args[3:]))
                    elif args[0] == "list":
                        self.list_sections()
                    else:
                        self.log("Dung: menu set <key> <value> | menu section <sec> <key> <val> | menu list", YELLOW)
                elif cmd == "alias":
                    if not args:
                        self.list_aliases()
                    elif args[0] == "del" and len(args) >= 2:
                        self.remove_alias(args[1])
                    elif args[0] == "list":
                        self.list_aliases()
                    elif len(args) >= 2:
                        self.set_alias(args[0], args[1])
                    else:
                        self.log("Dung: alias <lenh> <ten_moi> | alias del <lenh> | alias list", YELLOW)
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
                        self.log("Dung: status_del <so>", YELLOW)
                elif cmd == "status_list":
                    self.list_status()
                elif cmd == "reset":
                    if not args or args[0] == "all":
                        self.reset_all()
                    elif args[0] == "menu":
                        self.reset_menu()
                    elif args[0] == "gif":
                        self.reset_gifs()
                    elif args[0] == "alias":
                        self.reset_aliases()
                    else:
                        self.log("Dung: reset all | reset menu | reset gif | reset alias", YELLOW)
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
                self.log("Nhan Ctrl+C de thoat. Go exit.", YELLOW)
            except EOFError:
                break
            except Exception as e:
                self.log(f"Loi: {e}", RED)


if __name__ == "__main__":
    console = HostBotConsole()
    console.run()
