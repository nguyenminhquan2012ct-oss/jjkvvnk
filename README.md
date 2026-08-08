# 🔥 NÂNG CẤP JJK-VVNK BOT

## 📋 TỔNG QUAN
Nâng cấp bot self-bot Discord từ bản cơ bản lên phiên bản **pro** với:
- **War**: Spam, raid, nuke, mass actions nâng cao
- **Giải trí**: Game, meme, mini games, tương tác
- **Nhạc**: YouTube link, nhạc có sẵn, queue, volume
- **Hiệu năng**: Rate limit thông minh, cache, connection pool
- **Giao diện**: Embed, buttons, reactions, menus đẹp

---

## 🎵 PHẦN 1: NHẠC (Music Module)

### Tính năng:
```
.play [link/tên]      - Phát nhạc từ YouTube link hoặc tìm kiếm
.play-sa              - Phát "Stay Alive" (nhạc có sẵn)
.play-sh              - Phát "Styx Helix" (nhạc có sẵn)  
.queue                - Xem danh sách chờ
.skip                 - Bỏ qua bài hiện tại
.stop                 - Dừng nhạc + rời voice
.volume [1-100]       - Điều chỉnh âm lượng
.pause                - Tạm dừng
.resume               - Tiếp tục
.loop                 - Bật/tắt lặp bài
.now                  - Bài đang phát
.lyrics               - Lời bài hát hiện tại
```

### Tech requirements:
- `yt-dlp` (tối ưu hơn youtube-dl)
- `ffmpeg` (audio processing)
- `discord.py[self]` voice support
- Built-in songs: mp3 files trong thư mục `music/`
- Cache歌词, metadata

### Built-in playlist:
```
music/
├── stay_alive.mp3
├── styx_helix.mp3
├── akuma_no_ko.mp3
├── specialz.mp3
└── ... (thêm bài yêu thích)
```

---

## ⚔️ PHẦN 2: WAR (Raid Module Nâng Cao)

### Tính năng mới:
```
.vohahan [delay] [text]    - Spam tùy chỉnh (giữ)
.vohahan-all [delay] [text] - Spam TẤT CẢ kênh text
.thuong [delay]            - Spam ngon.txt (giữ)
.thuong-all [delay]        - Spam ngon.txt tất cả kênh
.hacmon [url] [delay] [text] - Webhook spam (giữ)
.khaitram                  - Xóa toàn bộ kênh (giữ)
.khaitram-all              - Xóa + tạo kênh mới + spam
.massban                   - Ban hàng loạt (từ file/list)
.masskick                  - Kick hàng loạt
.massnick [name]           - Đổi tên hàng loạt
.nukename [name]           - Đổi tên server
.delete-all                - Xóa TẤT CẢ (kênh + role + emoji)
.lockdown                  - Lock server (deny @everyone)
.raid-protect              - Tự động kick người lạ khi raid
```

### Rate limit nâng cao:
- Theo dõi `X-RateLimit-Remaining` headers
- Tự động throttle trước khi chạm limit
- Exponential backoff thông minh
- Queue system cho mass actions
- Progress bar khi thực hiện hàng loạt

---

## 🎮 PHẦN 3: GIẢI TRÍ (Entertainment Module)

### Mini Games:
```
.8ball [câu hỏi]     - Phép bói 8 bóng
.rps [rock/paper/scissors] - Kéo búa bao
.trivia              - Câu đố vui
.coinflip            - Toss đồng xu
.number [1-100]      - Đoán số
.wordle              - Game Wordle
.tictactoe [@user]   - Cờ caro
.quiz                - Quiz kiến thức
```

### Fun Commands:
```
.meme                - Random meme từ Reddit
.anime [tên]         - Tìm anime
.quote               - Random quote
.fact                - fact thú vị
.insult [@user]      - Insult random (vui)
.compliment [@user]  - Khen ngợi
.avatar [@user]      - Avatar đẹp hơn (embed)
.banner [@user]      - Banner đẹp hơn
.steam [@user]       - Steam profile
.mine                - Đào vàng mini game
.farm                - Farm resources
.daily               - Nhận quà hàng ngày
.bal                 - Xem số dư
.pay [@user] [số]    - Chuyển tiền
.shop                - Cửa hàng
.inventory           - Vật phẩm
```

### Utility nâng cao:
```
.remind [phút] [nội dung] - Nhắc nhở
.timer [giây]             - Đếm ngược
.poll [câu hỏi]          - Bình chọn (reaction)
.strawpoll               - Strawpoll link
.translate [text]         - Dịch ngôn ngữ
.weather [thành phố]     - Thời tiết
.emoji-stats             - Thống kê emoji server
.server-info             - Info server chi tiết
.user-info [@user]       - Info user chi tiết
.bot-info                - Info bot chi tiết
.uptime                  - Bot chạy được bao lâu
.ping                    - Latency
```

---

## 🎨 PHẦN 4: GIAO DIỆN (UI/UX)

### Embed Menu System:
```
.menu               - Menu chính (embed đẹp)
.warmenu            - Menu war
.musicmenu          - Menu nhạc
.funmenu            - Menu giải trí
.settingsmenu       - Menu cài đặt
```

