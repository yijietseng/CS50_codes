import pygame as pg
import os, random, time

# Globle parameters
FPS = 60
WIDTH = 1024
HIGHT = 588
BLACK = (0,0,0)
BLUE1 = (35,46,110)
RED = (237,28,36)
GREEN = (48,168,52)
GREEN1 = (14,209,69)



def main():

	# set up global variables
	global ground_img, background_init, dino_idle_ani, dino_fall_ani, dino_ani, dino_fall_ani
	global flying_ani, rock_ani, dino_obs_ani,gameover_img, jump_sound, gameover_sound, font_name
	global dino, all_sprites,runs, rocks, flys, score, frame, gs, clock

	# initialize pygame and pther params
	pg.init()
	pg.mixer.init()

	# Create game screen and settings
	gs = pg.display.set_mode((WIDTH,HIGHT))
	pg.display.set_caption('Dino Rush')
	clock = pg.time.Clock()

	# Load background images
	bg_scale = 2.1
	ground_img = pg.transform.scale(pg.image.load(os.path.join("img","grass.png")).convert(),(880*bg_scale,283*bg_scale))
	ground_img.set_colorkey(BLACK)
	background_init = pg.transform.scale(pg.image.load(os.path.join("img","bg.jpg")).convert(),(1010*bg_scale,280*bg_scale))

	# load dino idle images
	dino_idle_ani = []
	for i in range(5):
		dino_idle_img = pg.image.load(os.path.join('img',f'idling_{i}.png')).convert_alpha()
		dino_idle_img.set_colorkey(GREEN)
		dino_idle_ani.append(dino_idle_img)

	# load dino running images
	dino_ani = []
	for i in range(9):
		dino_img = pg.image.load(os.path.join('img',f'running0_{i}.png')).convert_alpha()
		dino_img.set_colorkey(RED)
		dino_ani.append(dino_img)
	dino = pg.image.load(os.path.join('img',f'running0_3.png')).convert_alpha()
	dino.set_colorkey(RED)

	# loading dino falling images
	dino_fall_ani = []
	for i in range(5):
		dino_fall_img = pg.image.load(os.path.join('img',f'falling{i}.png')).convert_alpha()
		dino_fall_img.set_colorkey(GREEN)
		dino_fall_ani.append(dino_fall_img)

	# loading flying obstacle images
	flying_ani = []
	for i in range(2):
		flying_img = pg.transform.scale(pg.image.load(os.path.join('img',f'flying_1{i}.png')).convert_alpha(),(608*0.15,411*0.15))
		flying_img.set_colorkey(BLUE1)
		flying_ani.append(flying_img)

	# loading rocks images
	rock_ani = []
	for i in range(7):
		rock_img = pg.image.load(os.path.join('img',f'rock{i}.png')).convert_alpha()
		rock_ani.append(rock_img)

	# load and set up ico image
	player_mini_img = pg.transform.scale(pg.image.load(os.path.join('img','player_select1.png')).convert_alpha(), (25,19))
	player_mini_img.set_colorkey(BLACK)
	pg.display.set_icon(player_mini_img)

	# loading running dino obstacle
	dino_obs_ani = []
	for i in range(9):
		dino_obs_img = pg.image.load(os.path.join('img',f'running1_{i}.png')).convert_alpha()
		dino_obs_img.set_colorkey(GREEN1)
		dino_obs_ani.append(dino_obs_img)

	# load game over image
	gameover_img = pg.transform.scale(pg.image.load(os.path.join('img','GameOver.png')).convert_alpha(), (610, 170))
	gameover_img.set_colorkey(BLACK)

	# load sounds
	jump_sound = pg.mixer.Sound(os.path.join("sound","jump1.wav"))
	gameover_sound = pg.mixer.Sound(os.path.join("sound","gameover.wav"))

	# load music
	pg.mixer.music.load(os.path.join("sound","background1.wav"))
	pg.mixer.music.set_volume(0.4)

	# load font
	font_name = pg.font.match_font('broadway')

	pg.mixer.music.play(-1)
	frame = 0
	animation_cooldown = 60
	score = 0
	current_time = pg.time.get_ticks()
	last_update = pg.time.get_ticks()
	show_init = True
	reset = False
	run = True

	while run:
		if show_init:
			close = draw_init(frame, last_update, 120)
			if close:
					break
			show_init = False
			HIGHEST_SCORE = 0
			start = time.time()
			# All sprite groups
			all_sprites = pg.sprite.Group()
			grasses = pg.sprite.Group()
			grass = Grass(score=score, sec=False)
			grass2 = Grass(score=score,sec=True)
			all_sprites.add(grass)
			all_sprites.add(grass2)
			grasses.add(grass)
			grasses.add(grass2)
			player = Player()
			all_sprites.add(player)
			rocks = pg.sprite.Group()
			flys = pg.sprite.Group()
			runs = pg.sprite.Group()

			new_rock(score)
			new_fly(score)
			new_run(score)
			key_press_time = 0

		elif reset:
			start = time.time()
			HIGHEST_SCORE = high_score
			# All sprite groups
			all_sprites = pg.sprite.Group()
			grasses = pg.sprite.Group()
			grass = Grass(score=score, sec=False)
			grass2 = Grass(score=score,sec=True)
			all_sprites.add(grass)
			all_sprites.add(grass2)
			grasses.add(grass)
			grasses.add(grass2)
			player = Player()
			all_sprites.add(player)
			rocks = pg.sprite.Group()
			flys = pg.sprite.Group()
			runs = pg.sprite.Group()

			new_rock(score)
			new_fly(score)
			new_run(score)
			key_press_time = 0
			reset = False

		# Start scoring
		if show_init == False and reset == False:
			score_speed = 8
			running_time = time.time()
			score = int((running_time - start)*score_speed)

			# Speed up scoring
			if 100 <= score < 200:
				score_speed += 1
			elif 200 <= score < 400:
				score_speed += 2
			elif 400 <= score < 600:
				score_speed += 4
			elif 600 <= score < 800:
				score_speed += 6
			elif 800 <= score < 1000:
				score_speed += 8
			elif 1000 <= score < 2000:
				score_speed += 10
			# Check high score
			if score <= HIGHEST_SCORE:
				high_score = HIGHEST_SCORE
			else:
				high_score = score

		# update player animation
		now = pg.time.get_ticks()
		if now - last_update >= animation_cooldown:
			frame += 1
			last_update = now
			if frame >= len(dino_ani):
				frame = 0

		# Game events
		clock.tick(FPS)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				run = False

		# updating game
		all_sprites.update()

		# hitting the obstacles
		hits_rock = pg.sprite.spritecollide(player,rocks,False, pg.sprite.collide_circle)
		hits_fly = pg.sprite.spritecollide(player,flys,False, pg.sprite.collide_circle)
		hits_run =pg.sprite.spritecollide(player,runs,False, pg.sprite.collide_circle)
		if hits_rock or hits_fly or hits_run:
			time.sleep(0.5)
			gameover_sound.play()
			restart = draw_gameover(score=score)
			if restart:
				reset = True
			else:
				run = False

		# display
		gs.blit(background_init, (0,0))
		#gs.blit(dino_ani[frame],(120,100))
		all_sprites.draw(gs)
		draw_text(gs, f'Score: {score:06d}', 30, WIDTH/2, 30)
		draw_text(gs, f'Highest score: {high_score}', 15, WIDTH - 90, 30)
		pg.display.update()


	pg.quit()

