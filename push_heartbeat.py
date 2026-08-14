import time
import requests
import logging
import sys

# Konfigurasi Logging: Dicatat ke file dan ditampilkan di CMD secara real-time
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("C:\\AWOS_Scripts\\heartbeat.log"),
        logging.StreamHandler(sys.stdout)  # Menampilkan pesan di layar CMD
    ]
)

# URL Push Uptime Kuma
UPTIME_KUMA_PUSH_URL = "http://localhost:3001/api/push/GGBPJFtMejHLpH4MMhe76fMNGfZjzAao?status=up&msg=OK&ping="

print("==================================================")
print("   AWOS HEARTBEAT SENDER SEDANG BERJALAN [RUNNING] ")
print("   Tekan Ctrl + C untuk mematikan script          ")
print("==================================================\n")

try:
    while True:
        try:
            response = requests.get(UPTIME_KUMA_PUSH_URL, timeout=10)
            if response.status_code == 200:
                logging.info("Heartbeat Terkirim Berhasil [HTTP 200]")
            else:
                logging.warning(f"Heartbeat Ditolak Server [HTTP {response.status_code}]")
        except requests.exceptions.RequestException as e:
            logging.error(f"Gagal Mengirim Heartbeat: {e}")
        
        # Jeda pengiriman setiap 60 detik
        time.sleep(60)

except KeyboardInterrupt:
    # Otomatis dipanggil saat menekan Ctrl + C
    print("\n==================================================")
    print(" [!] Menerima Sinyal Dihentikan (Ctrl + C)        ")
    print(" [STATUS] SCRIPT AWOS HEARTBEAT DINONAKTIFKAN!")
    print("==================================================")
    logging.info("Script dihentikan secara manual oleh pengguna.")
    sys.exit(0)