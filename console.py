import os
import sys
import signal
import subprocess
import threading
import time
from datetime import datetime

CONFIG_FILE = "config.json"
PYTHON = sys.executable

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
GRAY = "\033[1;30m"
PINK = "\033[1;95m"
RESET = "\033[0m"


def ts():
    return datetime.now().strftime("%H:%M:%S")


class HostBotConsole:
    def __init__(self):
        self.process = None
        self.version = "6.4.0"

    def banner(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""
{YELLOW}                  QU4N.TH3.D3V{RESET}

{CYAN}    ██╗   ██╗██╗   ██╗███╗   ██╗██╗  ██╗
{CYAN}    ██║   ██║██║   ██║████╗  ██║██║ ██╔╝
{CYAN}    ██║   ██║██║   ██║██╔██╗ ██║█████╔╝
{CYAN}    ╚██╗ ██╔╝╚██╗ ██╔╝██║╚██╗██║██╔═██╗
{CYAN}     ╚████╔╝  ╚████╔╝ ██║ ╚████║██║  ██╗
{CYAN}      ╚═══╝    ╚═══╝  ╚═╝  ╚═══╝╚═╝  ╚═╝{RESET}
{GRAY}    v{self.version}{RESET}
{GRAY}    {'=' * 50}{RESET}""")

    def log(self, msg, color=WHITE):
        print(f"  {GRAY}[{ts()}]{RESET} {color}{msg}{RESET}")

    def start_bot(self):
        if self.process and self.process.poll() is None:
            self.log("Bot dang chay roi! Dung stop truoc.", YELLOW)
            return

        if not os.path.exists(CONFIG_FILE):
            self.log("Thieu config.json! Chay HostBot.bat de tao.", RED)
            return

        self.log("Dang khoi dong bot...", CYAN)
        try:
            self.process = subprocess.Popen(
                [PYTHON, "main.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
            )
            threading.Thread(target=self._output, daemon=True).start()
            self.log("Bot da khoi dong!", GREEN)
        except Exception as e:
            self.log(f"Loi: {e}", RED)

    def _output(self):
        try:
            for line in self.process.stdout:
                print(f"  {GRAY}[BOT]{RESET} {line.rstrip()}")
        except Exception:
            pass
        finally:
            if self.process and self.process.poll() is not None:
                self.log("Bot da dung.", YELLOW)
                self.process = None

    def stop_bot(self):
        if not self.process or self.process.poll() is not None:
            self.log("Bot chua chay.", YELLOW)
            return
        self.log("Dang dung bot...", YELLOW)
        try:
            self.process.terminate()
            self.process.wait(timeout=10)
            self.log("Bot da dung.", GREEN)
        except subprocess.TimeoutExpired:
            self.process.kill()
            self.log("Bot bi kill.", RED)
        except Exception as e:
            self.log(f"Loi: {e}", RED)
        finally:
            self.process = None

    def restart_bot(self):
        self.log("Restarting...", CYAN)
        self.stop_bot()
        time.sleep(1)
        self.start_bot()

    def kill_bot(self):
        if not self.process or self.process.poll() is not None:
            self.log("Bot chua chay.", YELLOW)
            return
        try:
            self.process.kill()
        except Exception:
            pass
        self.process = None
        self.log("Bot bi kill.", RED)

    def show_status(self):
        if self.process and self.process.poll() is None:
            self.log(f"Bot: {GREEN}DANG CHAY{RESET} (PID: {self.process.pid})", GREEN)
        else:
            self.log(f"Bot: {RED}DA DUNG{RESET}", RED)

    def show_help(self):
        print(f"""
{CYAN}{'=' * 55}
{WHITE} HOSTBOT CONSOLE - v{self.version}
{CYAN}{'=' * 55}{RESET}

{YELLOW}[ Dieu khien bot ]{RESET}
  {WHITE}start{RESET}       Khoi dong bot
  {WHITE}stop{RESET}        Dung bot
  {WHITE}restart{RESET}     Restart bot
  {WHITE}kill{RESET}        Force kill bot
  {WHITE}status{RESET}      Xem trang thai

{YELLOW}[ Lenh bot (go trong Discord) ]{RESET}
  {WHITE}.menu{RESET}       Menu chinh
  {WHITE}.info{RESET}       Thong tin bot
  {WHITE}.raid{RESET}       Menu war/spam
  {WHITE}.nhac{RESET}       Menu nhac
  {WHITE}.traloi{RESET}     Menu giai tri
  {WHITE}.chucu{RESET}      Menu tien ich
  {WHITE}.quanly{RESET}     Menu quan ly
  {WHITE}.troll{RESET}      Menu troll
  {WHITE}.ngung{RESET}      Dung tat ca thuat thuc

{YELLOW}[ Lenh war ]{RESET}
  {WHITE}.vohahan{RESET} [delay] [text]     Spam tuy chinh
  {WHITE}.thuong{RESET} [delay]              Spam ngon.txt
  {WHITE}.lienke{RESET} [delay] [@user]      Spam nhay.txt
  {WHITE}.hacmon{RESET} [url] [delay] [text] Webhook spam
  {WHITE}.ngucmon{RESET} [voice_id]          Treo Voice
  {WHITE}.loanvuc{RESET} [voice_id] [delay]  Spam join/leave
  {WHITE}.anpham{RESET} [so] [emoji]         Reaction hang loat
  {WHITE}.khaitram{RESET}                    Xoa toan bo kenh
  {WHITE}.huydiet{RESET}                     Nuke server

{YELLOW}[ Lenh nhac ]{RESET}
  {WHITE}.play{RESET} [link/ten]    Phat nhac YouTube
  {WHITE}.play-sa{RESET}           Stay Alive
  {WHITE}.play-sh{RESET}           Styx Helix
  {WHITE}.play-amk{RESET}          Akuma no Ko
  {WHITE}.play-sp{RESET}           Specialz
  {WHITE}.queue{RESET}             Hang cho
  {WHITE}.skip{RESET}              Bo qua bai
  {WHITE}.stop{RESET}              Dung nhac
  {WHITE}.now{RESET}               Bai dang phat
  {WHITE}.loop{RESET}              Lap bai
  {WHITE}.volume{RESET} [1-100]    Am luong
  {WHITE}.pause{RESET} / {WHITE}.resume{RESET}  Tam dung / Tiep tuc

{YELLOW}[ Lenh giai tri ]{RESET}
  {WHITE}.8ball{RESET} [cau hoi]      Boi 8 bong
  {WHITE}.rps{RESET} [rock/paper/scissors]  Keo bua bao
  {WHITE}.trivia{RESET}              Cau do vui
  {WHITE}.coinflip{RESET}            Dong xu
  {WHITE}.number{RESET} [1-100]      Doan so
  {WHITE}.daily{RESET}               Nhan vang
  {WHITE}.bal{RESET}                 So du
  {WHITE}.shop{RESET}                Cua hang
  {WHITE}.avatar{RESET} [@user]      Avatar
  {WHITE}.banner{RESET} [@user]      Banner
  {WHITE}.fact{RESET} / {WHITE}.quote{RESET} / {WHITE}.meme{RESET}   Fun

{YELLOW}[ Lenh tien ich ]{RESET}
  {WHITE}.thauthi{RESET} [token]     Kiem tra token
  {WHITE}.thanhduyet{RESET} [so]     Xoa tin nhan
  {WHITE}.nguonluc{RESET}            Check ping
  {WHITE}.truytung{RESET} [@user]    Soi avatar
  {WHITE}.danhdinh{RESET} [@user]    Info nguoi dung
  {WHITE}.ketgioi{RESET}             Info server

{YELLOW}[ Lenh quan ly ]{RESET}
  {WHITE}.tram{RESET} [user]         Kick
  {WHITE}.phong{RESET} [user]        Ban
  {WHITE}.giai{RESET} [user_id]      Unban
  {WHITE}.diet{RESET}                Xoa kenh
  {WHITE}.tao{RESET} [ten]           Tao kenh
  {WHITE}.danh{RESET} [ten]          Doi ten server

{YELLOW}[ Phim tat ]{RESET}
  {WHITE}s{RESET} = start | {WHITE}p{RESET} = stop | {WHITE}r{RESET} = restart | {WHITE}q{RESET} = exit
{CYAN}{'=' * 55}{RESET}
""")

    def run(self):
        self.banner()
        self.log("Go {WHITE}help{RESET} de xem lenh.".replace("{WHITE}", WHITE).replace("{RESET}", RESET), GREEN)
        print()

        while True:
            try:
                raw = input(f"  {PINK}HostBot>{RESET} ").strip()
                if not raw:
                    continue
                cmd = raw.lower()

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
                elif cmd == "help":
                    self.show_help()
                elif cmd == "clear":
                    self.banner()
                elif cmd in ("exit", "quit", "q"):
                    if self.process and self.process.poll() is None:
                        self.stop_bot()
                    print(f"  {GRAY}Tam biet!{RESET}")
                    sys.exit(0)
                else:
                    self.log(f"Khong hieu: {cmd}. Go {YELLOW}help{RESET}.", RED)

            except KeyboardInterrupt:
                print()
            except EOFError:
                break
            except Exception as e:
                self.log(f"Loi: {e}", RED)


if __name__ == "__main__":
    HostBotConsole().run()
