# HostBot v6.3

**Bot Discord Self-Bot voi Console Manager va Che do Tu cao hoa**
Tac gia: **QU4N.TH3.D3V**

---

## HostBot la gi?

HostBot la mot **bot Discord** chay bang **tai khoan nguoi dung** (khong phai Bot Token). Bot co the:

- Spam tin nhan, tao/khoa kenh, xoa kenh
- Phat nhac tu YouTube
- Choi game giai tri
- Quan ly server

**Luu y quan trong:** Self-bot vi pham ToS Discord. Hay dung **tai khoan phu (alt account)**.

---

## CACH CAI DAT (2 buoc)

### Buoc 1: Tai ve may

**Cach A - Double-click (de nhat):**
1. Nhan vao day de tai: https://github.com/nguyenminhquan2012ct-oss/jjkvvnk
2. Nhan nut **Code** > **Download ZIP**
3. Giai nen thu muc
4. **Double-click file `HostBot.bat`**
5. Nhap Token khi duoc hoi -> Xong!

**Cach B - Git (neu biet):**
```bash
git clone https://github.com/nguyenminhquan2012ct-oss/jjkvvnk.git
cd jjkvvnk
pip install -r requirements.txt
python console.py
```

### Buoc 2: Nhap Token

Khi chay `HostBot.bat` hoac `python console.py`, bot se hoi Token.

**Lay Token tu dau?**
1. Vao: https://discord.com/developers/applications
2. Nhan **New Application** ->Nhap ten -> Nhan **Create**
3. Chon **Bot** o menu trai
4. Nhan **Reset Token** -> **Yes, do it!** -> Copy Token
5. Dan vao console hoac file `config.json`

---

## CONSOLE - CACH SU DUNG

Sau khi chay, ban se thay console nhu the nay:

```
                  QU4N.TH3.D3V
    ██╗   ██╗██╗   ██╗███╗   ██╗██╗  ██╗
    ...
    v6.3.0 | Console Manager
==================================================
  [12:00:00] Console san sang. Go help de xem huong dan.

HostBot >
```

### Cac lenh co ban

| Lenh | Nghia | Vi du |
|------|-------|-------|
| `start` | Khoi dong bot | `start` |
| `stop` | Dung bot | `stop` |
| `restart` | Tat roi bat lai | `restart` |
| `kill` | Tat luon (kho) | `kill` |
| `status` | Xem bot dang chay hay da dung | `status` |
| `help` | Xem danh sach lenh | `help` |
| `clear` | Xoa man hinh | `clear` |
| `exit` | Thoat | `exit` |

### Phim tat nhanh

| Phim | Lenh |
|------|------|
| `s` | = start |
| `p` | = stop |
| `r` | = restart |
| `q` | = exit |

### Vi du thuc te

**Khoi dong bot:**
```
HostBot > start
  [12:00:00] Dang khoi dong HostBot...
  [12:00:05] HostBot da duoc khoi dong!
```

**Dung bot:**
```
HostBot > stop
  [12:05:00] Dang dung HostBot...
  [12:05:02] HostBot da dung.
```

**Restart:**
```
HostBot > restart
  [12:10:00] Dang restart...
  [12:10:02] HostBot da duoc khoi dong!
```

---

## CAI DAT TEN BOT, AUTHOR, PREFIX

### Doi ten bot

```
HostBot > config bot_name SukunaBot
  [12:00:00] bot_name = SukunaBot
```

### Doi ten tac gia

```
HostBot > config author TenCuaBan
  [12:00:00] author = TenCuaBan
```

### Doi prefix (dau lenh)

Mac dinh la `.`. Ban co the doi thanh `!`, `?`, `>`,...

```
HostBot > config prefix ?
  [12:00:00] prefix = ?
```

Sau khi doi, tat ca lenh se dung prefix moi:
- `?menu` thay vi `.menu`
- `?play` thay vi `.play`
- `?vohahan` thay vi `.vohahan`

### Xem tat ca cau hinh

```
HostBot > config
  =======================================================
  CAU HINH HIEN TAI
  =======================================================
  Token:          abc12345...xyz9
  Prefix:         ?
  Bot Name:       SukunaBot
  Author:         TenCuaBan
  Auto GIF:       True
  ...
```

---

## TUY CHINH MENU CHINH

Menu chinh la cai hien khi go `?menu`. Ban co the doi moi thu.

### Doi title menu

```
HostBot > menu set title SUKUNA'S DOMAIN
  [12:00:00] Menu title = SUKUNA'S DOMAIN
```

### Doi mo ta menu

```
HostBot > menu set desc Chon thuat thuc muon su dung:
  [12:00:00] Menu desc = Chon thuat thuc muon su dung:
```

### Doi mau menu

```
HostBot > menu set color 0xFF0000
  [12:00:00] Menu color = 0xFF0000
```

Mau mac dinh: `0x800080` (tim)
- `0xFF0000` = Do
- `0x00FF00` = Xanh la
- `0x0000FF` = Xanh duong
- `0xFFFF00` = Vang
- `0xFF00FF` = Hong
- `0x00FFFF` = Cyan

### Doi footer menu

```
HostBot > menu set footer SukunaBot | {servers} servers
  [12:00:00] Menu footer = SukunaBot | {servers} servers
```

### Doi tung phan cua menu

Menu co 6 phan: `war`, `music`, `fun`, `utility`, `admin`, `troll`

**Xem danh sach phan:**
```
HostBot > menu list
  Menu Sections:
    war: ⚔️ WAR -> raid (Menu chien tranh)
    music: 🎵 MUSIC -> nhac (Menu nhac)
    fun: 🎮 FUN -> traloi (Menu giai tri)
    utility: 🛠️ UTILITY -> chucu (Menu tien ich)
    admin: 🛡️ ADMIN -> quanly (Menu quan ly)
    troll: 🃏 TROLL -> troll (Menu troll)
```

**Doi ten phan:**
```
HostBot > menu section war name CHIEN TRANH
  [12:00:00] Section 'war' name = CHIEN TRANH
```

**Doi emoji phan:**
```
HostBot > menu section war emoji 🔥
  [12:00:00] Section 'war' emoji = 🔥
```

**Doi lenh goi phan:**
```
HostBot > menu section war command tancong
  [12:00:00] Section 'war' command = tancong
```

**Doi mo ta phan:**
```
HostBot > menu section war desc Tan cong server dich
  [12:00:00] Section 'war' desc = Tan cong server dich
```

**Doi mau phan:**
```
HostBot > menu section music color 0x00FF00
  [12:00:00] Section 'music' color = 0x00FF00
```

---

## DOI TEN LENH

Ban co the doi ten bat ky lenh nao thanh ten ngan hon hoac de nho hon.

### Doi ten lenh

```
HostBot > alias vohahan spam
  [12:00:00] Alias: vohahan -> spam
```

Bay gio ban co the go `?spam` thay vi `?vohahan`.

### Doi nhieu lenh

```
HostBot > alias khaitram xoa
  [12:00:00] Alias: khaitram -> xoa

HostBot > alias huydiet nuke
  [12:00:00] Alias: huydiet -> nuke

HostBot > alias avatar avt
  [12:00:00] Alias: avatar -> avt

HostBot > alias trivia doan
  [12:00:00] Alias: trivia -> doan
```

### Xem danh sach ten lenh

```
HostBot > alias list
  Command Aliases:
    vohahan -> spam
    khaitram -> xoa
    huydiet -> nuke
    avatar -> avt
    trivia -> doan
```

### Xoa ten lenh

```
HostBot > alias del spam
  [12:00:00] Da xoa alias: spam
```

---

## TU DONG GUI GIF SAU MOI LENH

Khi bat, bot se tu dong gui 1 URL GIF sau moi lenh. Ban co the tuy chinh URL moi.

### Bat/Tat

```
HostBot > config auto_gif true    # Bat
HostBot > config auto_gif false   # Tat
```

### Them GIF moi

```
HostBot > gif_add raid https://media.tenor.com/sukuna.gif
  [12:00:00] GIF 'raid' da duoc them.
```

### Xoa GIF

```
HostBot > gif_del raid
  [12:00:00] GIF 'raid' da duoc xoa.
```

### Xem danh sach GIF

```
HostBot > gif_list
  GIF Responses:
    raid: https://media.tenor.com/sukuna.gif
    music: https://media.tenor.com/music.gif
```

### Cac loai GIF

| Loai | Khi nao gui |
|------|------------|
| `spam` | Lenh spam tin nhan |
| `raid` | Lenh voice raid |
| `nuke` | Lenh xoa/tao kenh |
| `music` | Lenh phat nhac |
| `fun` | Lenh game giai tri |
| `troll` | Lenh troll |
| `admin` | Lenh quan ly |

