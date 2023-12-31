# Importer les modules
import pygame, time, random, sys
pygame.init()
pygame.font.init()

# Rapidité du jeu 
snake_speed = 15

# Couleurs
black = "#181818"
white = "#ffffff"
red = "#FF0000"
green = "#4c9506"
blue = "#002b36"

# Bordure
border = 75 

# Créer la fenêtre principale
x = 600 
y = 500
pygame.display.set_caption("Snake")
game_window = pygame.display.set_mode((border + x, border + y))

# Fréquence d'images par seconde
fps = pygame.time.Clock()

# Télécharger images
rabbit_img = pygame.image.load("images/lapin.png") 
rabbit_img = pygame.transform.scale(rabbit_img, (12, 12))

# Position du serpent au début du jeu
snake_position = [x/3 + border/3, y/2 + border/2]

# Portion du serpent
snake_body = [[100, 50],
			[90, 50],
			[80, 50],
			[70, 50]
			]

# Position de la nourriture à l'intérieur du carré blanc
food_position = [random.randrange(border + 20, border + x - 30, 10), 
				random.randrange(border + 20, border + y - 30, 10)]

# Déplacer le serpent vers l'avant
direction = 'RIGHT'
change_to = direction

score = 0
def show_score():
	# Afficher score
	score_font = pygame.font.SysFont("monospace", 16)
	score_surface = score_font.render("Score : " + str(score), True, white)
	game_window.blit(score_surface, (x + border -170 , border - 30)  )

# Fin de partie	
def game_over():
		
	# Afficher le score final
	game_window.fill(blue)
	font = pygame.font.SysFont("monospace", 30)
	
	game_over_surface = font.render(
		"Nombre de lapins mangés : " + str(score), True, white)
	
	# Afficher 
	game_over_rect = game_over_surface.get_rect()
	
	# position du texte
	game_over_rect.center= (x/2 + border/2, y/2 + border/2)
	
	# blit will draw the text on screen
	game_window.blit(game_over_surface, game_over_rect)
	
	pygame.display.flip()
	
	# after 2 seconds we will quit the program
	time.sleep(2)
	
	# deactivating pygame library
	pygame.quit()
			 
# Boucle principale		
running = True
while True:

	# Gérer les events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()  
			         
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'		

	# Si deux flèches sont appuyées simultanément 
	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	# Deplacer le serpent
	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10
	
	# Croissance du snake quand il y a colision entre le fruits et le snakes 

	if (snake_position[0] < food_position[0] + 10
    and snake_position[0] > food_position[0] - 10
    and snake_position[1] < food_position[1] + 10
    and snake_position[1] > food_position[1] - 10):
		score += 1
		snake_body.insert(0, list(snake_position))
		food_position = [random.randrange(border + 10 , border + x - 75, 10), 
				random.randrange(border + 10 , border + y -75, 10)]
			
	else:
		snake_body.insert(0, list(snake_position))
		snake_body.pop()
		
	# food_spawn = True
	game_window.fill(blue)
		
	for pos in snake_body:
		pygame.draw.rect(game_window, green,
						pygame.Rect(pos[0], pos[1], 10, 10), 10)
	game_window.blit(rabbit_img, (food_position[0], food_position[1]))

	# Game Over conditions
	if snake_position[0] < border or snake_position[0] > x-10 or  snake_position[1] < border or snake_position[1] > y-10:
		game_over()

	# Touching the snake body
	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()

	# Pour afficher le score continuellement
	show_score()

	# Bordure
	pygame.draw.rect(game_window, white,(border, border, x - border, y-border), 3 )

	# Mettre à jour l'écran
	pygame.display.update()

	# Rapidité du chargement
	fps.tick(snake_speed)


