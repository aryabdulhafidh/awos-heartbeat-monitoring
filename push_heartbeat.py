import os
import time
import logging
import requests

# 1. Konfigurasi Direktori & Log File
LOG_DIR = r"C:\AWOS_Scripts"
LOG_FILE = os.path.join(LOG_DIR, "heartbeat.log")

# Membuat folder C:\AWOS_Scripts secara otomatis jika belum ada
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)

# Konfigurasi format logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# 2. URL Push Unik dari Uptime Kuma
# Ganti URL di bawah ini dengan Push URL yang Anda salin dari Uptime Kuma!
UPTIME_KUMA_PUSH_URL = "http://localhost:3001/api/push/5WvlkUts7EJwsDDAB0ISMs5KOVcRcbnR?status=up&msg=OK"

logging.info("=== Service AWOS Heartbeat Diaktifkan ===")

# 3. Main Loop (Berjalan terus-menerus setiap 60 detik)
while True:
    try:
        # Kirim sinyal HTTP GET ke Uptime Kuma dengan batas waktu respon 10 detik
        response = requests.get(UPTIME_KUMA_PUSH_URL, timeout=10)
        
        if response.status_code == 200:
            logging.info(f"Heartbeat Terkirim Berhasil [HTTP {response.status_code}]")
        else:
            logging.warning(f"Heartbeat Ditolak Server [HTTP {response.status_code}]")

    except requests.exceptions.RequestException as e:
        # Menangkap error jika LAN terputus / Uptime Kuma sedang restart
        # Loop tetap berjalan agar script tidak mati total
        logging.error(f"Gagal Mengirim Heartbeat (Jaringan Down/Timeout): {e}")

    # Tunggu 60 detik sebelum mengirimkan sinyal berikutnya
    time.sleep(60)