# JJK-VVNK BOT v6.0

**Self-Bot Discord theo phong cách Jujutsu Kaisen**
Tác giả: **QU4N.TH3.D3V**

---

## Tính năng

| Module | Mô tả |
|--------|-------|
| **War** | Spam, raid, nuke, mass delete/create channels |
| **Music** | YouTube, queue, volume, loop, nhạc có sẵn |
| **Entertainment** | 8ball, rps, trivia, coinflip, guess number |
| **Economy** | Daily, bal, pay, shop, inventory |
| **Utility** | Ping, avatar, banner, server/user info, copy emoji |
| **Admin** | Kick, ban, unban, create/delete channels, rename server |
| **Troll** | Fake message, dice, voice spam, mind games |
| **UI** | Embed menus màu sắc, progress bar |

---

## Cài đặt

### Yêu cầu

- Python 3.10 trở lên
- pip
- ffmpeg (cho tính năng nhạc)

### Cách 1: Double-click (Dễ nhất)

1. Tải zip hoặc clone repo
2. Double-click `JJK-VVNK.bat`
3. Nhập Discord Token khi được hỏi
4. Xong — bot tự cài dependencies và chạy

### Cách 2: Cmd / Terminal

```bash
git clone https://github.com/nguyenminhquan2012ct-oss/jjkvvnk.git
cd jjkvvnk
pip install -r requirements.txt
python main.py
```

### Cách 3: Tải zip

1. Vào https://github.com/nguyenminhquan2012ct-oss/jjkvvnk
2. Nhấn Code > Download ZIP
3. Giải nén
4. Chạy `JJK-VVNK.bat` hoặc `python main.py`

---

## Cấu hình

### File config.json

Tạo file `config.json` trong thư mục bot:

```json
{
    "token": "DISCORD_TOKEN_CUA_BAN",
    "prefix": "."
}
```

### Biến môi trường (ưu tiên cao hơn config.json)

| Biên | Mô tả |
|------|-------|
| `BOT_TOKEN` | Token Discord (ưu tiên nhất) |
| `DISCORD_TOKEN` | Token Discord (fallback) |
| `DISCORD_BOT_TOKEN` | Token Discord (fallback) |

### Lấy Token

1. Vào https://discord.com/developers/applications
2. Tạo Application > Bot > Copy Token
3. Dán vào `config.json` hoặc biến môi trường

---

## Cách dùng

### Khởi động

**Windows:**
```
Double-click JJK-VVNK.bat
```

**Cmd:**
```
set BOT_TOKEN=token_cua_ban
python main.py
```

**Linux/Mac:**
```
export BOT_TOKEN=token_cua_ban
python main.py
```

### Dừng bot

Nhấn `Ctrl + C` trong terminal.

---

## Danh sách lệnh

Prefix mặc định: `.` (có thể đổi trong config.json)

### Menu

| Lệnh | Mô tả |
|-------|-------|
| `.menu` | Menu chính (Embed) |
| `.lanhdia` | Menu chính (ANSI) |
| `.info` | Thông tin bot |
| `.ngung` | Dừng tất cả thuật thức đang chạy |

---

### War

| Lệnh | Tham số | Mô tả |
|-------|---------|-------|
| `.raid` | | Menu war |
| `.vohahan` | `[delay] [text]` | Spam tùy chỉnh |
| `.thuong` | `[delay]` | Spam nội dung từ `ngon.txt` |
| `.lienke` | `[delay] [@user]` | Spam nội dung từ `nhay.txt` |
| `.hacmon` | `[url] [delay] [text]` | Spam qua Webhook |
| `.ngucmon` | `[voice_id]` | Treo trong Voice Channel |
| `.loanvuc` | `[voice_id] [delay]` | Spam join/leave Voice |
| `.anpham` | `[số] [emoji]` | Thả reaction hàng loạt |
| `.khaitram` | | Xóa toàn bộ kênh |
| `.huydiet` | `[webhook_url] [delay]` | Nuke server (xóa + tạo kênh mới + spam) |

