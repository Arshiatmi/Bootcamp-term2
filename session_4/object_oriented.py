class Car:
    def __init__(self, speed=50, MAX_SPEED=200):
        self.speed = speed
        self.MAX_SPEED = MAX_SPEED

    def increase_speed(self, speed):
        self.speed += speed


BMW = Car(speed=50, MAX_SPEED=200)
BENZ = Car(speed=10)
AstonMartin = Car(MAX_SPEED=300)


for i in range(10):
    BMW.increase_speed(20)
    print(BMW.speed)

print(BENZ.speed)
