# HostBot v6.2

**Discord Self-Bot voi Console Manager & Customization**
Tac gia: **QU4N.TH3.D3V**

---

## Tinh nang

| Module | Mo ta |
|--------|-------|
| **Console** | CLI quan ly bot: start, stop, restart, kill, config, help |
| **War** | Spam, raid, nuke, mass delete/create channels |
| **Music** | YouTube, queue, volume, loop, nhac co san |
| **Entertainment** | 8ball, rps, trivia, coinflip, guess number |
| **Economy** | Daily, bal, pay, shop, inventory |
| **Utility** | Ping, avatar, banner, server/user info, copy emoji |
| **Admin** | Kick, ban, unban, create/delete channels, rename server |
| **Troll** | Fake message, dice, voice spam, mind games |
| **Auto GIF** | Tu dong gui GIF sau moi lenh |
| **Status Cycle** | Tu dong chuyen doi trang thai |
| **Customization** | Doi ten bot, author, prefix, GIF ma khong can code |

---

## Cai dat

### Yeu cau

- Python 3.10 tro len
- pip
- ffmpeg (cho tinh nang nhac)

### Cach 1: Double-click (De nhat)

1. Tai zip hoac clone repo
2. Double-click `HostBot.bat`
3. Nhap Discord Token khi duoc hoi
4. Xong — bot tu cai dependencies va chay

### Cach 2: Cmd / Terminal

```bash
git clone https://github.com/nguyenminhquan2012ct-oss/jjkvvnk.git
cd jjkvvnk
pip install -r requirements.txt
python console.py
```

### Cach 3: Tai zip

1. Vao https://github.com/nguyenminhquan2012ct-oss/jjkvvnk
2. Nhan Code > Download ZIP
3. Giai nen
4. Chay `HostBot.bat` hoac `python console.py`

---

## Console Manager

Sau khi chay `python console.py`, ban se thay console nhu hinh:

```
                  QU4N.TH3.D3V
    ██╗   ██╗██╗   ██╗███╗   ██╗██╗  ██╗
    ██║   ██║██║   ██║████╗  ██║██║ ██╔╝
    ...
    v6.2.0 | Console Manager
==================================================
  [HH:MM:SS] Console san sang. Go help de xem huong dan.

HostBot >
```

### Lenh Console

| Lenh | Alias | Mo ta |
|------|-------|-------|
| `start` | `s` | Khoi dong bot |
| `stop` | `p` | Dung bot |
| `restart` | `r` | Restart bot |
| `kill` | | Force kill bot |
| `status` | | Xem trang thai bot |
| `config` | `set` | Xem/tat ca cau hinh |
| `help` | | Hien thi menu lenh |
| `clear` | | Xoa man hinh |
| `exit` | `q` | Thoat console |

### Vi du su dung

```
HostBot > start
  [HH:MM:SS] Dang khoi dong HostBot...
  [HH:MM:SS] HostBot da duoc khoi dong!

HostBot > config bot_name SukunaBot
  [HH:MM:SS] Bot name: SukunaBot

HostBot > config prefix !
  [HH:MM:SS] Prefix: !

HostBot > gif_add raid https://media.tenor.com/sukuna.gif
  [HH:MM:SS] GIF 'raid' da duoc them.

HostBot > stop
  [HH:MM:SS] Dang dung HostBot...
  [HH:MM:SS] HostBot da dung.

HostBot > exit
  [HH:MM:SS] Tam biet!
```

---

## Cai dat Customization

### File settings.json

File `settings.json` luu tat ca cai dat ca nhan hoa:

```json
{
    "bot_name": "HostBot",
    "author": "QU4N.TH3.D3V",
    "auto_gif": true,
    "gif_responses": {
        "raid": "https://media.tenor.com/sukuna.gif",
        "spam": "https://media.tenor.com/sukuna.gif",
        "nuke": "https://media.tenor.com/sukuna.gif",
        "music": "https://media.tenor.com/music.gif",
        "fun": "https://media.tenor.com/fun.gif",
        "troll": "https://media.tenor.com/troll.gif",
        "admin": "https://media.tenor.com/admin.gif"
    },
    "status_cycle": [
        ".menu de mo Menu",
        "HostBot v6.2",
        "Dung .help de tro giup"
    ]
}
```

