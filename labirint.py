from pygame import *

class GameSprite(sprite.Sprite):
    # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))

       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
   # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
class Player(GameSprite):
    #метод, в котором реализовано управление спрайтом по кнопкам стрелочкам клавиатуры
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
       # Вызываем конструктор класса (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_y)
        
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self):
        if packman.rect.x <= win_width-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
            self.rect.x += self.x_speed
            platforms_touched = sprite.spritecollide(self, barriers, False)
            
            if self.x_speed > 0: 
                for p in platforms_touched:
                    self.rect.right = min(self.rect.right, p.rect.left)
            elif self.x_speed < 0:
                for p in platforms_touched:
                    self.rect.left = max(self.rect.left, p.rect.right)
        if packman.rect.y <= win_height-80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed
            platforms_touched = sprite.spritecollide(self, barriers, False)

            if self.y_speed > 0:
                for p in platforms_touched:#заподобное слово любой англичанин избьет 
                    self.rect.bottom = min(self.rect.bottom, p.rect.top)
            elif self.y_speed < 0:
                for p in platforms_touched:
                    self.rect.top = max(self.rect.top, p.rect.bottom)
#ПРОДОЛЖИТЬ ЗДЕСЬ    
class Enemy(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        
        self.speed = player_speed
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        
        

#21  class Bullet(GameSprite):
#21      def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
#21       #Вызываем конструктор класса (Sprite):
#21          GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
#21          self.speed = player_speed
#21      def update(self):
#21          self.rect.x += self.speed
#21          # исчезает, если дойдет до края экрана
#21          if self.rect.x > win_width + 10:
#21              self.kill()



#Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_height))
back = (119, 210, 223)#задаем цвет согласно цветовой схеме RGB
#создаем стены картинки
w1 = GameSprite('full1.png',win_width / 2-250, win_height / 2+90, 280, 20)
w2 = GameSprite('full2.png', 370, 100, 20, 130)
w3 = GameSprite('full2.png', 370, 300, 20, 200)
w4 = GameSprite('full1.png',win_width / 2-350, win_height / 2, 280, 20)
w5 = GameSprite('full1.png',win_width / 2-250, win_height / 2-90, 280, 20)
w6 = GameSprite('full1.png', 370, 200, 250, 20)
w7 = GameSprite('full2.png', 460, 200, 20, 220)
barriers = sprite.Group()
barriers.add(w1)
barriers.add(w2)
barriers.add(w3)
barriers.add(w4)
barriers.add(w5)
barriers.add(w6)
barriers.add(w7)

monsters = sprite.Group()
#21 bullets = sprite.Group()

#создаем спрайты
final = GameSprite('final.png',600,400,80,80)
win = GameSprite('win.jpg',0,0,700,500)

packman = Player('hero2.png', 5, win_height - 55, 55, 55, 0, 0)

platforms_touched = sprite.spritecollide(packman, barriers, False)

monster1 = Enemy('enemy.png', win_width - 80, 150, 50, 50, 5)
monster2 = Enemy('enemy.png', win_width - 80, 50, 50, 50, 5)

monsters.add(monster1)
monsters.add(monster2)

finish = False
run = True
while run:
    #цикл срабатывает каждую 0.05 секунд
    time.delay(50)
    window.fill(back)#закрашиваем окно цветом
    barriers.draw(window)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -5
            elif e.key == K_RIGHT:
                packman.x_speed = 5
            elif e.key == K_UP:
                packman.y_speed = -5
            elif e.key == K_DOWN:
                packman.y_speed = 5
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed = 0
            elif e.key == K_UP:
                packman.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0
        packman.reset()
        monster1.reset()
        monster2.reset()
        final.reset()
        
        final.update()
        packman.update()
        monsters.update()

    if not finish:
        #обновляем фон каждую итерацию
        window.fill(back)#закрашиваем окно цветом

        #запускаем движения спрайтов
        packman.update()
        #21 bullets.update()


        #обновляем их в новом местоположении при каждой итерации цикла
        packman.reset()
        #рисуем стены 2
        #w1.reset()
        #w2.reset()
        #21 bullets.draw(window)
        barriers.draw(window)
        final.reset()


        #21 sprite.groupcollide(monsters, bullets, True, True)
        monsters.update()
        monsters.draw(window)
        #21 sprite.groupcollide(bullets, barriers, True, False)


     #Проверка столкновения героя с врагом и стенами
        if sprite.spritecollide(packman, monsters, False):
            finish = True
            #вычисляем отношение
            img = image.load('game_over.png')
            d = img.get_width() // img.get_height()
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))
            run = False

        if sprite.collide_rect(packman, final):
            finish = True
            img = image.load('win.jpg')
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
            run = False
   #рисуем объекты

    
   #включаем движение
    display.update()

while True:
    display.update()
    clock.tick(40)