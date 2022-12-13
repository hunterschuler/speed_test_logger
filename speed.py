import speedtest
from csv import writer
import pendulum
import time

def b2Mb(bits):
  Mb = 1000000
  return round(bits/Mb, 2)

servers = [8706]
# Change this value to your desired server.
# You can find the best server id using s.get_best_server()

threads = None
# For a single-threaded test, set threads = 1

i = 1
while i > 0:
  # Change this condition if you don't want this loop to be infinite!
  
  s = speedtest.Speedtest()
  s.download(threads=threads)
  s.upload(threads=threads)
  s.results.share()
  r = s.results.dict()
  
  
  dt = pendulum.parse(r["timestamp"])
  latest = []
  latest.append(b2Mb(r["download"]))
  latest.append(b2Mb(r["upload"]))
  latest.append(r["ping"])
  latest.append(dt.in_timezone("America/Chicago"))
  # Change this timezone to your desired timezone
  
  f = open(r'C:\Users\Hunter\Documents\speed.csv', 'a')
  # Change this path to your desired .csv file path
  
  writer_object = writer(f)
  writer_object.writerow(latest)
  f.close()
  time.sleep(300)
  # Change this value (seconds) to your desired interval for repetition
  
  print(latest)
  i = i+1
