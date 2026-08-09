# BUG ANALYSIS - HostBot v6.4

## LOI 1: Banner bi loi trong HostBot.bat

**Nguyen nhan:**
Ky tu Unicode box-drawing (`██╗`, `╚═╝`, `██╔╝`...)khong render duoc trong cmd.exe.
Du da dat `chcp 65001` (UTF-8), cmd.exe Windows van khong ho tro day du cac ky tu Unicode nang cao nay.
Result: Hien thi ra nhung ky tu rac nhu `╗╗╗███╗` thay vi banner dep.

**Anh huong:** Banner bi lo, nhin ghe am. Bot van chay binh thuong nhung giao dien rat kem.

**Fix:** Xoa banner Unicode khoi HostBot.bat, chi giu banner trong console.py (Python ANSI hoat dong tot hon).

---

## LOI 2: Lenh go trong Discord khong chay (NGHIEM TRONG NHAT)

**Nguyen nhan chinh - Co 2 loi trong `main.py`:**

### Bug A: `on_message` return som (Line 169)
```python
@bot.event
async def on_message(message):
    if active_features['nitro_sniper']:
        if 'discord.gift/' in message.content or ...:
            match = re.search(...)
            if not match:
                return  # <<< BUG: return ma khong goi process_commands!
    await bot.process_commands(message)  # Line 185
```
Neu tin nhan chua "discord.gift/" nhung regex khong match (VD: link bi loi, go sai),
ham `on_message` return luon ma **khong goi `bot.process_commands(message)`**.
Ket qua: Lenh bi "nuot" - user go lenh nhung bot khong xu ly.

### Bug Cog Loading (Line 115-122)
```python
skip = {'main.py', 'index.py', 'rate_utils.py', 'cache.py', '__init__.py', 'console.py'}
for filename in os.listdir('.'):
    if filename.endswith('.py') and filename not in skip:
        try:
            await bot.load_extension(filename[:-3])
```
Neu bat ky cog nao bi loi import (thieu thu vien, loi syntax...),
no chi in loi ra console nhung **khong dung bot**. Neu NHIEU cog loi,
bot chay nhung khong co lenh nao hoat dong.

**Anh huong:** Bot hien thi online nhung go lenh gi cung khong tra loi.

---

## LOI 3: Can nhap Token moi lan mo Bot

**Tinh hien tai:** Token duoc luu trong config.json va doc tu do.
Neu config.json khong co, bot bao loi va thoat.

**Yeu cau:** Moi lan mo bot len phai hoi token moi (anh toan bao mat).
Token cu trong config.json van giu lam backup nhung phai hoi truoc khi start.

---

## CAC DIEM CAN UPGRADE

1. **Console subprocess stdout** - stdout bi pipe nen bot output chi hien thi trong console,
   khong hien thi truc tiep trong terminal. Can them `stderr` pipe de bat loi.

2. **Config validation** - Kiem tra token co hop le truoc khi start bot
   (gui 1 request nho den Discord API de verify).

3. **Error handling** - Moi loi trong cog loading nen in ro rang hon de debug.

---

## DANH SACH FILE CAN SUA

| File | Loi | Do uu tien |
|------|-----|-----------|
| `HostBot.bat` | Banner Unicode loi | CAO |
| `main.py:169` | on_message return som | CAO NHAT |
| `main.py:115-122` | Cog loading error handling | TRUNG BINH |
| `console.py` | Token input moi lan start | CAO |
| `console.py` | Bot stderr pipe | TRUNG BINH |
