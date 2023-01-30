import subprocess
import time
countdown = 60
while countdown != 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

subprocess.Popen(['start','alarm.wav'],shell=True)