### Doi ten bot

**Cach 1: Qua Console**
```
HostBot > config bot_name TenMoi
```

**Cach 2: Sua settings.json**
```json
"bot_name": "TenMoi"
```

### Doi ten tac gia

```
HostBot > config author TenTacGiaMoi
```

### Doi prefix

```
HostBot > config prefix !
```

### Them/Xoa GIF tu dong

Sau moi lenh, bot se tu dong gui 1 URL GIF. Ban co the tuy chinh:

```
HostBot > gif_add raid https://media.tenor.com/sukuna.gif
HostBot > gif_add music https://media.tenor.com/music.gif
HostBot > gif_add fun https://media.tenor.com/fun.gif
HostBot > gif_del raid
HostBot > gif_list
```

**Cac category GIF:**

| Category | Lenh tuong ung |
|----------|---------------|
| `spam` | .vohahan, .thuong, .lienke, .hacmon |
| `nuke` | .khaitram, .huydiet, .diet |
| `raid` | .ngucmon, .loanvuc, .anpham |
| `music` | .play, .nhac, .play-sa/sh/amk/sp |
| `fun` | .8ball, .rps, .trivia, .coinflip, .fact, .quote, .meme |
| `troll` | .batdiet, .xucxac, .amhon, .fake, .vonghon |
| `admin` | .tram, .phong, .giai, .tao, .danh |

### Bat/Tat Auto GIF

```
HostBot > config auto_gif false   # Tat
HostBot > config auto_gif true    # Bat
```

### Status Cycle (Tu dong chuyen doi trang thai)

```
HostBot > status_add "Dang hoat dong..."
HostBot > status_add ".help de tro giup"
HostBot > status_del 2
HostBot > status_list
```

### File config.json

```json
{
    "token": "DISCORD_TOKEN_CUA_BAN",
    "prefix": "."
}
```

### Bien moi truong (uu tile cao hon config.json)

| Bien | Mo ta |
|------|-------|
| `BOT_TOKEN` | Token Discord (uu tile nhat) |
| `DISCORD_TOKEN` | Token Discord (fallback) |
| `DISCORD_BOT_TOKEN` | Token Discord (fallback) |

### Lay Token

1. Vao https://discord.com/developers/applications
2. Tao Application > Bot > Copy Token
3. Dan vao `config.json` hoac bien moi truong

---

## Danh sach lenh Bot

