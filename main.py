import getBCvalue
import readmp3
import schedule
import time

prev = 0

def job():
  global prev
  v =  getBCvalue.getBCvalue()
  if prev != v:
    print("BitCoin value changed !!!!  %d -----> %d" % (prev, v))
    readmp3.readmp3()
    prev = v

schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
