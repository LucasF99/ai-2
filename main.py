import nn
import time

def main():
    net = nn.Network([4,10,20,10,4])

    net.prt()

    for _ in range(10):
        net.run([2,3,2,5])

    net.prt()

main()
