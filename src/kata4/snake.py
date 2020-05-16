import pygame, sys, time, random
from pygame.locals import *

#pygame.init()
#play_surface = pygame.display.set_mode((500, 500))
#fps = pygame.time.Clock()

class Snake():
    position = [100,50]
    body = [[100,50], [90,50],[80,50]]
    direction = "RIGHT"
    change = direction

    # Manejo del pressed [KEYDOWN] de las teclas [K_RIGHT - K_LEFT - K_UP -K_DOWN ]
    def controller(self, event, pygame):                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:                  
                    for l in self.body:                        
                        l[0] += 1                
                        l[1] += 1
                elif event.key == pygame.K_LEFT:
                    for l in self.body:
                        l[0] -= 1
                        l[1] -= 1                    
                elif event.key == pygame.K_UP:
                    for l in self.body:
                        l[0] -= 1
                        l[1] -= 1
                elif event.key == pygame.K_DOWN:
                    for l in self.body:
                        l[0] -= 1
                        l[1] -= 1
                    

            elif event.type == pygame.KEYUP:
                for l in self.body:
                    l[0] += 0
                    l[1] += 0
                

    # Controla el cambio de  las direcciones
    # Orientaciones
    # Vertical      -> Movimientos [RIGHT - LEFT]
    # Horizontal    -> Movimientos [UP - DOWN]
    # Incremento del movimiento 
    def changeDirection(self):

        for event in pygame.event.get():
            if event.type == pygame.K_RIGTH:
                self.position[0]+=1
                self.position[1]+=1
            if event.type == pygame.K_LEFT:
                self.position[0]-=1
                self.position[1]-=1
            if pygame.event.type == pygame.K_UP:
                self.position[0]+=1
                self.position[1]+=1
            if pygame.event.type == pygame.K_DOWN:
                self.position[0]-=1
                self.position[1]-=1

        self.body.insert(0, list(self.position))

class Game():
    run = True
    food_pos = 0
    score = 0

    def __init__(self):
        self.food_spawn()

    # función de salida
    def exit(self, event, pygame):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    
    # Posición aleatorio entre el ranto [0,49] * 10  
    def food_spawn(self):
        self.food_pos = 0

    # Si colisionas con una fruta, sumas 1
    # Sino decrementas en 1 el body del snake
    def eat(self, snake):
        
        if snake.body == self.food_pos:             
            for l in snake.body:
                l[0] += 1
                l[1] += 1
            
                
        else:
            for l in snake.body:
                l[0] -= 1
                l[1] -= 1
            
                
        #    
        #    
        #
        #  

    # Mensajes de salida cuando el snake muere
    # Posición snake[0] >= 500 ó snake[0] <= 0                  -> Muere
    # Posición snake[1] >= 500 ó snake[1] <= 0                  -> Muere
    # Posición del snake choca con sigo mismo menos la cabeza   -> Muere 
    def dead(self, snake):
        if snake[0] > 499 or snake[0] < 1:
            for l in snake.body:
                l[0] += 1
                l[1] += 1
            
        if snake[0] > 499 or snake[1] < 1:
            for l in snake.body:
                l[0] = 0
                l[1] = 0
            
                    
        #
        #
        #
        
        #
        #
        #
        
            
# Entry Point
def main():
    # Descomentar para lanzar el juego en local
    # Comentar para validar con el oráculo
    #pygame.init()
    #play_surface = pygame.display.set_mode((500, 500))
    #fps = pygame.time.Clock()

    snake = Snake()
    game = Game()

    # Bucle principal
    while game.run:
        for event in pygame.event.get():
            game.exit(event, pygame)
            snake.controller(event, pygame)
        
        snake.changeDirection()

        game.eat(snake)

        # Dibujar Snake
        play_surface.fill((0,0,0))
        for pos in snake.body:
            pygame.draw.rect(play_surface, (200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(play_surface, (255,160,60), pygame.Rect(game.food_pos[0], game.food_pos[1], 10, 10))

        game.dead(snake)

        pygame.display.flip()
        fps.tick(60)

        
# Comienza la aventura!!!!
# Descomentar para lanzar el juego en local
# Comentar para validar con el oráculo
#main()
#pygame.quit()
