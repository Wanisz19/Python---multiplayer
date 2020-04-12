import pygame
import random
import time
class Snake():
    def __init__(self, window,width,heigh):
        self.heigh = heigh
        self.width = width
        self.window = window
        self.clock = pygame.time.Clock()
        self.delta = 0.0
        self.movement = 50

        self.direction = 0
        self.snake_color = (55, 255, 100)
        self.snake_pos_x = [250]
        self.snake_pos_y = [100]
        self.lenght_pyton = len(self.snake_pos_x)
        self.head_x = self.snake_pos_x[0]
        self.head_y = self.snake_pos_y[0]

        self.apple_color = (69, 69, 69)
        self.apple_pos = [0,0]
        self.apple_ex = False
        self.apple_check = True

        self.score = 0
        self.game_over = False

    def apple(self):
        while self.apple_check:
            x = random.randint(0, 23) * 50
            y = random.randint(0, 15) * 50
            if x != self.snake_pos_x[0] and y != self.snake_pos_y[0]:
                self.apple_pos[0] = x
                self.apple_pos[1] = y
                self.apple_check = False # po wygenerowaniu jabłka zakańcza generowanie drugiego
                self.apple_ex = True  #do spełnienia warunku poniżej (rysuje jabłko)

        if self.apple_ex == True:
            pygame.draw.rect(self.window, self.apple_color, (self.apple_pos[0], self.apple_pos[1], 50, 50))


    def eat(self):
        if (self.apple_pos[0] == self.snake_pos_x[0]) and (self.apple_pos[1] == self.snake_pos_y[0]):
            self.apple_ex = False # z warunku powyżej, jabłko znika.
            self.apple_check = True # ponownie uruchamia funkcje do generowania jabłka
            self.score += 1
            #self.grow_snake()    # powiekszenie snejka
            self.apple()  # pojawienie sie jablka po zjedzeniu ( chyba nie potrzebne )



    def grow_snake(self):
         self.lenght_pyton = len(self.snake_pos_x)

         if self.score >= self.lenght_pyton-1:
                x = -50
                y = -50
                self.snake_pos_x.append(x)
                self.snake_pos_y.append(y)



    def rys(self):
        self.apple()
        self.grow_snake()
        self.eat()

        for num in range(0, self.lenght_pyton):
            pygame.draw.rect(self.window, self.snake_color, (self.snake_pos_x[num], self.snake_pos_y[num], 50, 50))
            #print(num)

    def crash(self):
        for x in range(2,self.lenght_pyton):
            if self.snake_pos_x[0] == self.snake_pos_x[x] and self.snake_pos_y[0] == self.snake_pos_y[x]:
                self.game_over = True


    def dirr(self):
        self.delta += self.clock.tick()/1000.0
        if self.delta > 0.1:
            self.delta = 0

            # głowa przed poruszeniem
            self.head_x = self.snake_pos_x[0]
            self.head_y = self.snake_pos_y[0]


            self.crash()

            #ustalanie kierunku
            if not self.game_over:
                if self.direction == 1:
                    self.snake_pos_y[0] -= self.movement
                elif self.direction == 2:
                    self.snake_pos_y[0] += self.movement
                elif self.direction == 3:
                    self.snake_pos_x[0] -= self.movement
                elif self.direction == 4:
                    self.snake_pos_x[0] += self.movement

            #przechodzenie przez sciany
            if self.snake_pos_x[0] >= self.width:
                self.snake_pos_x[0] = 0
            if self.snake_pos_x[0] < 0:
                self.snake_pos_x[0] = self.width
            if self.snake_pos_y[0] >= self.heigh:
                self.snake_pos_y[0] = 0
            if self.snake_pos_y[0] < 0:
                self.snake_pos_y[0] = self.heigh

            #cialo
            if not self.game_over:
                for number in range(self.lenght_pyton, 1, -1):
                    self.snake_pos_x[number - 1] = self.snake_pos_x[number - 2]
                    self.snake_pos_y[number - 1] = self.snake_pos_y[number - 2]
                    if number == 1:
                        self.snake_pos_x[number - 1] = self.head_x
                        self.snake_pos_y[number - 1] = self.head_y


























