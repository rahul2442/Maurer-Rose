import pygame
import math
import time
import random

pygame.init()

height=600
width=600
bg_color=(255,255,255)
display=pygame.display.set_mode((width,height))
points=[]

silver=(192,192,192)
golden=(255,215,0)
greenyellow=(173,255,47)
crimson=(220,20,60)



class rose:
	def __init__(self,n,d,color):
		self.n=n
		self.d=d
		self.color=color


	def point(self):
		for angle in range(361):
			k= angle * self.d * math.pi/180
			r= 300 * math.sin(self.n * k)
			x = r * math.cos( k)
			y= r * math.sin(k)
			temp=[width/2+x,height/2-y]
			points.append(temp)

	def draw(self):
		display.fill(bg_color)

		for x in range(len(points)-1):
			pygame.draw.line(display,self.color,points[x],points[x+1],1)
			pygame.display.update()
			time.sleep(0.05)


			

a=rose(3,47,(0,0,0))
a.point()
a.draw()
loop = True


while loop:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = False

pygame.display.update()
