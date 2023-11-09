import turtle
import time
import random

delay = 0.1
# Pencereyi oluştur
wn = turtle.Screen()
wn.title("Yılan Oyunu")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Ekran güncellemesini kapat

# Yılan başlangıç pozisyonu
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Yemek başlangıç pozisyonu
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Yılanın vücudu
segments = []

# Yılanın hareket etme fonksiyonları
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Hareket fonksiyonlarını tuşlara bağla
wn.listen()
wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_left, "a")
wn.onkey(go_right, "d")

# Yılanın hareket fonksiyonu
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Ana oyun döngüsü
while True:
    wn.update()

    # Yılanın kendine çarpmasını kontrol et
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        # Segmentleri temizle
        for segment in segments:
            segment.goto(1000, 1000)

        # Segment listesini temizle
        segments.clear()

    # Yemek yendiyse
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Yeni segment ekle
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Yılanın vücudunu güncelle
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Yılanın kendine çarpmasını kontrol et
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            # Segmentleri temizle
            for segment in segments:
                segment.goto(1000, 1000)

            # Segment listesini temizle
            segments.clear()

    time.sleep(delay)
