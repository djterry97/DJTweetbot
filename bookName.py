import time
for i in range(1,100):
    f = open('Sources\\' + str(i) + '.txt')
    print(f.readline())
    time.sleep(1)
