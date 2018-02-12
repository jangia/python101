import time
from threading import Thread

def print_sum(a, b):
    time.sleep(5)
    print(a + b)


start = time.time()
print('Call function')
print_sum(1, 4)
print('End function')
for j in range(50):
    time.sleep(0.1)
    print j
stop = time.time()
print('It took {0} s'.format(stop-start))
print('END')

# start = time.time()
# print('Call function')
# t = Thread(target=print_sum, args=(1, 4))
# t.setDaemon(True)
# t.start()
# print('End function')
# for j in range(50):
#     time.sleep(0.1)
#     print j
# t.join()
# #time.sleep(6)
# stop = time.time()
# print('It took {0} s'.format(stop-start))
# print('END')