---

## STATUS CYCLE (TU DONG CHUYEN DOI)

Bot tu dong hien thi trang thai khac nhau sau moi 10 giay.

### Them status

```
HostBot > status_add Dang hoat dong...
  [12:00:00] Da them status: Dang hoat dong...

HostBot > status_add Go ?help de tro giup
  [12:00:00] Da them status: Go ?help de tro giup
```

### Xem danh sach

```
HostBot > status_list
  Status Cycle:
    1. .menu de mo Menu
    2. HostBot v6.2
    3. Dung .help de tro giup
    4. Dang hoat dong...
    5. Go ?help de tro giup
```

### Xoa status

```
HostBot > status_del 4
  [12:00:00] Da xoa: Dang hoat dong...
```

---

## DAT LAI MAC DINH

Neu ban lam hau het roi, co the dat lai tat ca ve mac dinh.

```
HostBot > reset all
  [12:00:00] Da dat lai tat ca cau hinh ve mac dinh!
```

| Lenh | Nghia |
|------|-------|
| `reset all` | Dat lai TAT CA ve mac dinh |
| `reset menu` | Dat lai menu ve mac dinh |
| `reset gif` | Dat lai GIF ve mac dinh |
| `reset alias` | Xoa tat ca ten lenh da doi |

---

## DANH SACH LENH BOT

Prefix mac dinh: `.` (co the doi trong console)

### Lenh menu

| Lenh | Mo ta |
|------|-------|
| `.menu` | Menu chinh |
| `.lanhdia` | Menu chinh (ANSI) |
| `.info` | Thong tin bot |
| `.ngung` | Dung tat ca thuat thuc |

### Lenh war (chien tranh)

| Lenh | Tham so | Mo ta |
|-------|---------|-------|
| `.raid` | | Menu war |
| `.vohahan` | `[delay] [text]` | Spam tuy chinh |
| `.thuong` | `[delay]` | Spam ngon.txt |
| `.lienke` | `[delay] [@user]` | Spam nhay.txt |
| `.hacmon` | `[url] [delay] [text]` | Spam qua Webhook |
| `.ngucmon` | `[voice_id]` | Treo Voice |
| `.loanvuc` | `[voice_id] [delay]` | Spam join/leave Voice |
| `.anpham` | `[so] [emoji]` | Tha reaction hang loat |
| `.khaitram` | | Xoa toan bo kenh |
| `.huydiet` | `[webhook_url] [delay]` | Nuke server |
| `.ngung` | | Dung tat ca |

### Lenh nhac

| Lenh | Tham so | Mo ta |
|-------|---------|-------|
| `.play` | `[link/ten]` | Phat nhac tu YouTube |
| `.play-sa` | | Phat "Stay Alive" |
| `.play-sh` | | Phat "Styx Helix" |
| `.play-amk` | | Phat "Akuma no Ko" |
| `.play-sp` | | Phat "Specialz" |
| `.queue` | | Xem hang cho |
| `.skip` | | Bo qua bai hien tai |
| `.stop` | | Dung nhac + roi voice |
| `.now` | | Bai dang phat |
| `.loop` | | Bat/tat lap bai |
| `.volume` | `[1-100]` | Dieu chinh am luong |
| `.pause` | | Tam dung |
| `.resume` | | Tiep tuc |

### Lenh giai tri

| Lenh | Tham so | Mo ta |
|-------|---------|-------|
| `.traloi` | | Menu giai tri |
| `.8ball` | `[cau hoi]` | Phep boi 8 bong |
| `.rps` | `[rock/paper/scissors]` | Keo bua bao |
| `.trivia` | | Cau do vui |
| `.coinflip` | | Toss dong xu |
| `.number` | `[1-100]` | Doan so bi an |
| `.daily` | | Nhan 100-500 vang/ngay |
| `.bal` | `[@user]` | Xem so du |
| `.pay` | `[@user] [so]` | Chuyen tien |
| `.shop` | | Xem cua hang |
| `.buy` | `[ten item]` | Mua vat pham |
| `.inventory` | `[@user]` | Xem vat pham |
| `.fact` | | Fact thu vi |
| `.quote` | | Trich dan JJK |
| `.meme` | | Random meme |
| `.insult` | `[@user]` | Insult vui |
| `.compliment` | `[@user]` | Khen ngoi |
| `.avatar` | `[@user]` | Xem avatar |
| `.banner` | `[@user]` | Xem banner |

