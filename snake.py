import pygame
import random
import time

class Snake():
    def __init__(self, window,width,heigh):

        # GENERAL SETTINGS:
        self.heigh = heigh
        self.width = width
        self.apple_color = (69,69,69)
        self.window = window
        self.movement = 50
        #TIME AND SPEED
        self.clock = pygame.time.Clock()
        self.delta = 0.0

        #APPLE
        self.apple_pos = [0,0]
        self.apple_ex = False
        self.apple_check = True
        self.apple_generator = 0

        #SNAKE NUMER ONE
        self.snake_color = (55, 255, 100)
        self.snake_pos_x = [250,250,250]
        self.snake_pos_y = [100,150,200]
        self.direction = 1
        self.score = 0
        self.lenght_pyton = len(self.snake_pos_x)
        self.head_x = self.snake_pos_x[0]
        self.head_y = self.snake_pos_y[0]
        self.game_over = False

        # SNAKE NUMER TWO
        self.snake_color2 = (200, 50, 200)
        self.snake2_pos_x = [500, 500,500]
        self.snake2_pos_y = [100, 150,200]
        self.direction2 = 1
        self.score2 = 0
        self.lenght_pyton2 = len(self.snake2_pos_x)
        self.head2_x = self.snake2_pos_x[0]
        self.head2_y = self.snake2_pos_y[0]
        self.game_over2 = False
        self.star = False




    def apple(self):

        while self.apple_check:
            x = random.randint(0, 23) * 50
            y = random.randint(0, 15) * 50
            self.apple_generator = 0

            for number in range(0,self.lenght_pyton):

                if x != self.snake_pos_x[number] and y != self.snake_pos_y[number]:
                    self.apple_generator +=1
                    if self.apple_generator == self.lenght_pyton:

                        self.apple_pos[0] = x
                        self.apple_pos[1] = y
                        self.apple_check = False  # po wygenerowaniu jabłka zakańcza generowanie drugiego
                        self.apple_ex = True  # do spełnienia warunku poniżej (rysuje jabłko)
                        self.apple_generator = 0



        if self.apple_ex == True:
            pygame.draw.rect(self.window, self.apple_color, (self.apple_pos[0], self.apple_pos[1], 50, 50))


    def eat(self):
        if (self.apple_pos[0] == self.snake_pos_x[0]) and (self.apple_pos[1] == self.snake_pos_y[0]):
            self.apple_ex = False # z warunku powyżej, jabłko znika.
            self.apple_check = True # ponownie uruchamia funkcje do generowania jabłka
            self.score += 1
            self.apple()  # pojawienie sie jablka po zjedzeniu ( chyba nie potrzebne )

        if (self.apple_pos[0] == self.snake2_pos_x[0]) and (self.apple_pos[1] == self.snake2_pos_y[0]):
            self.apple_ex = False # z warunku powyżej, jabłko znika.
            self.apple_check = True # ponownie uruchamia funkcje do generowania jabłka
            self.score2 += 1
            self.apple()  # pojawienie sie jablka po zjedzeniu ( chyba nie potrzebne )


    #popracowac nad wartosciami
    def grow_snake(self):
         self.lenght_pyton = len(self.snake_pos_x)
         self.lenght_pyton2 = len(self.snake2_pos_x)
         print(self.lenght_pyton)
         #SNAKE1
         if self.score >= self.lenght_pyton-2:
             x = -50
             y = -50
             self.snake_pos_x.append(x)
             self.snake_pos_y.append(y)

         #SNAKE2
         if self.score2 >= self.lenght_pyton2-1 :
             x = -50
             y = -50
             self.snake2_pos_x.append(x)
             self.snake2_pos_y.append(y)




    def drawing_snakes(self):
        # SNAKE 1
        for num in range(0, self.lenght_pyton):
            pygame.draw.rect(self.window, self.snake_color, (self.snake_pos_x[num], self.snake_pos_y[num], 50, 50))

        # SNAKE 2
        for numm in range(0, self.lenght_pyton2):
            pygame.draw.rect(self.window, self.snake_color2, (self.snake2_pos_x[numm], self.snake2_pos_y[numm], 50, 50))


    def rys(self):
        self.apple()
        self.grow_snake()
        self.eat()
        self.drawing_snakes()
        #print(self.lenght_pyton)


    def crash(self):
        #SNAKE 1
        for x in range(3,self.lenght_pyton):
            if self.snake_pos_x[0] == self.snake_pos_x[x] and self.snake_pos_y[0] == self.snake_pos_y[x]:
                self.game_over = True
        # lose
        for xq in range(1, self.lenght_pyton2):
            if (self.snake_pos_x[0] == self.snake2_pos_x[xq] and self.snake_pos_y[0] == self.snake2_pos_y[xq]):
                self.game_over = True



        #SNAKE2
        for xx in range(3,self.lenght_pyton2):
            if self.snake2_pos_x[0] == self.snake2_pos_x[xx] and self.snake2_pos_y[0] == self.snake2_pos_y[xx]:
                self.game_over2 = True

            #lose
        for qx in range(1, self.lenght_pyton):
            if (self.snake2_pos_x[0] == self.snake_pos_x[qx] and self.snake2_pos_y[0] == self.snake_pos_y[qx]):
                self.game_over2 =True

    def direction_snake(self):
        #SNAKE 1
        if not self.game_over:
            if self.direction == 1:
                self.snake_pos_y[0] -= self.movement
            elif self.direction == 2:
                self.snake_pos_y[0] += self.movement
            elif self.direction == 3:
                self.snake_pos_x[0] -= self.movement
            elif self.direction == 4:
                self.snake_pos_x[0] += self.movement
        #SNAKE 2
        if not self.game_over2:
            if self.direction2 == 1:
                self.snake2_pos_y[0] -= self.movement
            elif self.direction2 == 2:
                self.snake2_pos_y[0] += self.movement
            elif self.direction2 == 3:
                self.snake2_pos_x[0] -= self.movement
            elif self.direction2 == 4:
                self.snake2_pos_x[0] += self.movement


    def dirr(self):
        self.delta += self.clock.tick()/1000.0
        if self.delta > 0.1:
            self.delta = 0

            # głowa przed poruszeniem
            self.head_x = self.snake_pos_x[0]
            self.head_y = self.snake_pos_y[0]
            self.head2_x = self.snake2_pos_x[0]
            self.head2_y = self.snake2_pos_y[0]

            self.crash()
            self.direction_snake()

            #przechodzenie przez sciany
            #SNAKE1
            if self.snake_pos_x[0] >= self.width:
                self.snake_pos_x[0] = 0
            if self.snake_pos_x[0] < 0:
                self.snake_pos_x[0] = self.width
            if self.snake_pos_y[0] >= self.heigh:
                self.snake_pos_y[0] = 0
            if self.snake_pos_y[0] < 0:
                self.snake_pos_y[0] = self.heigh
            #SNAKE2
            if self.snake2_pos_x[0] >= self.width:
                self.snake2_pos_x[0] = 0
            if self.snake2_pos_x[0] < 0:
                self.snake2_pos_x[0] = self.width
            if self.snake2_pos_y[0] >= self.heigh:
                self.snake2_pos_y[0] = 0
            if self.snake2_pos_y[0] < 0:
                self.snake2_pos_y[0] = self.heigh

            #CIAŁO SNAKE 1
            if not self.game_over:
                for number in range(self.lenght_pyton, 1, -1):
                    #print(number)
                    if number-2 !=0:
                        self.snake_pos_x[number - 1] = self.snake_pos_x[number - 2]
                        self.snake_pos_y[number - 1] = self.snake_pos_y[number - 2]
                    if number-2 == 0:
                        self.snake_pos_x[number - 1] = self.head_x
                        self.snake_pos_y[number - 1] = self.head_y

            # CIAŁO SNAKE 2
            if not self.game_over2:
                for numberu in range(self.lenght_pyton2, 1, -1):
                    if numberu-2 !=0:
                        self.snake2_pos_x[numberu - 1] = self.snake2_pos_x[numberu - 2]
                        self.snake2_pos_y[numberu - 1] = self.snake2_pos_y[numberu - 2]
                    if numberu-2 == 0:
                        self.snake2_pos_x[numberu - 1] = self.head2_x
                        self.snake2_pos_y[numberu - 1] = self.head2_y
























