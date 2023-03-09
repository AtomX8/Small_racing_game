import pygame
from pygame.locals import *
import os
import math

# Return the sine of different values
pygame.init()

screen = pygame.display.set_mode((1280,720),SCALED,OPENGL)
clock = pygame.time.Clock()
font = pygame.font.SysFont("terminal", 22)
player_1_position_x = 150
player_1_position_y = 180
speed = 0
velocity = [0,0]
steering_degree = 270
car_size = [45,100]
car_size_transform = [0,0]
steering_percent = [0,0]
steering_power = 0
diameter = 0.5 # in meters
wheel_base = car_size[1]/2.8
car_center = [0,0]


sourceFileDir = os.path.dirname(os.path.abspath(__file__))
# graphics loader
# bg = pygame.image.load(os.path.join(sourceFileDir, 'graphics/background/bg.png')).convert_alpha()
input_map = pygame.image.load(os.path.join(sourceFileDir, 'yhy.png')).convert_alpha()
mini_dot = pygame.image.load(os.path.join(sourceFileDir, 'mala_kropka.png')).convert_alpha()
white = (255, 255, 255)

mini_dot.set_colorkey(white) 

class wheels:
	global wheel,wheel_transform
	wheel_size_transform =[0,0]
	wheel = pygame.Surface((5, 10), pygame.SRCALPHA)
	wheel.fill((0,0,0))
	def rotation(self,degree):
		wheel_transform = pygame.transform.rotate(wheel, degree) 
		return wheel_transform

    
fr = wheels()
rr = wheels()
fl = wheels()
rl = wheels()
car = pygame.Surface((car_size[0], car_size[1]), pygame.SRCALPHA)
car.fill((255,0,0))
# bg1 = pygame.transform.scale(bg,(860,480)) 
# fps counter
def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text
def text():
	text = f'velocity x: {velocity[0]} velocity y: {velocity[1]} speed: {abs(speed)} position x {round(player_1_position_x)} position y {round(player_1_position_y,2)}'

	final_text = font.render(text, 1, pygame.Color("coral"))
	return final_text
# screen renderer
def screen_draw(player_1_position_x, player_1_position_y):
	car_transform = pygame.transform.rotate(car, steering_degree)
	car_size_transform[0], car_size_transform[1] = car_transform.get_size()
	car_center = [player_1_position_x-(car_size_transform[0]/2),player_1_position_y-(car_size_transform[1]/2)]
	screen.fill((250, 250, 250))# background
	screen.blit(input_map, (40, 40)) # player 1 test
	screen.blit(mini_dot, (70-(degree_x *40), 70 -(degree_y*40))) # player 1 test
	screen.blit(update_fps(), (10,10))
	screen.blit(car_transform, (car_center[0]+2,car_center[1]+2))
	screen.blit(fr.rotation(steering_degree),
		((player_1_position_x)-(wheel_base*degree_x)+20*degree_y,
   		(player_1_position_y-(wheel_base*degree_y)-20*degree_x
      	)))
	screen.blit(rr.rotation(steering_degree), 
	    ((player_1_position_x)+(wheel_base*degree_x)+20*degree_y,
      	(player_1_position_y+(wheel_base*degree_y)-20*degree_x
		)))
	screen.blit(fl.rotation(steering_degree),
		((player_1_position_x)-(wheel_base*degree_x)-20*degree_y,
   		(player_1_position_y-(wheel_base*degree_y)+20*degree_x
      	)))
	screen.blit(rl.rotation(steering_degree), 
	    ((player_1_position_x)+(wheel_base*degree_x)-20*degree_y,
      	(player_1_position_y+(wheel_base*degree_y)+20*degree_x
		)))
	screen.blit(text(), (70,10))
	pygame.display.update()
# main loop
loop = 1
while loop:
	pressed_keys = pygame.key.get_pressed()

	if velocity[0]>-0:
		velocity[0]+= ((-velocity[0]*0.05))
	elif velocity[0]<0:
		velocity[0]-= ((velocity[0]*0.05))
	if velocity[1]>-0:
		velocity[1]+= ((-velocity[1]*0.05))
	elif velocity[1]<0:
		velocity[1]-= ((velocity[1]*0.05))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = 0    

	steering_friction = round(1-abs(velocity[0]/3000),2)
	steering_percent[0] = round(0.5-abs(velocity[0]/6000),2)
	steering_percent[1] = round(0.5-abs(velocity[1]/6000),2)
	steering_percent_final = steering_percent[1] + steering_percent[0]
	steering_percent_final2 = 1-steering_percent_final 
	# print(steering_percent_final2)
	steering_power =  5* steering_percent_final  
	if pressed_keys[K_d]:
		if steering_degree >= 0:
			steering_degree -= steering_power
		else:
			steering_degree = 359
			
	if pressed_keys[K_a]:	
		if steering_degree < 360:
			steering_degree += steering_power
			
		else:
			steering_degree = 0

	
	if pressed_keys[K_w]:	
		if speed > -120:
			speed-=2
	if pressed_keys[K_s]:
		if speed < 50:
			speed+=1
	if not pressed_keys[K_s] and not pressed_keys[K_w]:
		speed = 0

	if pressed_keys[K_c]:
		player_1_position_x = 250
		player_1_position_y = 250	
		
	# print (f'degree: {steering_degree}')
	steering_degree_radian = math.radians(steering_degree) # / (90 /1.57) 
	degree_x = round(math.sin(steering_degree_radian),2)
	degree_y =  round(math.cos(steering_degree_radian),2)
	velocity[0] = int(velocity[0] + speed*degree_x)
	velocity[1] = int(velocity[1] + speed*degree_y)
	# print (f'velocity x: {velocity[0]} velocity y: {velocity[1]} speed: {vel}')
	# rotation = velocity[0] - velocity[1] / (diameter * math.pi)

	clock.tick(60) # fps
	player_1_position_x += (velocity[0]/100)
	player_1_position_y += (velocity[1]/100)
	# print(f'pozycja x {player_1_position_x}| pozycja y {player_1_position_y}')
	screen_draw(player_1_position_x,player_1_position_y) # screen renderer
 
pygame.quit()