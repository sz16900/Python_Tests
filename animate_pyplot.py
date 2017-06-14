from matplotlib import pyplot as plt
import numpy as np
import matplotlib.animation as animation

def ufield(x,y,t):
    return np.cos(x+y)*np.sin(t)

def vfield(x,y,t):
    return np.sin(x+y)*np.cos(t)

x = np.linspace(0,10, num=11)
y = np.linspace(0,10, num=11)
X,Y = np.meshgrid(x,y)
t = np.linspace(0,1)

def update_quiver(j, ax, fig):
    u = ufield(X,Y,t[j])
    v = vfield(X,Y,t[j])
    Q.set_UVC(u, v)
    ax.set_title('$t$ = '+ str(t[j]))
    return Q,

def init_quiver():
    global Q
    u = ufield(X,Y,t[0])
    v = vfield(X,Y,t[0])
    Q = ax.quiver(X, Y, u, v)
    ax.set_title('$t$ = '+ str(t[0]))
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    return  Q,

fig =plt.figure()
ax = fig.gca()
ax.set_title('$t$ = '+ str(t[0]))
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

ani = animation.FuncAnimation(fig, update_quiver,
                              frames = range(0,t.size),
                              init_func=init_quiver,
                              interval=1,fargs=(ax, fig))
plt.show()