Prefix mac dinh: `. (co the doi trong config.json hoac console)

### Menu

| Lenh | Mo ta |
|-------|-------|
| `.menu` | Menu chinh |
| `.lanhdia` | Menu chinh (ANSI) |
| `.info` | Thong tin bot |
| `.ngung` | Dung tat ca thuat thuc dang chay |

---

### War

| Lenh | Tham so | Mo ta |
|-------|---------|-------|
| `.raid` | | Menu war |
| `.vohahan` | `[delay] [text]` | Spam tuy chinh (delay=0 = max speed) |
| `.thuong` | `[delay]` | Spam noi dung tu `ngon.txt` |
| `.lienke` | `[delay] [@user]` | Spam noi dung tu `nhay.txt` |
| `.hacmon` | `[url] [delay] [text]` | Spam qua Webhook |
| `.ngucmon` | `[voice_id]` | Treo trong Voice Channel |
| `.loanvuc` | `[voice_id] [delay]` | Spam join/leave Voice |
| `.anpham` | `[so] [emoji]` | Tha reaction hang loat |
| `.khaitram` | | Xoa toan bo kenh |
| `.huydiet` | `[webhook_url] [delay]` | Nuke server |

**Vi du:**
```
.vohahan 0 Xin chao moi nguoi
.thuong 0
.lienke 0 @someone
.hacmon https://discord.com/api/webhooks/xxx 0 Spammed!
.ngucmon 123456789
.khaitram
```

---

### Music

| Lenh | Tham so | Mo ta |
|-------|---------|-------|
| `.nhac` | | Menu nhac |
| `.play` | `[link/ten]` | Phat nhac tu YouTube |
| `.play-sa` | | Phat "Stay Alive" |
| `.play-sh` | | Phat "Styx Helix" |
| `.play-amk` | | Phat "Akuma no Ko" |
| `.play-sp` | | Phat "Specialz" |
| `.queue` | | Xem danh sach cho |
| `.skip` | | Bo qua bai hien tai |
| `.stop` | | Dung nhac + roi voice |
| `.now` | | Bai dang phat |
| `.loop` | | Bat/tat lap bai |
| `.volume` | `[1-100]` | Dieu chinh am luong |
| `.pause` | | Tam dung |
| `.resume` | | Tiep tuc |

**Yeu cau:** FFmpeg phai duoc cai tren he thong.

**Nhac co san (dat trong thu muc `music/`):**
- `stay_alive.mp3`
- `styx_helix.mp3`
- `akuma_no_ko.mp3`
- `specialz.mp3`

---

### Entertainment

| Lenh | Tham so | Mo ta |
|-------|---------|-------|
| `.traloi` | | Menu giai tri |
| `.8ball` | `[cau hoi]` | Phep boi 8 bong |
| `.rps` | `[rock/paper/scissors]` | Keo bua bao |
| `.trivia` | | Cau do vui |
| `.coinflip` | | Toss dong xu |
| `.number` | `[1-100]` | Doan so bi an |

---

### Economy

| Lenh | Tham so | Mo ta |
|-------|---------|-------|
| `.daily` | | Nhan 100-500 vang/ngay |
| `.bal` | `[@user]` | Xem so du |
| `.pay` | `[@user] [so]` | Chuyen tien |
| `.shop` | | Xem cua hang |
| `.buy` | `[ten item]` | Mua vat pham |
| `.inventory` | `[@user]` | Xem vat pham |

**Items trong shop:**
- `bam_ngo` — Banh Ngo Random Box (500)
- `chuc_luc` — Chu Luc Tui +10 (1000)
- `hoa_dieu` — Hoa Giai Da Reset (2000)
- `nguyen_lieu` — Nguyen Lieu SSR (5000)

---

### Utility

| Lenh | Tham so | Mo ta |
|-------|---------|-------|
| `.chucu` | | Menu tien ich |
| `.thauthi` | `[token]` | Kiem tra token |
| `.thanhduyet` | `[so]` | Xoa tin nhan ban than |
| `.giapan` | | Dong tat ca DM |
| `.nguonluc` | | Check ping & he thong |
| `.truytung` | `[@user]` | Soi avatar |
| `.phian` | `[@user]` | Soi banner |
| `.sao-an` | `[server_id]` | Copy toan bo cau truc kenh |
| `.danhdinh` | `[@user]` | Thong tin nguoi dung |
| `.ketgioi` | | Thong tin server |
| `.dongan` | `[emoji]` | Copy emoji ve server |

---

### Admin

| Lenh | Tham so | Mo ta |
|-------|---------|-------|
| `.quanly` | | Menu quan ly |
| `.tram` | `[user]` | Kick thanh vien |
| `.phong` | `[user]` | Ban thanh vien |
| `.giai` | `[user_id]` | Unban thanh vien |
| `.diet` | | Xoa toan bo kenh |
| `.tao` | `[ten]` | Tao 15 kenh moi |
| `.danh` | `[ten moi]` | Doi ten server |

---

### Troll

| Lenh | Tham so | Mo ta |
|-------|---------|-------|
| `.troll` | | Menu troll |
| `.batdiet` | | Random outcome |
| `.xucxac` | | Tung xuc xac 1-6 |
| `.amhon` | `[channel_id] [file]` | Phat nhac vao Voice |
| `.truhon` | | Roi Voice |
| `.fake` | `[@user] [text]` | Gia mao tin nhan |
| `.donguyen` | | Doan chu luc |
| `.vonghon` | | Nhai lai tin nhan |
| `.nguyenrua` | `[@user]` | Am que doi phuong |
| `.batkhuat` | | Tu phan hoi khi bi tag |

---

## Hosting 24/7

### Wispbyte (Free)

**Buoc 1:** Push code len GitHub

**Buoc 2:** Clone tren Wispbyte panel

**Buoc 3:** Startup Command:
```
if [[ -d .git ]] && [[ "0" == "1" ]]; then git pull; fi;
if [[ ! -z "aiohttp" ]]; then pip install -U --prefix .local aiohttp; fi;
if [[ -f /home/container/${REQUIREMENTS_FILE} ]]; then
  pip install -U --prefix .local -r ${REQUIREMENTS_FILE};
