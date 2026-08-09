# HostBot v6.4

**Discord Self-Bot** - Dieu khien tai khoan Discord ca nhan voi nhieu tinh nang.

> ⚠️ Self-bot vi pham Discord ToS. Su dung tai khoan alt. Chu nhan chap nhan moi rui ro.

---

## Cai dat

### Yeu cau
- **Python 3.10+** (test voi Python 3.14)
- **Windows** (hoac Linux/macOS voi dieu chinh nho)

### Buoc 1: Tai source code
```bash
git clone https://github.com/nguyenminhquan2012ct-oss/jjkvvnk.git
cd jjkvvnk
```

### Buoc 2: Chay Run.bat
- Double-click **`Run.bat`**
- Lan dau se hoi **Discord Token** → nhap vao
- Thu vien se tu dong cai dat
- Bot tu dong khoi dong va **tu restart neu crash**

### Hoac chay thu cong
```bash
python -m pip install -r requirements.txt
python main.py
```

---

## Cau hinh

File `config.json` (tu dong tao boi Run.bat):
```json
{
    "token": "DISCORD_TOKEN_CUA_BAN",
    "prefix": "."
}
```

File `settings.json` (tuy chinh bot):
```json
{
    "bot_name": "HostBot",
    "author": "QU4N.TH3.D3V",
    "auto_gif": true,
    "status_cycle": ["JJK-VVNK", "Playing...", "HostBot v6.4"]
}
```

---

## Danh sach lenh

### Menu chinh
| Lenh | Mo ta |
|------|-------|
| `.menu` | Hien thi menu chinh |
| `.info` | Thong tin bot va server |
| `.ngung` | Dung tat ca thuat thuc dang chay |

### War / Spam
| Lenh | Mo ta |
|------|-------|
| `.raid` | Menu war/spam |
| `.vohahan [delay] [text]` | Spam tuy chinh |
| `.thuong [delay]` | Spam noi dung tu `ngon.txt` |
| `.lienke [delay] [@user]` | Spam noi dung tu `nhay.txt` |
| `.hacmon [url] [delay] [text]` | Spam qua Webhook |
| `.ngucmon [voice_id]` | Treo Voice Channel |
| `.loanvuc [voice_id] [delay]` | Spam join/leave Voice |
| `.anpham [so] [emoji]` | Reaction hang loat |
| `.khaitram` | Xoa toan bo kenh |
| `.huydiet` | Nuke server |

### Nhac
| Lenh | Mo ta |
|------|-------|
| `.nhac` | Menu nhac |
| `.play [link/ten]` | Phat nhac tu YouTube |
| `.play-sa` | Phat "Stay Alive" |
| `.play-sh` | Phat "Styx Helix" |
| `.play-amk` | Phat "Akuma no Ko" |
| `.play-sp` | Phat "Specialz" |
| `.queue` | Xem hang cho |
| `.skip` | Bo qua bai hien tai |
| `.stop` | Dung nhac + roi voice |
| `.now` | Bai dang phat |
| `.loop` | Bat/tat lap bai |
| `.volume [1-100]` | Dieu chinh am luong |
| `.pause` / `.resume` | Tam dung / Tiep tuc |

### Giai tri
| Lenh | Mo ta |
|------|-------|
| `.traloi` | Menu giai tri |
| `.8ball [cau hoi]` | Boi 8 bong |
| `.rps [rock/paper/scissors]` | Keo bua bao |
| `.trivia` | Cau do vui |
| `.coinflip` | Dong xu |
| `.number [1-100]` | Doan so |
| `.daily` | Nhan vang hang ngay |
| `.bal` | Xem so du |
| `.shop` | Cua hang |
| `.avatar [@user]` | Xem avatar |
| `.banner [@user]` | Xem banner |
| `.fact` / `.quote` / `.meme` | Fun |

### Tien ich
| Lenh | Mo ta |
|------|-------|
| `.chucu` | Menu tien ich |
| `.thauthi [token]` | Kiem tra token |
| `.thanhduyet [so]` | Xoa tin nhan ban than |
| `.nguonluc` | Check ping |
| `.truytung [@user]` | Soi avatar |
| `.danhdinh [@user]` | Thong tin nguoi dung |
| `.ketgioi` | Thong tin server |

### Quan ly
| Lenh | Mo ta |
|------|-------|
| `.quanly` | Menu quan ly |
| `.tram [user]` | Kick |
| `.phong [user]` | Ban |
| `.giai [user_id]` | Unban |
| `.diet` | Xoa kenh |
| `.tao [ten]` | Tao kenh |
| `.danh [ten]` | Doi ten server |

### Troll
| Lenh | Mo ta |
|------|-------|
| `.troll` | Menu troll |
| `.batdiet` | Game nhan pham |
| `.xucxac` | Xuc xac |
| `.amhon [id] [file]` | Phat nhac vao Voice |
| `.truhon` | Roi Voice |
| `.fake [@user] [text]` | Gia mao tin nhan |
| `.donguyen` | Do suc manh |
| `.vonghon` | Nhai lai tin nhan |
| `.nguyenrua [@user]` | Am que doi phuong |
| `.batkhuat` | Tu phan hoi khi bi tag |

---

## Cau truc thu muc

```
JJK-VVNK/
├── main.py              # Entry point
├── Run.bat              # Launcher (auto-install + auto-restart)
├── config.json          # Token (gitignored)
├── settings.json        # Cau hinh bot
├── requirements.txt     # Thu vien can thiet
├── .gitignore           # Git ignore
│
├── ui.py                # Menu commands
├── entertainment.py     # Fun/economy commands
├── music.py             # Music commands
├── raid.py              # War/spam commands
├── tienich.py           # Utility commands
├── quanly.py            # Admin commands
├── troll.py             # Troll commands
├── lanhdia.py           # Info commands
│
├── rate_utils.py        # Rate limit handling
├── cache.py             # Cache utilities
│
├── ngon.txt             # Noi dung spam (.thuong)
├── nhay.txt             # Noi dung spam (.lienke)
├── music/               # File nhac co san
│   ├── stay_alive.mp3
│   ├── styx_helix.mp3
│   ├── akuma_no_ko.mp3
│   └── specialz.mp3
└── music_cache/         # Cache nhac tu YouTube (gitignored)
```

---

## Fix loi thuong gap

**Bot khong phan hoi lenh:**
- Kiem tra `config.json` co token dung khong
- Kiem tra bot co quyen gui tin nhan trong channel khong
- Go `.ngung` de dung tat ca, thu lai

**Loi khi play nhac:**
- Can **FFmpeg** installed. Tai: https://ffmpeg.org/download.html
- Dat `ffmpeg.exe` vao thu muc `ffmpeg/` hoac them vao PATH

**Bot bi rate limit:**
- Bot co he xu ly rate limit tu dong
- Neu bi khoa, doi vai phut roi thu lai

---

## Tac gia

**QU4N.TH3.D3V** - JJK-VVNK Bot v6.4
