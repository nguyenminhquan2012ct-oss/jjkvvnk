# 🏮 JJK-VVNK BOT v6.0

**Self-Bot Discord theo phong cách Jujutsu Kaisen**
Tác giả: **QU4N.TH3.D3V**

---

## 📋 Mục lục

- [Tính năng](#tính-năng)
- [Cài đặt](#cài-đặt)
- [Cách dùng](#cách-dùng)
- [Danh sách lệnh](#danh-sách-lệnh)
- [Hosting (Wispbyte)](#hosting)
- [Troubleshooting](#troubleshooting)

---

## ⚡ Tính năng

| Module | Mô tả |
|--------|-------|
| **⚔️ War** | Spam, raid, nuke, mass delete/create |
| **🎵 Music** | YouTube, queue, volume, nhạc có sẵn |
| **🎮 Entertainment** | 8ball, rps, trivia, economy, daily |
| **🛠️ Utility** | Ping, avatar, banner, server info |
| **🛡️ Admin** | Kick, ban, unban, create/delete channels |
| **🃏 Troll** | Fake message, dice, mind games |
| **📊 UI** | Embed menu, progress bar, pagination |

---

## 📥 Cài đặt

### Cách 1: 1-Click (PowerShell)

```powershell
irm https://raw.githubusercontent.com/nguyenminhquan2012ct-oss/jjkvvnk/main/setup.ps1 | iex
```

Tự động: clone repo → cài dependencies → cấu hình token → chạy bot.

### Cách 2: Tải thủ công

1. Tải zip từ GitHub: https://github.com/nguyenminhquan2012ct-oss/jjkvvnk
2. Giải nén
3. Cài dependencies:
```bash
pip install -r requirements.txt
```

### Cách 3: Clone

```bash
git clone https://github.com/nguyenminhquan2012ct-oss/jjkvvnk.git
cd jjkvvnk
pip install -r requirements.txt
```

---

## 🚀 Cách dùng

### PowerShell Launcher (Khuyến nghị)

```powershell
powershell -ExecutionPolicy Bypass -File launch.ps1
```

Hoặc双击 file `JJK-VVNK.bat`

### Chạy trực tiếp

**Windows:**
```cmd
set BOT_TOKEN=token_cua_ban
python main.py
```

**Linux/Mac:**
```bash
export BOT_TOKEN=token_cua_ban
python main.py
```

### Cấu hình

Tạo file `config.json` (hoặc dùng launcher):
```json
{
    "token": "DISCORD_TOKEN_CUA_BAN",
    "prefix": "."
}
```

Hoặc đặt biến môi trường:
- `BOT_TOKEN` (ưu tiên cao nhất)
- `DISCORD_TOKEN`
- `DISCORD_BOT_TOKEN`

---

## 📖 Danh sách lệnh

### ⚔️ WAR (`raid`)
| Lệnh | Mô tả |
|-------|-------|
| `.raid` | Menu war |
| `.vohahan [delay] [text]` | Spam tùy chỉnh |
| `.thuong [delay]` | Spam file ngon.txt |
| `.lienke [delay]` | Spam file nhay.txt |
| `.hacmon [url] [delay] [text]` | Webhook spam |
| `.ngucmon [voice_id]` | Treo voice |
| `.loanvuc [voice_id] [delay]` | Spam join/leave voice |
| `.anpham [số] [emoji]` | Mass reaction |
| `.khaitram` | Xóa toàn bộ kênh |
| `.huydiet` | Nuke server |
| `.ngung` | Dừng tất cả |

### 🎵 MUSIC (`nhac`)
| Lệnh | Mô tả |
|-------|-------|
| `.nhac` | Menu nhạc |
| `.play [link/tên]` | Phát từ YouTube |
| `.play-sa` | Phát Stay Alive |
| `.play-sh` | Phát Styx Helix |
| `.play-amk` | Phát Akuma no Ko |
| `.play-sp` | Phát Specialz |
| `.queue` | Xem hàng chờ |
| `.skip` | Bỏ qua bài hiện tại |
| `.stop` | Dừng + rời voice |
| `.now` | Bài đang phát |
| `.loop` | Bật/tắt lặp |
| `.volume [1-100]` | Điều chỉnh âm lượng |
| `.pause` | Tạm dừng |
| `.resume` | Tiếp tục |

### 🎮 ENTERTAINMENT (`traloi`)
| Lệnh | Mô tả |
|-------|-------|
| `.traloi` | Menu giải trí |
| `.8ball [câu hỏi]` | Phép bói 8 bóng |
| `.rps [rock/paper/scissors]` | Kéo búa bao |
| `.trivia` | Câu đố vui |
| `.coinflip` | Toss đồng xu |
| `.number [1-100]` | Đoán số |
| `.daily` | Nhận quà hàng ngày |
| `.bal` | Xem số dư |
| `.pay [@user] [số]` | Chuyển tiền |
| `.shop` | Cửa hàng |
| `.buy [item]` | Mua vật phẩm |
| `.inventory` | Xem vật phẩm |
| `.fact` | Fact thú vị |
| `.quote` | Trích dẫn JJK |
| `.insult [@user]` | Insult vui |
| `.compliment [@user]` | Khen ngợi |
| `.avatar [@user]` | Xem avatar |
| `.banner [@user]` | Xem banner |

### 🛠️ UTILITY (`chucu`)
| Lệnh | Mô tả |
|-------|-------|
| `.chucu` | Menu tiện ích |
| `.thauthi [token]` | Kiểm tra token |
| `.thanhduyet [số]` | Xóa tin nhắn bản thân |
| `.giapan` | Đóng DM |
| `.nguonluc` | Check ping |
| `.truytung [@user]` | Soi avatar |
| `.phian [@user]` | Soi banner |
| `.sao-an [server_id]` | Copy cấu trúc kênh |
| `.danhdinh [@user]` | Info người dùng |
| `.ketgioi` | Info server |
| `.dongan [emoji]` | Copy emoji |

### 🛡️ ADMIN (`quanly`)
| Lệnh | Mô tả |
|-------|-------|
| `.quanly` | Menu quản lý |
| `.tram [user]` | Kick |
| `.phong [user]` | Ban |
| `.giai [user_id]` | Unban |
| `.diet` | Xóa toàn bộ kênh |
| `.tao [tên]` | Tạo kênh hàng loạt |
| `.danh [tên]` | Đổi tên server |

### 🃏 TROLL
| Lệnh | Mô tả |
|-------|-------|
| `.troll` | Menu troll |
| `.batdiet` | Random outcome |
| `.xucxac` | Tung xúc xắc |
| `.amhon [channel_id] [file]` | Phát nhạc voice |
| `.truhon` | Rời voice |
| `.fake [@user] [text]` | Giả mạo tin nhắn |
| `.donguyen` | Đoạn chú lực |
| `.nguyenrua [@user]` | Ám quẻ |

### 📊 UI
| Lệnh | Mô tả |
|-------|-------|
| `.menu` | Menu chính (embed) |
| `.warmenu` | Menu war (embed) |
| `.musicmenu` | Menu nhạc (embed) |
| `.funmenu` | Menu giải trí (embed) |
| `.lanhdia` | Menu ANSI |
| `.info` | Thông tin bot |

---

## 🌐 Hosting (Wispbyte)

### Bước 1: Upload

**Cách A — GitHub (khuyến nghị):**
1. Push code lên GitHub
2. Trên Wispbyte panel → Clone từ URL

**Cách B — Upload zip:**
1. Tải `JJK-VVNK-v6.zip`
2. Upload lên Wispbyte FileManager

### Bước 2: Startup Command

```
if [[ -d .git ]] && [[ "0" == "1" ]]; then git pull; fi;
if [[ ! -z "aiohttp" ]]; then pip install -U --prefix .local aiohttp; fi;
if [[ -f /home/container/${REQUIREMENTS_FILE} ]]; then 
  pip install -U --prefix .local -r ${REQUIREMENTS_FILE}; 
fi;
/usr/local/bin/python /home/container/main.py
```

### Bước 3: Environment Variables

| Key | Value |
|-----|-------|
| `BOT_TOKEN` | Token Discord của bạn |

### Bước 4: Khởi động

Nhấn **Start** trên panel. Bot sẽ chạy 24/7.

### ⚠️ Lưu ý hosting

- Free tier rất ít dung lượng — xóa `.git/`, `__pycache__/`, `.zip`
- Python version: 3.11 hoặc 3.12
- Cần `ffmpeg` cho music: thêm `apt install -y ffmpeg` vào startup

---

## 🔧 Troubleshooting

### Bot không chạy
- Kiểm tra token đúng chưa
- Xem log trên console
- Chạy `python main.py` trực tiếp để xem lỗi

### Lỗi `ModuleNotFoundError`
```bash
pip install -r requirements.txt
```

### Lỗi rate limit (429)
Bot tự xử lý rate limit. Nếu bị spam quá, giảm delay:
```
.vohahan 1.0 text
```

### Lỗi voice/music
- Cần cài `ffmpeg`
- Linux: `apt install ffmpeg`
- Windows: tải ffmpeg.exe đặt trong thư mục `ffmpeg/`

### Không join voice được
- Kiểm tra bot có quyền `Connect` trong voice channel
- ID voice phải đúng

---

## 📁 Cấu trúc file

```
JJK-VVNK/
├── main.py              ← Entry point
├── rate_utils.py        ← Xử lý rate limit
├── cache.py             ← Cache system
├── ui.py                ← Embed helpers
├── entertainment.py     ← Games & economy
├── music.py             ← YouTube music
├── raid.py              ← War commands
├── tienich.py           ← Utility commands
├── quanly.py            ← Admin commands
├── troll.py             ← Troll commands
├── lanhdia.py           ← Menu & info
├── requirements.txt     ← Dependencies
├── ngon.txt             ← Data cho .thuong
├── nhay.txt             ← Data cho .lienke
├── launch.ps1           ← PowerShell launcher
├── setup.ps1            ← 1-click installer
├── JJK-VVNK.bat         ← Batch launcher
└── music/               ← Nhạc có sẵn (tạo thủ công)
    ├── stay_alive.mp3
    ├── styx_helix.mp3
    ├── akuma_no_ko.mp3
    └── specialz.mp3
```

---

## ⚠️ Lưu ý quan trọng

- **Self-bot vi phạm ToS Discord** — dùng alt account
- **Không spam quá đà** — dễ bị flag
- **Token bí mật** — không share cho ai
- **Backup config** — lưu token ở nơi an toàn

---

*JJK-VVNK Bot v6.0 — Made by QU4N.TH3.D3V*
