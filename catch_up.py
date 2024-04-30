from pygame import *

#создай окно игры
window = display.set_mode((700, 500))

clock = time.Clock()

FPS = 120

f1 = 1

f2 = 10

x1 = 200
y1 = 250

x2 = 500
y2 = 250

display.set_caption('Game')
bg = transform.scale(image.load('background.png'),(700, 500))
sp1 = transform.scale(image.load('sprite1.png'),(100, 100))
sp2 = transform.scale(image.load('sprite2.png'),(100, 100))


game = True
while game:
    window.blit(bg, (0, 0))
    window.blit(sp1, (x1, y1))
    window.blit(sp2, (x2, y2))
    key_press = key.get_pressed()
    if key_press[K_UP] and y1 > 1:
        y1 -= f1
    if key_press[K_DOWN] and y1 < 399:
        y1 += f1
    if key_press[K_RIGHT] and x1 < 599:
        x1 += f1
    if key_press[K_LEFT] and x1 > 1:
        if abs(y1 - y2) > 100:
            if abs(x1 - x2) > 100:
                x1 -= f1
    if key_press[K_w] and y2 > 1:
        y2 -= f2
    if key_press[K_a] and x2 > 1:
        if abs(y1 - y2) > 100:
            if abs(x1 - x2) > 100:
                x2 -= f2
    if key_press[K_s] and y2 < 399:
        y2 += f2
    if key_press[K_d] and x2 < 599:
        x2 += f2
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()


#задай фон сцены

#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке\uploads\2020\12\Запись экрана 2020-12-22 в 13.21.04.gif "Закрыть окно"»