**Ví dụ:**
```
.vohahan 0.5 Xin chào mọi người
.thuong 0.8
.lienke 1.0 @someone
.hacmon https://discord.com/api/webhooks/xxx 0.5 Spammed!
.ngucmon 123456789
.khaitram
```

---

### Music

| Lệnh | Tham số | Mô tả |
|-------|---------|-------|
| `.nhac` | | Menu nhạc |
| `.play` | `[link/tên]` | Phát nhạc từ YouTube |
| `.play-sa` | | Phát "Stay Alive" |
| `.play-sh` | | Phát "Styx Helix" |
| `.play-amk` | | Phát "Akuma no Ko" |
| `.play-sp` | | Phát "Specialz" |
| `.queue` | | Xem danh sách chờ |
| `.skip` | | Bỏ qua bài hiện tại |
| `.stop` | | Dừng nhạc + rời voice |
| `.now` | | Bài đang phát |
| `.loop` | | Bật/tắt lặp bài |
| `.volume` | `[1-100]` | Điều chỉnh âm lượng |
| `.pause` | | Tạm dừng |
| `.resume` | | Tiếp tục |

**Yêu cầu:** FFmpeg phải được cài trên hệ thống.

**Nhạc có sẵn (đặt trong thư mục `music/`):**
- `stay_alive.mp3`
- `styx_helix.mp3`
- `akuma_no_ko.mp3`
- `specialz.mp3`

---

### Entertainment

| Lệnh | Tham số | Mô tả |
|-------|---------|-------|
| `.traloi` | | Menu giải trí |
| `.8ball` | `[câu hỏi]` | Phép bói 8 bóng |
| `.rps` | `[rock/paper/scissors]` | Kéo búa bao |
| `.trivia` | | Câu đố vui (JJK + kiến thức chung) |
| `.coinflip` | | Toss đồng xu |
| `.number` | `[1-100]` | Đoán số bí ẩn |

---

### Economy

| Lệnh | Tham số | Mô tả |
|-------|---------|-------|
| `.daily` | | Nhận 100-500 vàng/ngày |
| `.bal` | `[@user]` | Xem số dư |
| `.pay` | `[@user] [số]` | Chuyển tiền |
| `.shop` | | Xem cửa hàng |
| `.buy` | `[tên item]` | Mua vật phẩm |
| `.inventory` | `[@user]` | Xem vật phẩm |

**Items trong shop:**
- `bam_ngo` — Bành Ngô Random Box (500)
- `chuc_luc` — Chú Lực Túi +10 (1000)
- `hoa_dieu` — Hóa Giải Đá Reset (2000)
- `nguyen_lieu` — Nguyên Liệu SSR (5000)

---

### Utility

| Lệnh | Tham số | Mô tả |
|-------|---------|-------|
| `.chucu` | | Menu tiện ích |
| `.thauthi` | `[token]` | Kiểm tra token |
| `.thanhduyet` | `[số]` | Xóa tin nhắn bản thân |
| `.giapan` | | Đóng tất cả DM |
| `.nguonluc` | | Check ping & hệ thống |
| `.truytung` | `[@user]` | Soi avatar |
| `.phian` | `[@user]` | Soi banner |
| `.sao-an` | `[server_id]` | Copy toàn bộ cấu trúc kênh |
| `.danhdinh` | `[@user]` | Thông tin người dùng |
| `.ketgioi` | | Thông tin server |
| `.dongan` | `[emoji]` | Copy emoji về server |

---

### Admin

| Lệnh | Tham số | Mô tả |
|-------|---------|-------|
| `.quanly` | | Menu quản lý |
| `.tram` | `[user]` | Kick thành viên |
| `.phong` | `[user]` | Ban thành viên |
| `.giai` | `[user_id]` | Unban thành viên |
| `.diet` | | Xóa toàn bộ kênh |
| `.tao` | `[tên]` | Tạo 15 kênh mới |
| `.danh` | `[tên mới]` | Đổi tên server |

