# FTP Server Termux

FTP server lokal untuk Termux Android — anonymous access, tanpa username/password, hanya untuk penggunaan pribadi.

## Download

```bash
# Clone repo
git clone https://github.com/superdecrypt-dev/ftp_termux.git
cd ftp_termux
```

Atau download langsung file `ftp_termux.py`:
```
https://raw.githubusercontent.com/superdecrypt-dev/ftp_termux/main/ftp_termux.py
```

## Persyaratan

- Termux Android
- Koneksi internet (hanya sekali untuk instalasi)

## Instalasi

```bash
# 1. Update package
pkg update && pkg upgrade

# 2. Install Python
pkg install python

# 3. Install library FTP
pip install pyftpdlib
```

## Penggunaan

### Jalankan (default)

```bash
python ftp_termux.py
```

Output:
```
=======================================================
  PERINGATAN KEAMANAN
=======================================================
  Server FTP ini TANPA PASSWORD.
  HANYA untuk jaringan lokal pribadi.
  JANGAN dibuka ke Wi-Fi publik atau internet.

  ftp://127.0.0.1:2121
  Direktori: /data/data/com.termux

  Tekan Ctrl+C untuk menghentikan server.
=======================================================
```

### Opsi kustom

```bash
python ftp_termux.py --host 127.0.0.1 --port 2121 --dir /data/data/com.termux
```

| Opsi | Default | Deskripsi |
|------|---------|-----------|
| `--host` | `127.0.0.1` | Alamat host |
| `--port` | `2121` | Port FTP |
| `--dir` | `/data/data/com.termux` | Direktori yang di-share |

### Menghentikan server

Tekan `Ctrl+C` di terminal.

### Contoh koneksi dari PC

Di file manager PC (Nautilus, Finder, Explorer):
```
ftp://127.0.0.1:2121
```

Atau dari browser:
```
ftp://127.0.0.1:2121
```

## Peringatan Keamanan

- FTP ini **TANPA PASSWORD** — siapa pun yang bisa menjangkau host:port bisa mengakses file Anda.
- Default hanya listen di `127.0.0.1` (localhost) — aman karena hanya perangkat sendiri yang bisa akses.
- **JANGAN** set `--host 0.0.0.0` saat terhubung ke Wi-Fi publik atau jaringan yang tidak Anda percayai.
- Hanya gunakan untuk transfer file cepat antara perangkat Anda sendiri di jaringan pribadi.

## Lisensi

MIT
