from datetime import datetime
from time import sleep

for c in range(5):
    now = datetime.now()
    print(now.strftime("%H:%M:%S"))
    sleep(1)