---

### Troll

| Lệnh | Tham số | Mô tả |
|-------|---------|-------|
| `.troll` | | Menu troll |
| `.batdiet` | | Random outcome (Sống sót/Bị thanh tẩy...) |
| `.xucxac` | | Tung xúc xắc 1-6 |
| `.amhon` | `[channel_id] [file]` | Phát nhạc vào Voice |
| `.truhon` | | Rời Voice |
| `.fake` | `[@user] [text]` | Giả mạo tin nhắn |
| `.donguyen` | | Đoạn chú lực (random power) |
| `.vonghon` | | Nhại lại tin nhắn |
| `.nguyenrua` | `[@user]` | Ám quẻ đối phương |
| `.batkhuat` | | Tự phản hồi khi bị tag |

---

## Hosting 24/7 (Wispbyte)

### Bước 1: Upload code

**GitHub (khuyến nghị):**
```
git push origin main
```
Rồi clone trên Wispbyte panel.

**Hoặc upload zip:**
- Tải `JJK-VVNK-v6.zip`
- Upload lên FileManager của Wispbyte

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

Nhấn **Start** trên panel.

### Lưu ý hosting

- Xóa `.git/`, `__pycache__/`, `.zip` để tiết kiệm dung lượng
- Python version: 3.11 hoặc 3.12
- Thêm `apt install -y ffmpeg` vào startup nếu dùng nhạc

---

## Cấu trúc file

```
JJK-VVNK/
├── main.py              ← Entry point, nạp modules
├── rate_utils.py        ← Xử lý rate limit Discord API
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
├── ngon.txt             ← Data cho lệnh .thuong
├── nhay.txt             ← Data cho lệnh .lienke
├── JJK-VVNK.bat         ← Launcher (double-click)
├── .gitignore           ← Bảo vệ secrets
├── LICENSE              ← MIT License
├── README.md            ← Tài liệu này
└── music/               ← Thư mục nhạc có sẵn (tạo thủ công)
    ├── stay_alive.mp3
    ├── styx_helix.mp3
    ├── akuma_no_ko.mp3
    └── specialz.mp3
```

---

## Yêu cầu hệ thống

| Thành phần | Yêu cầu |
|------------|----------|
| Python | 3.10+ |
| pip | Có sẵn với Python |
| ffmpeg | Cho tính năng nhạc (không bắt buộc) |
| Disk | ~50MB |
| RAM | ~100MB |

---

## Troubleshooting

### Bot không chạy

1. Kiểm tra `config.json` có token đúng chưa
2. Chạy `python main.py` trực tiếp để xem lỗi

### Lỗi `ModuleNotFoundError`

```
pip install -r requirements.txt
```

### Lỗi `No module named 'discord'`

```
pip install discord.py-self
```

### Lỗi rate limit (429)

Bot tự xử lý 429. Nếu bị spam quá, tăng delay:
```
.vohahan 2.0 text
```

### Lỗi voice / music

- Cần cài ffmpeg
- Windows: tải ffmpeg.exe, đặt trong thư mục `ffmpeg/`
- Linux: `apt install ffmpeg`
- Mac: `brew install ffmpeg`

### Không join voice được

- Kiểm tra bot có quyền `Connect` trong voice channel
- Kiểm tra voice ID đúng

### Token die / Không login được

- Token có thể bị reset khi đổi password
- Vào Developer Portal > Bot > Reset Token
- Cập nhật lại `config.json`

---

## Lưu ý quan trọng

- **Self-bot vi phạm ToS Discord** — dùng alt account, chấp nhận rủi ro
- **Không spam quá đà** — dễ bị flag và ban account
- **Token là bí mật** — không share, không commit lên GitHub
- **Backup config** — lưu token ở nơi an toàn
- **Whitelist** — thêm ID server vào `PROTECTED_GUILD_IDS` trong `rate_utils.py` để bảo vệ

---

*JJK-VVNK Bot v6.0 — Made by QU4N.TH3.D3V*
