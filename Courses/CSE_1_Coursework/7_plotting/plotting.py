import matplotlib.pyplot as plt


mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(2**i)

def plottingdifferent():
    plt.figure("Linear & Quadratic") #make figure b4 invoking labels
    plt.clf() # clearing the figure/frame after we open, just in case we were using it before
    plt.xlabel("Sample Points")
    plt.ylabel("Linear and Quadratic") # affects the "current" display
    plt.title("Linear & Quadratic Growth Order")
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.plot(mySamples,myLinear)


    plt.figure("Exponential & Cubic") # makes figure
    plt.clf() # clearing the figure/frame after we open, just in case we were using it before
    plt.xlabel("Sample Points")
    plt.ylabel("Expoenetial & Cubic")
    plt.title("Exponenetial & Cubic Growth Order")
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.plot(mySamples,myExponential)
    plt.plot(mySamples,myCubic)


    plt.figure("Linear & Quadratic")# reopen the same figure
    # plt.clf() #if we execute this, it would clear the old data
    plt.plot(mySamples,myQuadratic) # plot the data


# Plotting it all on one:
def plottingAIO():

    plt.figure("Comparison of 4 Growth Orders") # creating new figure
    plt.clf() # clear frame if used b4

    # plot data
    plt.plot(mySamples,myLinear,"b-",label = "Linear", linewidth = 2.0) 
    plt.plot(mySamples,myCubic, "ro",label = "Cubic", linewidth = 5.0)
    plt.plot(mySamples,myExponential, "g--",label = "Exponential")
    plt.plot(mySamples,myQuadratic, "k^",label = "Quadratic")
    plt.title("Comparison of 4 Growth Orders")
    plt.yscale("log") # changes the scale into a log scale

    # limits and modifications
    plt.xlim(0,20)
    plt.ylim(0,50)
    plt.xlabel("Sample Points")
    plt.ylabel("Growth Orders")
    plt.legend() # has to be called to show the labels, can specify loc 

def subplotting():
    plt.figure("Linear & Quadratic")
    plt.clf()
    plt.title("Linear vs Quadratic")
    plt.subplot(2,1,1)  # split into (row), (col), (index to use)
    plt.plot(mySamples,myLinear,"r--", label = "Linear", linewidth = 5.0)
    plt.ylim(0,900) # limited within each subplot
    plt.subplot(2,1,2) # use the other index
    plt.plot(mySamples,myQuadratic,"b", label = "Quadratic", linewidth = 3.0)
    
    plt.legend()
    plt.ylim(0,900)



plt.show()


