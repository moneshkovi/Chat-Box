from vidstream import CameraClient
from vidstream import StreamingServer

import threading
import time

receiving = StreamingServer('IP ADDRESS', 9999) #Your_ip_address
sending = CameraClient('IP ADDRESS', 9999)  #Your-patner_ip_address

t1 = threading.Thread(target=receiving.start_server())
t1.start()

time.sleep(5)

t2 = threading.Thread(target=sending.start_stream())
t2.start()

while input("") != "STOP":
    continue

receiving.stop_server()
sending.stop.stream()
