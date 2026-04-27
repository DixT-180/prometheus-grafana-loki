import time
from datetime import datetime
import os

name = "dikshyant-app"
log_dir = "/var/log/app-log"
log_file = f"{log_dir}/app.log"

# Ensure directory exists
os.makedirs(log_dir, exist_ok=True)

while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"{timestamp} - {name} - heartbeat log\n"

    with open(log_file, "a") as f:
        f.write(log)

    time.sleep(30)
