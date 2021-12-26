from vpython import *
# canvas color
canvas(background=vector(0, 0, 0))

# init objects
###################################################
star1 = sphere(pos=vector(0, -1e11, 0), color=color.yellow,
               mass=2.1*10**30, radius=2e10, retain=50, make_trail=True) # ALPHA CENTAURI A
star1.momentum = vector(0, 0, -1e4) * star1.mass # ALPHA CENTAURI A MOMENTUM
star2 = sphere(pos=vector(0,2.5e11, 0),
               color=color.orange, mass=1.8*10 ** 30, radius=1e10, retain=50, make_trail=True) # ALPHA CENTAURI B
star2.momentum = -star1.momentum # ALPHA CENTAURI B MOMENTUM
####################################################

dt = 1e5 # DELTATIME

while 1:
    rate(200)
    G = 6.7e-11 # GRAVITATIONAL CONSTANT
    distance = star1.pos-star2.pos # CALCULATE DISTANCE
    distance_mag = mag(distance) # GET THE MAGNITUDE OF THE DISTANCE VECTOR

    F = G * star1.mass * star2.mass * distance.hat / distance_mag**2 # CALCULATE THE FORCE
    star1.momentum -= F * dt # UPDATE THE ALPHA CENTAURI A'S MOMENTUM
    star2.momentum += F * dt # UPDATE THE ALPHA CENTAURI B'S MOMENTUM

    star1.pos += (star1.momentum/star1.mass)*dt # UPDATE ALPHA CENTAURI A POSITION
    star2.pos += (star2.momentum/star2.mass)*dt # UPDATE ALPHA CENTAURI B POSITION
    
    
    
  # END
  # BY ANXDEV -----------------------------------------




    
