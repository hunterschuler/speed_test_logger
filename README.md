# speed_test_logger
This is a python script that will perform an internet speed test (on an infinite loop) and log the results in a CSV file.

Here are some defaults that you should (or must) change if you want to use this:
* servers = [8706]

  8706 is a server in Dallas. You can find your own optimal server using s.get_best_server()
  
* threads = None

  Set threads = 1 if you want a single-threaded test
  
* while i > 0

  This condition makes the loop infinite. Change this if you don't want an infinite loop
  
* dt.in_timezone("America/Chicago")

  Change this if you want the timestamp in another timezone. See https://pendulum.eustace.io/docs/ for additional info
  
* f = open(r'C:\Users\Hunter\Documents\speed.csv', 'a')

  Change this to your desired csv file path
  
* time.sleep(300)

  Change this to your desired test interval (in seconds)

Output is in a basic (and unlabeled) format:

column1 | column2 | column3 | column4

down (mbps) | up (mbps) | ping (ms) | timestamp
