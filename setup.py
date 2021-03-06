import bricks
import subprocess
import display
import slider
import ball


class setup:
    def __init__(self):

        self.display1 = display.display()
        self.ball1 = ball.ball(34, 61)
        self.slider = slider.slider(35, 57)

    def createlvl1(self):

        self.layout = []
        self.layout.append(bricks.bricklvl1(10, 1))
        self.layout.append(bricks.bricklvl1(10, 6))
        self.layout.append(bricks.bricklvl1(10, 11))
        self.layout.append(bricks.bricklvl1(10, 16))
        self.layout.append(bricks.bricklvl1(10, 21))
        self.layout.append(bricks.bricklvl1(10, 26))
        self.layout.append(bricks.bricklvl1(10, 31))
        self.layout.append(bricks.bricklvl1(10, 36))
        self.layout.append(bricks.bricklvl1(10, 41))
        self.layout.append(bricks.bricklvl1(10, 46))
        self.layout.append(bricks.bricklvl1(10, 51))
        self.layout.append(bricks.bricklvl1(10, 56))
        self.layout.append(bricks.bricklvl1(10, 61))
        self.layout.append(bricks.bricklvl1(10, 66))
        self.layout.append(bricks.bricklvl1(10, 71))
        self.layout.append(bricks.bricklvl1(10, 76))
        self.layout.append(bricks.bricklvl1(10, 81))
        self.layout.append(bricks.bricklvl1(10, 86))
        self.layout.append(bricks.bricklvl1(10, 91))
        self.layout.append(bricks.bricklvl1(10, 96))
        self.layout.append(bricks.bricklvl1(10, 101))
        self.layout.append(bricks.bricklvl1(10, 106))
        self.layout.append(bricks.bricklvl1(10, 111))
        self.layout.append(bricks.bricklvl1(10, 116))
        self.layout.append(bricks.bricklvl3(12, 1))
        self.layout.append(bricks.bricklvl3(12, 6))
        self.layout.append(bricks.bricklvl3(12, 11))
        self.layout.append(bricks.bricklvl3(12, 16))
        self.layout.append(bricks.bricklvl3(12, 21))
        self.layout.append(bricks.bricklvl3(12, 26))
        self.layout.append(bricks.bricklvl3(12, 31))
        self.layout.append(bricks.bricklvl3(12, 36))
        self.layout.append(bricks.bricklvl3(12, 41))
        self.layout.append(bricks.bricklvl3(12, 46))
        self.layout.append(bricks.bricklvl3(12, 51))
        self.layout.append(bricks.bricklvl3(12, 56))
        self.layout.append(bricks.bricklvl3(12, 61))
        self.layout.append(bricks.bricklvl3(12, 66))
        self.layout.append(bricks.bricklvl3(12, 71))
        self.layout.append(bricks.bricklvl3(12, 76))
        self.layout.append(bricks.bricklvl3(12, 81))
        self.layout.append(bricks.bricklvl3(12, 86))
        self.layout.append(bricks.bricklvl3(12, 91))
        self.layout.append(bricks.bricklvl3(12, 96))
        self.layout.append(bricks.brickExp(11, 1))
        self.layout.append(bricks.brickExp(11, 6))
        self.layout.append(bricks.brickExp(11, 11))
        self.layout.append(bricks.brickExp(11, 16))
        self.layout.append(bricks.brickExp(11, 21))
        self.layout.append(bricks.brickExp(11, 26))
        self.layout.append(bricks.brickExp(11, 31))
        self.layout.append(bricks.brickExp(11, 36))
        self.layout.append(bricks.brickExp(11, 41))
        self.layout.append(bricks.brickExp(11, 46))
        self.layout.append(bricks.brickExp(11, 51))
        self.layout.append(bricks.brickExp(11, 56))
        self.layout.append(bricks.brickExp(11, 61))
        self.layout.append(bricks.brickExp(11, 66))
        self.layout.append(bricks.brickExp(11, 71))
        self.layout.append(bricks.brickExp(11, 76))
        self.layout.append(bricks.brickExp(11, 81))
        self.layout.append(bricks.brickExp(11, 86))
        self.layout.append(bricks.brickExp(11, 91))
        self.layout.append(bricks.brickExp(11, 96))
        self.layout.append(bricks.brickExp(11, 101))
        self.layout.append(bricks.brickExp(11, 106))
        self.layout.append(bricks.brickExp(11, 111))
        self.layout.append(bricks.brickExp(11, 116))
        self.layout.append(bricks.bricklvl3(12, 101))
        self.layout.append(bricks.bricklvl3(12, 106))
        self.layout.append(bricks.bricklvl3(12, 111))
        self.layout.append(bricks.bricklvl3(12, 116))
        self.layout.append(bricks.brickfixed(9, 1))
        self.layout.append(bricks.brickfixed(9, 21))
        self.layout.append(bricks.brickfixed(9, 41))
        self.layout.append(bricks.brickfixed(9, 61))
        self.layout.append(bricks.brickfixed(9, 81))
        self.layout.append(bricks.brickfixed(9, 101))
        self.layout.append(bricks.brickfixed(13, 6))
        self.layout.append(bricks.brickfixed(13, 16))
        self.layout.append(bricks.brickfixed(13, 26))
        self.layout.append(bricks.brickfixed(13, 36))
        self.layout.append(bricks.brickfixed(13, 46))
        self.layout.append(bricks.brickfixed(13, 56))
        self.layout.append(bricks.brickfixed(13, 66))
        self.layout.append(bricks.brickfixed(13, 76))
        self.layout.append(bricks.brickfixed(13, 86))
        self.layout.append(bricks.brickfixed(13, 96))
        self.layout.append(bricks.brickfixed(13, 106))
        self.layout.append(bricks.brickfixed(13, 116))
        self.layout.append(bricks.brickRainbow(14, 46))
        self.layout.append(bricks.brickRainbow(14, 51))
        self.layout.append(bricks.brickRainbow(14, 56))
        self.layout.append(bricks.brickRainbow(14, 61))
        self.layout.append(bricks.brickRainbow(14, 66))
        self.layout.append(bricks.brickRainbow(14, 71))
        self.layout.append(bricks.brickRainbow(14, 76))
        self.layout.append(bricks.brickRainbow(14, 81))
        self.layout.append(bricks.brickRainbow(14, 86))
        self.layout.append(bricks.brickRainbow(14, 91))
        self.layout.append(bricks.brickRainbow(14, 96))

        self.display1.createlvl(self.layout)
        self.display1.updateSlider(self.slider)
        self.display1.updateBall(self.display1, self.ball1, 0, 0)

    def createlvl2(self):

        self.layout = []
        self.layout.append(bricks.bricklvl1(10, 1))
        self.layout.append(bricks.bricklvl1(10, 6))
        self.layout.append(bricks.bricklvl1(10, 11))
        self.layout.append(bricks.bricklvl1(10, 16))
        self.layout.append(bricks.bricklvl1(10, 21))
        self.layout.append(bricks.bricklvl1(10, 26))
        self.layout.append(bricks.bricklvl1(10, 31))
        self.layout.append(bricks.bricklvl1(10, 36))
        self.layout.append(bricks.bricklvl1(10, 41))
        self.layout.append(bricks.bricklvl1(10, 46))
        self.layout.append(bricks.bricklvl1(10, 51))
        self.layout.append(bricks.bricklvl1(10, 56))
        self.layout.append(bricks.bricklvl1(10, 61))
        self.layout.append(bricks.bricklvl1(10, 66))
        self.layout.append(bricks.bricklvl1(10, 71))
        self.layout.append(bricks.bricklvl1(10, 76))
        self.layout.append(bricks.bricklvl1(10, 81))
        self.layout.append(bricks.bricklvl1(10, 86))
        self.layout.append(bricks.bricklvl1(10, 91))
        self.layout.append(bricks.bricklvl1(10, 96))
        self.layout.append(bricks.bricklvl1(10, 101))
        self.layout.append(bricks.bricklvl1(10, 106))
        self.layout.append(bricks.bricklvl1(10, 111))
        self.layout.append(bricks.bricklvl1(10, 116))
        self.layout.append(bricks.bricklvl2(12, 1))
        self.layout.append(bricks.bricklvl2(12, 6))
        self.layout.append(bricks.bricklvl2(12, 11))
        self.layout.append(bricks.bricklvl2(12, 16))
        self.layout.append(bricks.bricklvl2(12, 21))
        self.layout.append(bricks.bricklvl2(12, 26))
        self.layout.append(bricks.bricklvl2(12, 31))
        self.layout.append(bricks.bricklvl2(12, 36))
        self.layout.append(bricks.bricklvl2(12, 41))
        self.layout.append(bricks.bricklvl2(12, 46))
        self.layout.append(bricks.bricklvl2(12, 51))
        self.layout.append(bricks.bricklvl2(12, 56))
        self.layout.append(bricks.bricklvl2(12, 61))
        self.layout.append(bricks.bricklvl2(12, 66))
        self.layout.append(bricks.bricklvl2(12, 71))
        self.layout.append(bricks.bricklvl2(12, 76))
        self.layout.append(bricks.bricklvl2(12, 81))
        self.layout.append(bricks.bricklvl2(12, 86))
        self.layout.append(bricks.bricklvl2(12, 91))
        self.layout.append(bricks.bricklvl2(12, 96))
        self.layout.append(bricks.bricklvl2(12, 101))
        self.layout.append(bricks.bricklvl2(12, 106))
        self.layout.append(bricks.bricklvl2(12, 111))
        self.layout.append(bricks.bricklvl2(12, 116))
        self.layout.append(bricks.bricklvl3(14, 1))
        self.layout.append(bricks.bricklvl3(14, 6))
        self.layout.append(bricks.bricklvl3(14, 11))
        self.layout.append(bricks.bricklvl3(14, 16))
        self.layout.append(bricks.bricklvl3(14, 21))
        self.layout.append(bricks.bricklvl3(14, 26))
        self.layout.append(bricks.bricklvl3(14, 31))
        self.layout.append(bricks.bricklvl3(14, 36))
        self.layout.append(bricks.bricklvl3(14, 41))
        self.layout.append(bricks.bricklvl3(14, 46))
        self.layout.append(bricks.bricklvl3(14, 51))
        self.layout.append(bricks.bricklvl3(14, 56))
        self.layout.append(bricks.bricklvl3(14, 61))
        self.layout.append(bricks.bricklvl3(14, 66))
        self.layout.append(bricks.bricklvl3(14, 71))
        self.layout.append(bricks.bricklvl3(14, 76))
        self.layout.append(bricks.bricklvl3(14, 81))
        self.layout.append(bricks.bricklvl3(14, 86))
        self.layout.append(bricks.bricklvl3(14, 91))
        self.layout.append(bricks.bricklvl3(14, 96))
        self.layout.append(bricks.brickExp(13, 46))
        self.layout.append(bricks.brickExp(13, 51))
        self.layout.append(bricks.brickExp(13, 56))
        self.layout.append(bricks.brickExp(13, 61))
        self.layout.append(bricks.brickExp(13, 66))
        self.layout.append(bricks.brickExp(13, 71))
        self.layout.append(bricks.brickExp(13, 76))
        self.layout.append(bricks.brickExp(13, 81))
        self.layout.append(bricks.brickExp(13, 86))
        self.layout.append(bricks.brickExp(13, 91))
        self.layout.append(bricks.brickExp(13, 96))
        self.layout.append(bricks.bricklvl3(14, 101))
        self.layout.append(bricks.bricklvl3(14, 106))
        self.layout.append(bricks.bricklvl3(14, 111))
        self.layout.append(bricks.bricklvl3(14, 116))
        self.layout.append(bricks.brickfixed(9, 1))
        self.layout.append(bricks.brickfixed(9, 21))
        self.layout.append(bricks.brickfixed(9, 41))
        self.layout.append(bricks.brickfixed(9, 61))
        self.layout.append(bricks.brickfixed(9, 81))
        self.layout.append(bricks.brickfixed(9, 101))
        self.layout.append(bricks.brickfixed(15, 6))
        self.layout.append(bricks.brickfixed(15, 16))
        self.layout.append(bricks.brickfixed(15, 26))
        self.layout.append(bricks.brickfixed(15, 36))
        self.layout.append(bricks.brickfixed(15, 46))
        self.layout.append(bricks.brickfixed(15, 56))
        self.layout.append(bricks.brickfixed(15, 66))
        self.layout.append(bricks.brickfixed(15, 76))
        self.layout.append(bricks.brickfixed(15, 86))
        self.layout.append(bricks.brickfixed(15, 96))
        self.layout.append(bricks.brickfixed(15, 106))
        self.layout.append(bricks.brickfixed(15, 116))
        self.layout.append(bricks.brickExp(16, 46))
        self.layout.append(bricks.brickExp(16, 51))
        self.layout.append(bricks.brickExp(16, 56))
        self.layout.append(bricks.brickExp(16, 61))
        self.layout.append(bricks.brickExp(16, 66))
        self.layout.append(bricks.brickExp(16, 71))
        self.layout.append(bricks.brickExp(16, 76))
        self.layout.append(bricks.brickExp(16, 81))
        self.layout.append(bricks.brickExp(16, 86))
        self.layout.append(bricks.brickExp(16, 91))
        self.layout.append(bricks.brickExp(16, 96))

        self.display1.createlvl(self.layout)
        self.display1.updateSlider(self.slider)
        self.display1.updateBall(self.display1, self.ball1, 0, 0)

    def createlvl3(self):

        self.layout = []
        self.layout.append(bricks.bricklvl3(10, 1))
        self.layout.append(bricks.bricklvl3(10, 6))
        self.layout.append(bricks.bricklvl3(10, 11))
        self.layout.append(bricks.bricklvl3(10, 16))
        self.layout.append(bricks.bricklvl3(10, 21))
        self.layout.append(bricks.bricklvl3(10, 26))
        self.layout.append(bricks.bricklvl3(10, 31))
        self.layout.append(bricks.bricklvl3(10, 36))
        self.layout.append(bricks.bricklvl3(10, 41))
        self.layout.append(bricks.bricklvl3(10, 46))
        self.layout.append(bricks.bricklvl3(10, 51))
        self.layout.append(bricks.bricklvl3(10, 56))
        self.layout.append(bricks.bricklvl3(10, 61))
        self.layout.append(bricks.bricklvl3(10, 66))
        self.layout.append(bricks.bricklvl3(10, 71))
        self.layout.append(bricks.bricklvl3(10, 76))
        self.layout.append(bricks.bricklvl3(10, 81))
        self.layout.append(bricks.bricklvl3(10, 86))
        self.layout.append(bricks.bricklvl3(10, 91))
        self.layout.append(bricks.bricklvl3(10, 96))
        self.layout.append(bricks.bricklvl3(10, 101))
        self.layout.append(bricks.bricklvl3(10, 106))
        self.layout.append(bricks.bricklvl3(10, 111))
        self.layout.append(bricks.bricklvl3(10, 116))
        self.layout.append(bricks.bricklvl2(12, 1))
        self.layout.append(bricks.bricklvl2(12, 6))
        self.layout.append(bricks.bricklvl2(12, 11))
        self.layout.append(bricks.bricklvl2(12, 16))
        self.layout.append(bricks.bricklvl2(12, 21))
        self.layout.append(bricks.bricklvl2(12, 26))
        self.layout.append(bricks.bricklvl2(12, 31))
        self.layout.append(bricks.bricklvl2(12, 36))
        self.layout.append(bricks.bricklvl2(12, 41))
        self.layout.append(bricks.bricklvl2(12, 46))
        self.layout.append(bricks.bricklvl2(12, 51))
        self.layout.append(bricks.bricklvl2(12, 56))
        self.layout.append(bricks.bricklvl2(12, 61))
        self.layout.append(bricks.bricklvl2(12, 66))
        self.layout.append(bricks.bricklvl2(12, 71))
        self.layout.append(bricks.bricklvl2(12, 76))
        self.layout.append(bricks.bricklvl2(12, 81))
        self.layout.append(bricks.bricklvl2(12, 86))
        self.layout.append(bricks.bricklvl2(12, 91))
        self.layout.append(bricks.bricklvl2(12, 96))
        self.layout.append(bricks.bricklvl2(12, 101))
        self.layout.append(bricks.bricklvl2(12, 106))
        self.layout.append(bricks.bricklvl2(12, 111))
        self.layout.append(bricks.bricklvl2(12, 116))
        self.layout.append(bricks.bricklvl1(14, 1))
        self.layout.append(bricks.bricklvl1(14, 6))
        self.layout.append(bricks.bricklvl1(14, 11))
        self.layout.append(bricks.bricklvl1(14, 16))
        self.layout.append(bricks.bricklvl1(14, 21))
        self.layout.append(bricks.bricklvl1(14, 26))
        self.layout.append(bricks.bricklvl1(14, 31))
        self.layout.append(bricks.bricklvl1(14, 36))
        self.layout.append(bricks.bricklvl1(14, 41))
        self.layout.append(bricks.bricklvl1(14, 46))
        self.layout.append(bricks.bricklvl1(14, 51))
        self.layout.append(bricks.bricklvl1(14, 56))
        self.layout.append(bricks.bricklvl1(14, 61))
        self.layout.append(bricks.bricklvl1(14, 66))
        self.layout.append(bricks.bricklvl1(14, 71))
        self.layout.append(bricks.bricklvl1(14, 76))
        self.layout.append(bricks.bricklvl1(14, 81))
        self.layout.append(bricks.bricklvl1(14, 86))
        self.layout.append(bricks.bricklvl1(14, 91))
        self.layout.append(bricks.bricklvl1(14, 96))
        self.layout.append(bricks.brickExp(13, 46))
        self.layout.append(bricks.brickExp(13, 51))
        self.layout.append(bricks.brickExp(13, 56))
        self.layout.append(bricks.brickExp(13, 61))
        self.layout.append(bricks.brickExp(13, 66))
        self.layout.append(bricks.brickExp(13, 71))
        self.layout.append(bricks.brickExp(13, 76))
        self.layout.append(bricks.brickExp(13, 81))
        self.layout.append(bricks.brickExp(13, 86))
        self.layout.append(bricks.brickExp(13, 91))
        self.layout.append(bricks.brickExp(13, 96))
        self.layout.append(bricks.bricklvl1(14, 101))
        self.layout.append(bricks.bricklvl1(14, 106))
        self.layout.append(bricks.bricklvl1(14, 111))
        self.layout.append(bricks.bricklvl1(14, 116))
        self.layout.append(bricks.brickfixed(9, 1))
        self.layout.append(bricks.brickfixed(9, 21))
        self.layout.append(bricks.brickfixed(9, 41))
        self.layout.append(bricks.brickfixed(9, 61))
        self.layout.append(bricks.brickfixed(9, 81))
        self.layout.append(bricks.brickfixed(9, 101))
        self.layout.append(bricks.brickfixed(15, 6))
        self.layout.append(bricks.brickfixed(15, 16))
        self.layout.append(bricks.brickfixed(15, 26))
        self.layout.append(bricks.brickfixed(15, 36))
        self.layout.append(bricks.brickfixed(15, 46))
        self.layout.append(bricks.brickfixed(15, 56))
        self.layout.append(bricks.brickfixed(15, 66))
        self.layout.append(bricks.brickfixed(15, 76))
        self.layout.append(bricks.brickfixed(15, 86))
        self.layout.append(bricks.brickfixed(15, 96))
        self.layout.append(bricks.brickfixed(15, 106))
        self.layout.append(bricks.brickfixed(15, 116))
        self.layout.append(bricks.brickExp(16, 46))
        self.layout.append(bricks.brickExp(16, 51))
        self.layout.append(bricks.brickExp(16, 56))
        self.layout.append(bricks.brickExp(16, 61))
        self.layout.append(bricks.brickExp(16, 66))
        self.layout.append(bricks.brickExp(16, 71))
        self.layout.append(bricks.brickExp(16, 76))
        self.layout.append(bricks.brickExp(16, 81))
        self.layout.append(bricks.brickExp(16, 86))
        self.layout.append(bricks.brickExp(16, 91))
        self.layout.append(bricks.brickExp(16, 96))

        self.display1.createlvl(self.layout)
        self.display1.updateSlider(self.slider)
        self.display1.updateBall(self.display1, self.ball1, 0, 0)
    
    def createbosslvl(self):
        self.layout = []
        self.layout.append(bricks.brickRainbow(4, 61))
        self.layout.append(bricks.brickRainbow(4, 65))
        self.layout.append(bricks.brickRainbow(5, 61))
        self.layout.append(bricks.brickRainbow(5, 66))
        self.layout.append(bricks.brickRainbow(5, 71))
        self.layout.append(bricks.brickRainbow(5, 56))
        self.layout.append(bricks.brickRainbow(6, 61))
        self.layout.append(bricks.brickRainbow(6, 66))
        self.layout.append(bricks.brickRainbow(6, 71))
        self.layout.append(bricks.brickRainbow(6, 56))
        self.layout.append(bricks.brickRainbow(7, 66))
        self.layout.append(bricks.brickRainbow(7, 71))
        self.layout.append(bricks.brickRainbow(7, 76))
        self.layout.append(bricks.brickRainbow(7, 61))
        self.layout.append(bricks.brickRainbow(7, 56))
        self.layout.append(bricks.brickRainbow(7, 51))
        self.layout.append(bricks.brickRainbow(8, 66))
        self.layout.append(bricks.brickRainbow(8, 71))
        self.layout.append(bricks.brickRainbow(8, 76))
        self.layout.append(bricks.brickRainbow(9, 71))
        self.layout.append(bricks.brickRainbow(8, 61))
        self.layout.append(bricks.brickRainbow(8, 56))
        self.layout.append(bricks.brickRainbow(9, 56))
        self.layout.append(bricks.brickRainbow(8, 51))
        self.layout.append(bricks.brickfixed(13, 6))
        self.layout.append(bricks.brickfixed(13, 46))
        self.layout.append(bricks.brickfixed(13, 76))
        self.layout.append(bricks.brickfixed(13, 106))

        self.display1.createlvl(self.layout)
        self.display1.updateSlider(self.slider)
        self.display1.updateBall(self.display1, self.ball1, 0, 0)

