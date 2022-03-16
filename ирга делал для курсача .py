# подключаем графическую библиотеку
from tkinter import *
import time
import random
# подключаем модули, которые отвечают за время и случайные числа
#Генерация случайного цвета Hex в Python
r= lambda: random.randint(0,255)
g= lambda: random.randint(0,255)
b= lambda: random.randint(0,255)
c= lambda: random.randint(0,255)
colorfulr=('#%02X%02X%02X' % (r(),r(),r()))
colorfulg=('#%02X%02X%02X' % (g(),g(),g()))
colorfulb=('#%02X%02X%02X' % (b(),b(),b()))
colorfulc=('#%02X%02X%02X' % (c(),c(),c()))

# Описываем класс Ball, который будет отвечать за шарик
class Ball:
    # конструктор
    def __init__(self, canvas, color, paddle, bricks, score):
        # задаём параметры объекта, которые нам передают в скобках в момент создания
        self.bricks = bricks
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.bottom_hit = False
        # свойство, которое отвечает за то, достиг шарик дна или нет. Пока не достиг, значение будет False
        self.hit = 0
        # цвет нужен был для того, чтобы мы им закрасили весь шарик
        # здесь появляется новое свойство id,
        # в котором хранится внутреннее название шарика
        # а ещё командой create_oval мы создаём круг радиусом 15 пикселей и закрашиваем нужным цветом
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color, width=1)
        self.canvas.move(self.id, 230, 461)
        # помещаем шарик в точку с координатами 230,461
        start = [3, 2.8, 2.6, 2.4, 2.2, 2, 1.8, 1.6]
        # задаём список возможных направлений для старта
        random.shuffle(start)
        # выбираем первый из перемешанного — это будет вектор движения шарика
        self.x = start[0]
        self.y = -start[0]
        # в самом начале он всегда падает вниз, поэтому уменьшаем значение по оси y
        self.canvas.move(self.id, self.x, self.y)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        # шарик узнаёт свою высоту и ширину

    # обрабатываем касание блока, для этого получаем 4 координаты шарика в переменной pos (левая верхняя и правая нижняя точки)
    def brick_hit(self, pos):
        for brick_line in self.bricks:
            for brick in brick_line:
                # получаем кординаты блока через объект brick (блок)
                brick_pos = self.canvas.coords(brick.id)
                try:
                    # если координаты касания совпадают с координатами блока
                    if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
                        if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                            self.hit += 1
                            # увеличиваем счёт (обработчик этого события будет описан ниже)
                            self.score.configure(text="Очки: " + str(self.hit))
                            self.canvas.delete(brick.id)
                            # возвращаем метку о том, что мы успешно коснулись
                            return True
                except:
                    continue
        # возвращаем False — касания не было
        return False

    # обрабатываем касание платформы, для этого получаем 4 координаты шарика в переменной pos (левая верхняя и правая нижняя точки)
    def paddle_hit(self, pos):
        # получаем кординаты блока через объект paddle (платформa)
        paddle_pos = self.canvas.coords(self.paddle.id)
        # если координаты касания совпадают с координатами блока
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                # возвращаем метку о том, что мы успешно коснулись
                return True
            # возвращаем False — касания не было
            return False

    # обрабатываем отрисовку шарика
    def draw(self):
        # передвигаем шарик на заданные координаты x и y
        self.canvas.move(self.id, self.x, self.y)
        # запоминаем новые координаты шарика
        pos = self.canvas.coords(self.id)
        # задаём список возможных направлений для старта
        start = [3, 2.8, 2.6, 2.4, 2.2, 2, 1.8, 1.6]
        random.shuffle(start)
        # выбираем  из перемешанного — это будет вектор движения шарика
        if self.brick_hit(pos):
            self.y = start[0]
            # если шарик падает сверху
        if pos[1] <= 0:
            self.y = start[0]
            # если шарик правым нижним углом коснулся дна
        if pos[3] >= self.canvas_height:
            # помечаем это в отдельной переменной
            self.bottom_hit = True
        if pos[0] <= 0:
            # если коснулись левой стенки
            self.x = start[0]
            # если коснулись правой стенки
        if pos[2] >= self.canvas_width:
            self.x = -start[0]
        if self.paddle_hit(pos):
            self.y = -start[0]

