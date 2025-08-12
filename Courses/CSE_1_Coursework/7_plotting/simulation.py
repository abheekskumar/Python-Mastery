"""
Simulation is very useful in any computational task.

Water runs through a faucet somewhere between a rate of 1gallon per minute and 3 gallons per minute.
What's the time it takes to fill a 600 gallon pool?
"""
import random as rd
import matplotlib.pyplot as plt

def fill_pool(size):
    flow_rate = []
    fill_time = []
    Npoints = 10000
    for i in range(Npoints):
        r = 1 + 2*rd.random()
        flow_rate.append(r)
        fill_time.append(size/r)
    
    print("Avg. fill time:",(sum(fill_time)/len(fill_time)))
    print("Avg flow rate:",(sum(flow_rate)/len(flow_rate)))
    plt.figure()
    plt.clf()
    plt.scatter(range(Npoints),flow_rate, s =1)
    plt.title("Flow Rate")

    plt.figure()
    plt.clf()
    plt.scatter(range(Npoints),fill_time,s = 1)
    plt.title("Fill Rate")

    plt.show()


fill_pool(600)