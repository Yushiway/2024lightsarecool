import pixelstrip
import board 
from colors import *
import math
import random

class Rainbow(pixelstrip.Animation):
    def fill(self, red, green, blue):
        for x in range(8):
            for y in range(8):
                matrix[x,y] = (red, green, blue, 0)
    def __init__(self):
        matrix.increment = 0
        pixelstrip.Animation.__init__(self)
        # self.color = GREEN
        self.timeout = 0.0
        self.row = 0
    def reset(self, matrix):
        self.timeout = 0.0
    def draw(self, matrix, delta_time):
        if self.is_timed_out():
            matrix.increment = (matrix.increment + .1) % (math.pi*3/2)
            if matrix.increment <= math.pi/2:
                matrix.color = matrix.increment % (math.pi/2)
                self.fill(int(abs(math.cos(matrix.color)*10)), 0, int(abs(math.sin(matrix.color)*10)))
            elif matrix.increment <= math.pi:
                matrix.color = matrix.increment%(math.pi/2)
                self.fill(0, int(abs(math.sin(matrix.color)*10)), int(abs(math.cos(matrix.color)*10)))
            else:
                matrix.color = matrix.increment% (math.pi/2)
                self.fill(int(abs(math.sin(matrix.color)*10)), int(abs(math.cos(matrix.color)*10)), 0)
            self.timeout = 0.001
            matrix.show()



class Coder(pixelstrip.Animation):
    def line(self, x, y, length):
        for i in range(length):
            if x <= matrix.width and x >= 0:
                if y-i >= 0 and y-i <= matrix.height:
                    if i == 0:
                        matrix[x, y-i] = (0, 0, 0, 0)                   
                    if i < length/2 and not i == 0:
                        matrix[x, y-i] = (0, int(abs(0.5*5*math.cos(math.pi*i/(length*0.1)))), 0, 0)
                    if i == length/2:
                        matrix[x, y-i] = (0, 15, 0, 0)
                    if i > length/2:
                        matrix[x, y-i] = (int(abs(0.5*math.cos(math.pi*i/(length*0.1)))), 15, int(abs(0.5*5*math.cos(math.pi*i/(length*0.1)))), 0)
    def __init__(self):
        self.xPos = []
        self.yPos = []
        self.length = []
        self.timeout = 0.0
        self.xPos.append(random.randrange(0, matrix.width-1))
        self.yPos.append(random.randrange(0, matrix.height+7))
        self.length.append(random.randrange(0, 7))
    def reset(self, matrix):
        self.timeout = 0.0

    def draw(self, matrix, delta_time):
        if self.is_timed_out():

            for i in range(matrix.width/3):
                self.xPos.append(random.randrange(0, matrix.width))
                self.yPos.append(random.randrange(0, matrix.height+7))
                self.length.append(random.randrange(1, 8))
            for stuff in range(len(self.xPos)):
                if self.yPos[stuff] >= 0:
                    self.line(self.xPos[stuff], self.yPos[stuff], self.length[stuff])
                    self.yPos[stuff] = self.yPos[stuff] - 1
            self.timeout = 0.1
            matrix.show()

matrix = pixelstrip.PixelStrip(board.D12, width=32, height=8, bpp=4, pixel_order=pixelstrip.GRB, options={pixelstrip.MATRIX_TOP, pixelstrip.MATRIX_LEFT, pixelstrip.MATRIX_COLUMN_MAJOR, pixelstrip.MATRIX_ZIGZAG})
matrix.timeout = 0.7

matrix.animation = Coder()

while True:
    matrix.draw()