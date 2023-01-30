#working with csv files and json data

import subprocess,threading,time
print('Press Enter to begin. Afterward,press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time()-lastTime,2)
        totalTime = round(time.time() - startTime,2)
        print('Lap #%s: %s (%s)' % (lapNum,totalTime,lapTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    #Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone')