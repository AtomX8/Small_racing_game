import pygame
from pygame.locals import *
import os
import math

# Return the sine of different values
pygame.init()

screen = pygame.display.set_mode((640,480),SCALED,OPENGL)
clock = pygame.time.Clock()
font = pygame.font.SysFont("terminal", 22)
player_1_position_x = 150
player_1_position_y = 180
vel = 0
velx = 0
vely = 0
steering_degree = 0

# path taker
sourceFileDir = os.path.dirname(os.path.abspath(__file__))
# graphics loader
# bg = pygame.image.load(os.path.join(sourceFileDir, 'graphics/background/bg.png')).convert_alpha()
input_map = pygame.image.load(os.path.join(sourceFileDir, 'yhy.png')).convert_alpha()
mini_dot = pygame.image.load(os.path.join(sourceFileDir, 'mala_kropka.png')).convert_alpha()
white = (255, 255, 255)

dot = pygame.image.load(os.path.join(sourceFileDir, 'kropka.png')).convert_alpha()
mini_dot.set_colorkey(white) 
dot.set_colorkey(white)
# bg1 = pygame.transform.scale(bg,(860,480)) 
# fps counter
def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text

# screen renderer
def screen_draw(player_1_position_x, player_1_position_y):
	 
	screen.fill((250, 250, 250))# background
	screen.blit(input_map, (17, 17)) # player 1 test
	screen.blit(dot, (player_1_position_x, player_1_position_y)) # player 1 test
	screen.blit(mini_dot, (50-(degree_x *40), 50 -(degree_y*40))) # player 1 test
	screen.blit(update_fps(), (10,10)) # fps counter
	pygame.display.update()
# main loop
loop = 1
def friction(speed):
	if(speed == 4 or speed ==-4):
		speed = 0
	speed = int(speed * 0.5)
	return speed

while loop:
	pressed_keys = pygame.key.get_pressed()

	if velx>0:
		velx+= int((-velx*0.2))
	elif velx<0:
		velx-= int((velx*0.2))
	if vely>0:
		vely+= int((-vely*0.2))
	elif vely<0:
		vely-= int((vely*0.2))
	if vel>0:
		vel-=5
	elif vel<0:
		vel+=5

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = 0    
	if pressed_keys[K_d]:
		if steering_degree >= 0:
			steering_degree -= 5
		else:
			steering_degree = 359
			
	if pressed_keys[K_a]:	
		if steering_degree < 360:
			steering_degree += 5
		else:
			steering_degree = 0

	if pressed_keys[K_s]:
		if vel < 150:
			vel+=80
			
	if pressed_keys[K_w]:	
		if vel > -150:
			vel-=80


	# print (f'degree: {steering_degree}')

	steering_degree_radian = math.radians(steering_degree) # / (90 /1.57) 
	degree_x = round(math.sin(steering_degree_radian),2)
	degree_y =  round(math.cos(steering_degree_radian),2)
	velx = velx + vel*degree_x
	vely = vely + vel*degree_y
	print (f'velocity x: {velx} velocity y: {vely} speed: {vel}')
	clock.tick(60) # fps
	player_1_position_x += (velx/100)
	player_1_position_y += (vely/100)
	# print(f'pozycja x {player_1_position_x}| pozycja y {player_1_position_y}')
	screen_draw(player_1_position_x,player_1_position_y) # screen renderer
 
pygame.quit()