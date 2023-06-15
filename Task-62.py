class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def distance(self, time):
        return time * self.speed

class CrawlerRobot(Robot):
    def __init__(self, name, speed, territory):
        super().__init__(name, speed)
        self.territory = territory

class WheelRobot(Robot):
    def __init__(self, name, speed, car_brand):
        super().__init__(name, speed)
        self.car_brand = car_brand

robot = Robot('C3PO', 10)
crawler = CrawlerRobot('Caterpillar', 5, 'NiNo')
cart = WheelRobot('Bucket', 15, 'Toyo')
print(robot.distance(6))
print(crawler.distance(10))
print(cart.distance(4))
print(crawler.territory)
print(cart.car_brand)