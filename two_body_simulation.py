import numpy as np
import time
#Length Units
G=6.67*10**(-11)
au=1.496*10**(11)
pc=3.086*10**(16)
ly=9.461*10**(15)
metre=1

dt = 1


#Mass, Position and Velocity Co-ordinates
class Objects():

  def __init__(self, mass, position, velocity):

    self.mass = mass
    self.position = position
    self.velocity = velocity


#information about each objects
object1 = Objects(1 ,  [0, 0, -0.5], [0, 0 , 0])
object2 = Objects(1 ,  [0, 0, 0.5], [0, 0 , 0])

#Force

m1 = object1.mass
m2 = object2.mass
# x1 = object1.position[0]
# y1 = object1.position[1]
# z1 = object1.position[2]
# vx1= object1.velocity[0]
# vy1= object1.velocity[1]
# vz1= object1.velocity[2]
# x2 = object2.position[0]
# y2 = object2.position[1]
# z2 = object2.position[2]
# vx2= object2.velocity[0]
# vy2= object2.velocity[1]
# vz2= object2.velocity[2]


def force(m1,x1,y1,z1,m2,x2,y2,z2):
  F = G*m1*m2 / ( (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 )
  Fx= F * (x2-x1) / ( np.sqrt( (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 ) )
  Fy= F * (y2-y1) / ( np.sqrt( (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 ) )
  Fz= F * (z2-z1) / ( np.sqrt( (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 ) )
  return [Fx,Fy,Fz]
# acc_1 = np.array(force(m1,x1,y1,z1,m2,x2,y2,z2))/m1
# acc_2 = np.array(force(m1,x1,y1,z1,m2,x2,y2,z2))*(-1)/m2

object1.position=np.array(object1.position)
object2.position=np.array(object2.position)
object1.velocity=np.array(object1.velocity)
object2.velocity=np.array(object2.velocity)

T = 0
start = time.time()
while T <= 1200000:

  x1 = object1.position[0]
  y1 = object1.position[1]
  z1 = object1.position[2]
  vx1 = object1.velocity[0]
  vy1 = object1.velocity[1]
  vz1 = object1.velocity[2]
  x2 = object2.position[0]
  y2 = object2.position[1]
  z2 = object2.position[2]
  vx2 = object2.velocity[0]
  vy2 = object2.velocity[1]
  vz2 = object2.velocity[2]

  acc_1 = np.array(force(m1, x1, y1, z1, m2, x2, y2, z2)) / m1
  acc_2 = np.array(force(m1, x1, y1, z1, m2, x2, y2, z2)) * (-1) / m2

  object1.position = object1.position + (object1.velocity * dt) + (1 / 2) * (acc_1 * dt ** 2)
  object1.velocity = object1.velocity + acc_1 * dt
  object2.position = object2.position + (object2.velocity * dt) + (1 / 2) * (acc_2 * dt ** 2)
  object2.velocity = object2.velocity + acc_2 * dt
  T = T + dt
  print(object1.position,object1.velocity)
  # if abs(object1.position[2] - object2.position[2]) <= 0.001:
  #   break
end = time.time()
print("Total time ", end-start)
print(object1.position, object2.position, T)
