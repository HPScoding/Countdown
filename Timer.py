import time
play_time = 'r'

while play_time == 'r':
  def countdown(t):
      while t:
          mins, secs = divmod(t,60)
          timer = '{:02d}:{:02d}'.format(mins, secs)
          print(timer, end = "\r")
          time.sleep(1)
          t -= 1

      print('Time up!! ') 
      play_time = input("Repeate(r): ")

  t = input('Enter the time in seconds: ')       

  countdown(int(t))
 
