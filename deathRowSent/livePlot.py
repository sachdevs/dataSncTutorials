import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("data.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    x = 0
    y = 0
    for eachLine in dataArray:
        if len(eachLine)>1:
            y += (int)(eachLine)
            x += 1
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=500)
plt.axis([0, 500, -10, 10])
plt.show()