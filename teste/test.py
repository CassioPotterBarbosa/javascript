import math
import speedtest

def mb (size_bytes):
    i = int(math.floor(math.log(size_bytes,1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return f"{size} mbps"

wifi = speedtest.Speedtest()

print("download speed...")
download_speed = wifi.download()

print("upload speed...")
upload_speed = wifi.upload()

print("dow", mb(download_speed))
print("up", mb(upload_speed))