fi;
/usr/local/bin/python /home/container/main.py
```

**Buoc 4:** Env var: `BOT_TOKEN` = Token Discord

**Buoc 5"> Nhan Start

### Luu y hosting

- Xoa `.git/`, `__pycache__/`, `.zip` de tieu thu dung luong
- Python version: 3.11 hoac 3.12
- Them `apt install -y ffmpeg` vao startup neu dung nhac

---

## Cau truc file

```
HostBot/
├── console.py           ← Console manager (entry point)
├── main.py              ← Bot logic, loads cogs
├── settings.json        ← Cai dat ca nhan hoa (bot name, GIF, status)
├── config.json          ← Token & prefix
├── rate_utils.py        ← Xu ly rate limit Discord API
├── cache.py             ← TTL cache (user/guild/channel/role)
├── ui.py                ← Embed helpers, colors, progress bar
├── entertainment.py     ← Games, economy, fun commands
├── music.py             ← YouTube playback, queue, built-in songs
├── raid.py              ← War/spam/raid commands
├── tienich.py           ← Utility commands
├── quanly.py            ← Admin commands
├── troll.py             ← Troll/mini-game commands
├── lanhdia.py           ← Menu & bot info
├── requirements.txt     ← Python dependencies
├── ngon.txt             ← Data cho lenh .thuong
├── nhay.txt             ← Data cho lenh .lienke
├── HostBot.bat          ← Launcher (double-click)
├── .gitignore           ← Bao ve secrets
├── LICENSE              ← MIT License
├── README.md            ← Tai lieu nay
└── music/               ← Thu muc nhac co san
    ├── stay_alive.mp3
    ├── styx_helix.mp3
    ├── akuma_no_ko.mp3
    └── specialz.mp3
```

---

## Yeu cau he thong

| Thanh phan | Yeu cau |
|------------|----------|
| Python | 3.10+ |
| pip | Co san voi Python |
| ffmpeg | Cho tinh nang nhac (khong bat buoc) |
| Disk | ~50MB |
| RAM | ~100MB |

---

## Troubleshooting

### Bot khong chay

1. Kiem tra `config.json` co token dung chua
2. Chay `python main.py` truc tiep de xem loi

### Loi `ModuleNotFoundError`

```
pip install -r requirements.txt
```

### Loi `No module named 'discord'`

```
pip install discord.py-self
```

### Loi rate limit (429)

Bot tu xu ly 429 va retry ngay lap tuc. Neu muon delay giua cac tin nhan:
```
.vohahan 2.0 text
```

### Loi voice / music

- Can cai ffmpeg
- Windows: tai ffmpeg.exe, dat trong thu muc `ffmpeg/`
- Linux: `apt install ffmpeg`
- Mac: `brew install ffmpeg`

### Khong join voice duoc

- Kiem tra bot co quyen `Connect` trong voice channel
- Kiem tra voice ID dung

### Token die / Khong login duoc

- Token co the bi reset khi doi password
- Vao Developer Portal > Bot > Reset Token
- Cap nhat lai `config.json`

---

## Luu y quan trong

- **Self-bot vi pham ToS Discord** — dung alt account, chap nhan rui ro
- **Khong spam qua de** — de bi flag va ban account
- **Token la bi mat** — khong share, khong commit len GitHub
- **Backup config** — luu token o noi an toan
- **Whitelist** — them ID server vao `PROTECTED_GUILD_IDS` trong `rate_utils.py` de bao ve
- **Max Speed** — delay = 0 o moi lenh, Discord se tu impose rate limit nhung bot retry ngay
- **Customization** — dung console hoac settings.json de cau hinh, khong can viet code

---

*HostBot v6.2 — Made by QU4N.TH3.D3V*