### Lenh tien ich

| Lenh | Tham so | Mo ta |
|-------|---------|-------|
| `.chucu` | | Menu tien ich |
| `.thauthi` | `[token]` | Kiem tra token |
| `.thanhduyet` | `[so]` | Xoa tin nhan |
| `.giapan` | | Dong tat ca DM |
| `.nguonluc` | | Check ping |
| `.truytung` | `[@user]` | Soi avatar |
| `.phian` | `[@user]` | Soi banner |
| `.sao-an` | `[server_id]` | Copy cau truc kenh |
| `.danhdinh` | `[@user]` | Thong tin nguoi dung |
| `.ketgioi` | | Thong tin server |
| `.dongan` | `[emoji]` | Copy emoji |

### Lenh quan ly

| Lenh | Tham so | Mo ta |
|-------|---------|-------|
| `.quanly` | | Menu quan ly |
| `.tram` | `[user]` | Kick |
| `.phong` | `[user]` | Ban |
| `.giai` | `[user_id]` | Unban |
| `.diet` | | Xoa toan bo kenh |
| `.tao` | `[ten]` | Tao 15 kenh moi |
| `.danh` | `[ten moi]` | Doi ten server |

### Lenh troll

| Lenh | Tham so | Mo ta |
|-------|---------|-------|
| `.troll` | | Menu troll |
| `.batdiet` | | Random outcome |
| `.xucxac` | | Tung xuc xac |
| `.amhon` | `[channel_id] [file]` | Phat nhac vao Voice |
| `.truhon` | | Roi Voice |
| `.fake` | `[@user] [text]` | Gia mao tin nhan |
| `.donguyen` | | Doan chu luc |
| `.vonghon` | | Nhai lai tin nhan |
| `.nguyenrua` | `[@user]` | Am que doi phuong |
| `.batkhuat` | | Tu phan hoi khi bi tag |

---

## HOSTING 24/7 (Mien phi)

### Wispbyte

1. Push code len GitHub
2. Dang ky tai khoan tai https://wispbyte.com
3. Tao server moi -> Chon Python
4. Clone repository
5. Startup Command:
```bash
if [[ -f /home/container/${REQUIREMENTS_FILE} ]]; then
  pip install -U --prefix .local -r ${REQUIREMENTS_FILE};
fi;
/usr/local/bin/python /home/container/main.py
```
6. Env var: `BOT_TOKEN` = Token Discord
7. Nhan **Start**

---

## CAU TRUC THU MUC

```
HostBot/
├── console.py           ← Console manager (chinh)
├── main.py              ← Bot logic
├── settings.json        ← Cai dat ca nhan hoa
├── config.json          ← Token & prefix
├── rate_utils.py        ← Xu ly rate limit
├── music.py             ← Phat nhac YouTube
├── raid.py              ← Lenh spam/raid
├── entertainment.py     ← Game giai tri
├── tienich.py           ← Tien ich
├── quanly.py            ← Quan ly server
├── troll.py             ← Lenh troll
├── lanhdia.py           ← Menu & info
├── ui.py                ← UI helpers
├── cache.py             ← Cache
├── requirements.txt     ← Dependencies
├── HostBot.bat          ← Launcher
└── music/               ← Nhac co san
```

---

## LOI THUONG GAP

### Bot khong chay
- Kiem tra `config.json` co Token dung khong
- Chay `python main.py` de xem loi cu the

### Loi `ModuleNotFoundError`
```
pip install -r requirements.txt
```

### Loi `No module named 'discord'`
```
pip install discord.py-self
```

### Loi nhac khong phat duoc
- Can cai **ffmpeg**
- Windows: tai ffmpeg.exe, dat trong thu muc `ffmpeg/`
- Linux: `apt install ffmpeg`
- Mac: `brew install ffmpeg`

### Token bi reset
- Vao Developer Portal > Bot > Reset Token
- Cap nhat lai `config.json`

---

## LUU Y

- **Self-bot vi pham ToS Discord** - dung alt account
- **Token la bi mat** - khong share, khong commit len GitHub
- **Max Speed** - bot chay toc do toi da, Discord se tu gi han nhung bot retry ngay
- **Dung spam qua nhieu** - de bi flag va ban account
- **Backup config** - luu Token o noi an toan

---

*HostBot v6.3 - Made by QU4N.TH3.D3V*