def new_rock(score:int):
	r = Rock(score=score)
	all_sprites.add(r)
	rocks.add(r)

def new_fly(score:int):
	f = Flying_obstacle(score=score)
	all_sprites.add(f)
	flys.add(f)

def new_run(score:int):
	run = Running_obstacle(score=score)
	all_sprites.add(run)
	runs.add(run)

def draw_text(surf, text, size, x, y):
	font = pg.font.Font(font_name, size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.centerx = x
	text_rect.top = y
	surf.blit(text_surface, text_rect)

def draw_x_y_test(x:int, y:int):
	if x > 1024 or x < 0:
		return False
	elif y > 588 or y < 0:
		return False
	else:
		return True


def draw_init(frame,last_update,animation_cooldown):
	last_update = last_update
	animation_cooldown = animation_cooldown
	# check if start the game
	waiting = True
	while waiting:
		# update animation frame
		now = pg.time.get_ticks()
		if now - last_update >= animation_cooldown:
			frame += 1
			last_update = now
		if frame >= len(dino_idle_ani):
			frame = 0
		# update actual animation
		gs.blit(background_init, (0,0))
		gs.blit(ground_img,(0,50))
		draw_text(gs, 'Little Dino Rush', 100, WIDTH/2, HIGHT/4)
		draw_text(gs, 'Press space to jump', 40, WIDTH/2, HIGHT/2)
		draw_text(gs, 'Press any key to start', 30, WIDTH/2, HIGHT*0.65)
		gs.blit(dino_idle_ani[frame],(WIDTH/4,HIGHT-120))
		pg.display.update()

		# game event
		clock.tick(60)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				return True
			elif event.type == pg.KEYUP:
				waiting = False
				return False

def init_param_test(frame,last_update,animation_cooldown):
	if frame < 0 or last_update < 0 or animation_cooldown < 0:
		return False
	else:
		return True

def draw_gameover(score):
	# update dino falling animation
	for img in dino_fall_ani:
		gs.blit(background_init, (0,0))
		gs.blit(gameover_img, (WIDTH/5, 110))
		gs.blit(ground_img,(0,35))
		draw_text(gs, f'Your Score: {score}', 70, WIDTH/2, (HIGHT/2)-20)
		draw_text(gs, 'Press R to restart', 40, WIDTH/2, (HIGHT*0.65)-20)
		gs.blit(img,((WIDTH/2)-70,HIGHT-120))
		pg.display.update()
		time.sleep(0.15)

	waiting = True
	while waiting:
		clock.tick(FPS)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				return False
			elif event.type == pg.KEYUP:
				if event.key == pg.K_r:
					waiting = False
					return True

def score_test(score):
	if score < 0:
		return False
	else:
		return True


class Player(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		# set initial image and cooridanance
		self.image = dino
		self.rect = self.image.get_rect()
		self.radius = 35
		#pg.draw.circle(self.image, RED, self.rect.center,self.radius)

		self.y_ori = HIGHT - 120
		self.rect.x = WIDTH/4
		self.rect.y = self.y_ori

		# params for jumping
		self.Y_GRAVITY = 2.6
		self.JUMP_HIGHT = 40
		self.Y_speed = self.JUMP_HIGHT
		self.jumping = False

	def update(self):
		self.image = dino_ani[frame]
		#pg.draw.circle(self.image, RED, self.rect.center,self.radius)
		# jumping
		key_pressed = pg.key.get_pressed()
		if key_pressed[pg.K_SPACE]:
			self.jumping = True
			jump_sound.play()
		if self.jumping:
			self.rect.y -= self.Y_speed
			self.Y_speed -= self.Y_GRAVITY
			if self.Y_speed < -self.JUMP_HIGHT:
				self.Y_speed = self.JUMP_HIGHT
				self.rect.y = self.y_ori
				self.jumping = False

class Rock(pg.sprite.Sprite):
	def __init__(self, score:int):
		pg.sprite.Sprite.__init__(self)
		#self.image = pg.Surface((60,50))
		#self.image.fill(BLACK)
		self.image = random.choice(rock_ani)
		self.rect = self.image.get_rect()
		self.radius = self.rect.height/2
		#pg.draw.circle(self.image, RED, self.rect.center,self.radius)
		self.rect.x = 1100
		self.locations = [HIGHT, HIGHT-100]
		self.rect.y = random.choices(self.locations, weights=(40,60))[0]
		self.score = score
		self.speedx = 10

	def update(self):
		# adjusting moving speed according to score
		self.radius = self.rect.height/2
		#pg.draw.circle(self.image, RED, self.rect.center,self.radius)

		self.score = score
		self.rect.x -= self.speedx
		if 0 < self.score < 100:
			self.speedx = 10
		elif 100 <= self.score < 200:
			self.speedx = 13
		elif 200 <= self.score < 400:
			self.speedx = 17
		elif 400 <= self.score < 600:
			self.speedx = 22
		elif 600 <= self.score < 800:
			self.speedx = 28
		elif 800 <= self.score < 1000:
			self.speedx = 35
		elif 1000 <= self.score < 2000:
			self.speedx = 45

		if self.rect.right <= 0:
			scale = random.uniform(0.5, 1.8)
			self.image = pg.transform.scale(random.choice(rock_ani), (self.rect.width*scale, self.rect.height*scale))
			self.rect.x = random.randrange(1024,1100)
			if 0 <= self.score < 100:
				self.rect.y = random.choices(self.locations, weights=(30,70))[0]
			elif 100 <= self.score < 400:
				self.rect.y = random.choices(self.locations, weights=(20,80))[0]
			elif 400 <= self.score < 800:
				self.rect.y = random.choices(self.locations, weights=(10,90))[0]
			elif self.score > 800:
				self.rect.y = random.choices(self.locations, weights=(10,90))[0]

class Flying_obstacle(pg.sprite.Sprite):
	def __init__(self, score:int):
		pg.sprite.Sprite.__init__(self)
		#self.image = pg.Surface((60,50))
		#self.image.fill(BLACK)
		self.image = flying_ani[0]
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(1200,1400)
		self.locations = [HIGHT, HIGHT-140, HIGHT-240]
		self.rect.y = random.choices(self.locations, weights=(80,10,10))[0]
		self.radius = 30.8
		#pg.draw.circle(self.image, RED, self.rect.center,self.radius)
		self.score = score
		self.speedx = 15
		self.last_update_f = pg.time.get_ticks()
		self.animation_cooldown1 = 120
		self.frame2 = 0


	def update(self):
		now = pg.time.get_ticks()

		if now - self.last_update_f >= self.animation_cooldown1:
			self.frame2 += 1
			self.last_update_f = now
		elif self.frame2 >= len(flying_ani):
			self.frame2 = 0
		self.image = flying_ani[self.frame2-1]
		#self.rect = self.image.get_rect()

		#pg.draw.circle(self.image, RED, self.rect.center,self.radius)




		# adjusting moving speed according to score
		self.score = score
		self.rect.x -= self.speedx
		if 0 < self.score < 100:
			self.speedx = 10
		elif 100 <= self.score < 200:
			self.speedx = 13
		elif 200 <= self.score < 400:
			self.speedx = 17
		elif 400 <= self.score < 600:
			self.speedx = 22
		elif 600 <= self.score < 800:
			self.speedx = 28
		elif 800 <= self.score < 1000:
			self.speedx = 35
		elif 1000 <= self.score < 2000:
			self.speedx = 45

		if self.rect.right <= 0:
			self.rect.x = random.randrange(1400,1600)
			if 0 <= self.score < 100:
				self.rect.y = random.choices(self.locations, weights=(70,15,15))[0]
			elif 100 <= self.score < 400:
				self.rect.y = random.choices(self.locations, weights=(50,25,25))[0]
			elif 400 <= self.score < 800:
				self.rect.y = random.choices(self.locations, weights=(40,30,30))[0]
			elif self.score > 800:
				self.rect.y = random.choices(self.locations, weights=(30,40,40))[0]

class Running_obstacle(pg.sprite.Sprite):
	def __init__(self, score:int):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((60,50))
		self.image.fill(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(1300,1700)
		self.radius = 35
		self.locations = [HIGHT, HIGHT-90, HIGHT-100, HIGHT-110]
		self.rect.y = random.choices(self.locations, weights=(85,5,5,5))[0]
		self.score = score
		self.speedx = 15
		self.last_update_f = pg.time.get_ticks()
		self.animation_cooldown1 = 120
		self.frame2 = 0


	def update(self):
		now = pg.time.get_ticks()

		if now - self.last_update_f >= self.animation_cooldown1:
			self.frame2 += 1
			self.last_update_f = now
		elif self.frame2 >= len(dino_obs_ani):
			self.frame2 = 0
		self.image = dino_obs_ani[self.frame2-1]



		# adjusting moving speed according to score
		self.score = score
		self.rect.x -= self.speedx
		if 0 < self.score < 100:
			self.speedx = 10
		elif 100 <= self.score < 200:
			self.speedx = 13
		elif 200 <= self.score < 400:
			self.speedx = 17
		elif 400 <= self.score < 600:
			self.speedx = 22
		elif 600 <= self.score < 800:
			self.speedx = 28
		elif 800 <= self.score < 1000:
			self.speedx = 35
		elif 1000 <= self.score < 2000:
			self.speedx = 45


		if self.rect.right <= 0:
			self.rect.x = random.randrange(1300,1700)
			if 0 <= self.score < 100:
				self.rect.y = random.choices(self.locations, weights=(85,5,5,5))[0]
			elif 100 <= self.score < 400:
				self.rect.y = random.choices(self.locations, weights=(70,10,10,10))[0]
			elif 400 <= self.score < 800:
				self.rect.y = random.choices(self.locations, weights=(60,13.3,13.3,13.3))[0]
			elif self.score > 800:
				self.rect.y = random.choices(self.locations, weights=(40,20,20,20))[0]

class Grass(pg.sprite.Sprite):
	def __init__(self, score:int, sec=False):
		pg.sprite.Sprite.__init__(self)
		self.image = ground_img
		self.rect = self.image.get_rect()
		if not sec:
			self.rect.x = 0
		else:
			self.rect.x = WIDTH	+ 10
		self.rect.y = 35
		self.score = score
		self.speedx = 10


	def update(self):
		self.score = score
		self.rect.x -= self.speedx
		gs.blit(self.image,(0, 35))
		if 0 < self.score < 100:
			self.speedx = 10
		elif 100 <= self.score < 200:
			self.speedx = 13
		elif 200 <= self.score < 400:
			self.speedx = 17
		elif 400 <= self.score < 600:
			self.speedx = 22
		elif 600 <= self.score < 800:
			self.speedx = 28
		elif 800 <= self.score < 1000:
			self.speedx = 35
		elif 1000 <= self.score < 2000:
			self.speedx = 45

		if self.rect.right <= 0:
			self.rect.x = WIDTH
			self.rect.y = 35



if __name__ == '__main__':
	main()