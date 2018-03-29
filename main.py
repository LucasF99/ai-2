import nn
import time
import random

def main():
    net = nn.Network([1200,200,40,10])

    net.prt()

    times = []

    for _ in range(10):
        start_time = time.clock()
        net.run([2,3,2,5])
        times.append(time.clock()-start_time)

    net.prt()
    print("Average time: " + str(sum(times)/len(times)))

main()
