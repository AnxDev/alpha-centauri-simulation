from vpython import *
#GlowScript 3.2 VPython
canvas(background=vector(0, 0, 0))


star1 = sphere(pos=vector(0, -1e11, 0), color=color.yellow,
               mass=2.1*10**30, radius=2e10, retain=50, make_trail=True)
star1.momentum = vector(0, 0, -1e4) * star1.mass
star2 = sphere(pos=vector(0,2.5e11, 0),
               color=color.orange, mass=1.8*10 ** 30, radius=1e10, retain=50, make_trail=True)
star2.momentum = -star1.momentum

t = 0
dt = 1e5

while 1:
    rate(200)
    G = 6.7e-11
    distance = star1.pos-star2.pos
    distance_mag = mag(distance)

    F = G * star1.mass * star2.mass * distance.hat / distance_mag**2
    star1.momentum -= F * dt
    star2.momentum += F * dt

    star1.pos += (star1.momentum/star1.mass)*dt
    star2.pos += (star2.momentum/star2.mass)*dt




    