# Описываем класс Paddle, который будет отвечать за платформу
class Paddle:
    def __init__(self, canvas, color):
        # canvas означает, что платформа будет нарисована на нашем изначальном холсте
        self.canvas = canvas
        # создаём прямоугольную платформу 10 на 100 пикселей, закрашиваем выбранным цветом и получаем её внутреннее имя
        self.id = self.canvas.create_rectangle(0, 0, 100, 10, fill=color)
        # пока платформа никуда не движется, поэтому изменений по оси х нет
        self.canvas.move(self.id, 200, 485)
        self.x = 0
        # платформа узнаёт свою ширину
        self.canvas_width = self.canvas.winfo_width()
        # задаём обработчик нажатий
        # если стрелка влево — turn_left()
        self.canvas.bind_all("<Left>", self.turn_left)
        # если нажата стрелка вправо — выполняется метод turn_right()
        self.canvas.bind_all("<Right>", self.turn_right)

    def draw(self):
        # метод, который отвечает за движение платформы
        # получаем координаты холста
        pos = self.canvas.coords(self.id)
        # если мы упёрлись в левую границу
        if pos[0] + self.x <= 0:
            # останавливаемся
            self.x = 0
            # если упёрлись в правую границу
        if pos[2] + self.x >= self.canvas_width:
            # останавливаемся
            self.x = 0
        # сдвигаем нашу платформу на заданное количество пикселей
        self.canvas.move(self.id, self.x, 0)

    # движемся влево
    def turn_left(self, event):
        # будем смещаться левее на -3 пикселя по оси х
        self.x = -3

    # движемся вправо
    def turn_right(self, event):
        # будем смещаться правее на 3 пикселя по оси х
        self.x = 3

# Описываем класс Bricks, который будет отвечать за блок
class Bricks:
    def __init__(self, canvas, color):
        # canvas означает, что блок будет нарисован на нашем изначальном холсте
        self.canvas = canvas
        # создаём прямоугольную платформу 25 на 25 пикселей, закрашиваем выбранным цветом и получаем её внутреннее имя
        self.id = self.canvas.create_rectangle(0, 0, 25, 25, fill=color, width=5)



playing = False
#пока playing False игра не начнется и будет покаан только начальный экран
# создаём новый объект — окно с игровым полем. В нашем случае переменная окна называется game, и мы его сделали из класса Tk() — он есть в графической библиотеке tk = Tk()
game = Tk()
# делаем заголовок окна — Игра с помощью свойства объекта title
game.title("Игра")
game.geometry("500x570")
# запрещаем менять размеры окна, для этого используем свойство resizable
game.resizable(0, 0)
# помещаем наше игровое окно выше остальных окон на компьютере, чтобы другие окна не могли его заслонить.
game.wm_attributes("-topmost", 1)
# создаём новый холст — 500 на 500 пикселей, где и будем рисовать игру
canvas = Canvas(game, width=500, height=500, bd=0, highlightthickness=0, highlightbackground=colorfulc, bg=colorfulr)
# говорим холсту, что у каждого видимого элемента будут свои отдельные координаты
canvas.pack(padx=10, pady=10)
#упаковали canvas-холст
score = Label(height=50, width=80, text="Очки: 00", font="Consolas 14 bold")
#строка с счетом
score.pack(side="left")
#упаковали Label-знак
game.update()
#обновили окно


def start_game(event):
    global playing
    if playing is False:
        playing = True
        #playing = True значит игра началась
        score.configure(text="Очки: 00")
        canvas.delete("all")
        #удаляем начальное окно
        BALL_COLOR = [colorfulr, colorfulg, colorfulb, colorfulc]
        #задаем цвет шару
        BRICK_COLOR = [colorfulr, colorfulg, colorfulb, colorfulc]
        #задаем цвет блоку
        random.shuffle(BALL_COLOR)
        #перемешиваем цвета для шара
        paddle = Paddle(canvas, colorfulb)
        #задаем цвет для платформы
        bricks = []
        #создаем массив для блока
        for i in range(0, 5):
            #делаем цикл для блоко 19рядов по 5 линий
            b = []
            for j in range(0, 19):
                random.shuffle(BRICK_COLOR)
                #меремешиваем цвета
                tmp = Bricks(canvas, BRICK_COLOR[0])
                # закрашиваем 19 блоков
                b.append(tmp)
            bricks.append(b)
            #добавляем указаные элементы в конец списка

        for i in range(0, 5):
            for j in range(0, 19):
                canvas.move(bricks[i][j].id, 25 * j, 25 * i)
                #выставляем наши блоки

        ball = Ball(canvas, BALL_COLOR[0], paddle, bricks, score)
        #после того как шар касаеться блока убираем его
        game.update_idletasks()
        #обновляем окно
        game.update()

        time.sleep(1)
        while 1:
            #если шар касается платформы обновляем окно и игра продолжается
            if not ball.bottom_hit:
                ball.draw()
                paddle.draw()
                game.update_idletasks()
                game.update()
                time.sleep(0.01)
            #если шар не касается платформы и падает то выводим текст и останавливаем игру
            else:
                canvas.create_text(250, 250, text="ПРОИГРАЛ!!", fill="red", font="Consolas 24 ")
                game.update_idletasks()
                game.update()
                playing = False
                break


game.bind_all("<Return>", start_game)
#бинидим кнопку Enter что бы игра началась
canvas.create_text(250, 250, text="нажми Enter что бы начать!!", fill=colorfulc, font="Consolas 18")
#создаем лейбл с текстом "нажми Enter что бы начать!!"
game.mainloop()
#необходимо вызывать для окон, которые нужно рисовать