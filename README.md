# HostBot v6.4

Discord Self-Bot voi nhieu tinh nang: war, spam, nhac, giai tri, quan ly.

> ⚠️ Self-bot vi pham Discord ToS. Su dung tai khoan alt. Chu nhan chap nhan moi rui ro.

---

## Cach tai

### Cach 1: Tai file ZIP
1. Vao: https://github.com/nguyenminhquan2012ct-oss/jjkvvnk
2. Nút **Code** (mau xanh) → **Download ZIP**
3. Giai nen thu muc `jjkvvnk-main`

### Cach 2: Clone (can Git)
```bash
git clone https://github.com/nguyenminhquan2012ct-oss/jjkvvnk.git
```

---

## Cach chay

1. Mo thu muc `jjkvvnk`
2. Double-click **`Run.bat`**
3. Lan dau hoi **Discord Token** → nhap vao
4. Bot tu dong cai thu vien va khoi dong
5. Bot tu dong restart neu crash

Hoac chay thu cong:
```bash
python -m pip install -r requirements.txt
python main.py
```

---

## Cau hinh

File `config.json` (tu tao boi Run.bat):
```json
{
    "token": "DISCORD_TOKEN_CUA_BAN",
    "prefix": "."
}
```

---

## Danh sach lenh

### Menu chinh
| Lenh | Mo ta |
|------|-------|
| `.menu` | Hien thi menu chinh |
| `.lanhdia` | Hien thi menu chinh (JJK style) |
| `.info` | Thong tin bot va server |
| `.ngung` | Dung tat ca thuat thuc dang chay |

### War / Spam
| Lenh | Mo ta |
|------|-------|
| `.raid` | Menu war |
| `.vohahan [delay] [text]` | Spam tuy chinh (100 tin) |
| `.thuong [delay]` | Spam tu ngon.txt (100 tin) |
| `.lienke [delay] [@user]` | Spam tu nhay.txt (100 tin) |
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
| `.pay [@user] [so]` | Chuyen tien |
| `.shop` / `.buy [item]` | Cua hang |
| `.inventory` | Vat pham |
| `.fact` / `.quote` / `.meme` | Fun |
| `.insult [@user]` / `.compliment [@user]` | Troll vui |
| `.avatar [@user]` | Xem avatar |
| `.banner [@user]` | Xem banner |

### Tien ich
| Lenh | Mo ta |
|------|-------|
| `.chucu` | Menu tien ich |
| `.thauthi [token]` | Kiem tra token |
| `.thanhduyet [so]` | Xoa tin nhan ban than |
| `.giapan` | Dong DM |
| `.nguonluc` | Check ping |
| `.truytung [@user]` | Soi avatar |
| `.phian [@user]` | Soi banner |
| `.danhdinh [@user]` | Thong tin nguoi dung |
| `.ketgioi` | Thong tin server |
| `.dongan [emoji]` | Sao chep emoji |
| `.sao-an [server_id]` | Sao chep kenh |

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
| `.amhon [url]` | Phat nhac vao Voice |
| `.truhon` | Roi Voice |
| `.fake [@user] [text]` | Gia mao tin nhan |
| `.donguyen` | Do suc manh |
| `.vonghon` | Nhai lai tin nhan |
| `.nguyenrua [@user]` | Am que doi phuong |
| `.batkhuat` | Tu phan hoi khi bi tag |

---

## Cau truc thu muc

```
jjkvvnk/
├── main.py              # Entry point
├── Run.bat              # Launcher tu dong
├── config.json          # Token (bi gitignore)
├── settings.json        # Cau hinh bot
├── requirements.txt     # Thu vien
├── .gitignore
│
├── ui.py                # Menu
├── entertainment.py     # Giai tri / Economy
├── music.py             # Nhac
├── raid.py              # War / Spam
├── tienich.py           # Tien ich
├── quanly.py            # Quan ly
├── troll.py             # Troll
├── lanhdia.py           # Info
│
├── rate_utils.py        # Xu ly rate limit
├── cache.py             # Cache
│
├── ngon.txt             # Noi dung .thuong
├── nhay.txt             # Noi dung .lienke
├── music/               # Nhac co san
└── music_cache/         # Cache nhac
```

---

## Fix loi

- **Bot khong phan hoi**: Kiem tra token trong `config.json` dung chua
- **Loi play nhac**: Can FFmpeg - tai https://ffmpeg.org/download.html
- **Bi rate limit**: Bot xu ly tu dong, doi vai phut roi thu lai
- **Bot bi kick/khoa**: Dung tai khoan alt, khong phai tai khoan chinh

---

**QU4N.TH3.D3V** | JJK-VVNK Bot v6.4