### Features:
- Discord Embeds có màu theo loại lệnh
- Buttons cho menu chính (Interaction buttons)
- Pagination cho danh sách dài
- Progress bars khi spam/raid
- Color scheme:
  - 🔴 War: Red (#FF0000)
  - 🔵 Music: Blue (#00FF00)
  - 🟢 Fun: Green (#00FF00)
  - 🟡 Utility: Yellow (#FFFF00)
  - 🟣 Special: Purple (#800080)

### Reaction Navigation:
- ⬅️ ➡️ để chuyển trang
- ❌ để đóng menu
- ✅ để xác nhận

---

## ⚡ PHẦN 5: HIỆU NĂNG (Performance)

### Rate Limit System:
```python
class SmartRateLimiter:
    - Theo dõi headers X-RateLimit-Remaining
    - Pre-throttle: ngủ trước khi chạm limit
    - Exponential backoff: 1s → 2s → 4s → 8s...
    - Global bucket detection
    - Per-route bucket tracking
```

### Caching:
```python
class BotCache:
    - Cache user info (5 phút)
    - Cache guild info (10 phút)
    - Cache channel list (2 phút)
    - Cache role list (5 phút)
    - Auto-invalidate on changes
```

### Connection Pooling:
```python
class SessionManager:
    - aiohttp.ClientSession reuse
    - Connection keep-alive
    - Cookie jar persistence
    - Timeout configuration
```

### Memory Optimization:
- Lazy loading cho大型 file (ngon.txt, nhay.txt)
- Stream processing cho spam
- Limit cache size
- Cleanup unused objects

---

## 📦 PHẦN 6: THƯ VIỆN CẦN THÊM

```txt
# requirements.txt mới
discord.py-self>=2.0.0
aiohttp>=3.8.0
yt-dlp>=2023.1.6
ffmpeg-python>=0.2.0
pynacl>=1.5.0
pyttsx3>=2.90
googletrans==4.0.0rc1
wikipedia>=1.4.0
Pillow>=9.0.0
```

### System Dependencies:
- `ffmpeg` (audio)
- `yt-dlp` (YouTube download)

---

## 🔧 PHẦN 7: CẤU TRÚC FILE MỚI

```
JJK-VVNK/
├── main.py              - Entry point
├── rate_utils.py        - Rate limit handling
├── music.py             - Music module
├── war.py               - War module (nâng cao)
├── entertainment.py     - Games & fun
├── utils.py             - Utility functions
├── ui.py                - Embeds & menus
├── cache.py             - Caching system
├── config.py            - Cài đặt bot
├── requirements.txt
├── music/               - Built-in songs
│   ├── stay_alive.mp3
│   ├── styx_helix.mp3
│   └── ...
└── data/                - Data files
    ├── ngon.txt
    ├── nhay.txt
    ├── trivia.json
    └── memes.json
```

---

## 🚀 PHẦN 8: IMPLEMENTATION ORDER

### Phase 1: Core (Ưu tiên cao nhất)
1. ✅ Rate limit nâng cao (rate_utils.py)
2. ✅ Music module (music.py)
3. ✅ Embed menus (ui.py)
4. ✅ Cache system (cache.py)

### Phase 2: War Features
5. Mass actions (ban/kick/nick)
6. Enhanced spam
7. Server nuke nâng cao
8. Raid protection

### Phase 3: Entertainment
9. Mini games
10. Fun commands
11. Daily/economy system
12. Trivia & quotes

### Phase 4: Polish
13. Button interactions
14. Progress bars
15. Error handling đẹp
16. Logging system

---

## 💡 PROMPT CHO AI CODE

Sử dụng prompt này với AI để tạo code:

```
Tôi muốn nâng cấp bot self-bot Discord với các tính năng:

1. MUSIC MODULE:
- Phát nhạc từ YouTube link bằng yt-dlp + ffmpeg
- Built-in songs trong thư mục music/
- Queue system, volume control, loop
- Auto-disconnect sau 5 phút idle

2. WAR MODULE:
- Mass ban/kick với progress bar
- Enhanced spam với smart rate limit
- Server nuke nâng cao (delete + recreate + spam)
- Raid protection (auto-kick strangers)

3. ENTERTAINMENT:
- Mini games: 8ball, rps, trivia, wordle
- Economy: daily, bal, pay, shop, inventory
- Fun: meme, anime search, quotes, facts

4. UI:
- Discord Embeds màu sắc cho mỗi loại lệnh
- Button interactions cho menus
- Pagination cho danh sách dài
- Progress bars cho operations

5. PERFORMANCE:
- Smart rate limiter (theo dõi headers)
- Caching user/guild/channel info
- Connection pooling cho aiohttp
- Lazy loading cho大型 files

Yêu cầu:
- Sử dụng discord.py-self (self-bot)
- Tối ưu cho hosting (Linux, 512MB RAM)
- Xử lý lỗi tốt, không crash
- Code sạch, có comment tiếng Việt
```

---

## 📝 LƯU Ý

1. **Self-bot**:仍vi phạm ToS Discord — account có nguy cơ bị ban
2. **FFmpeg**: Cần cài trên hosting (apt install ffmpeg)
3. **yt-dlp**: Cần cài trên hosting (pip install yt-dlp)
4. **RAM**: Music + war cùng lúc có thể dùng nhiều RAM
5. **Rate limit**: Luôn respect Discord API limits

---

*Created: 2026-08-08*
*Version: 2.0.0*
