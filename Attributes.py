"""module that sets up each ride and its attributes"""
from time import time

class Attraction():
    """main class for the attributes"""
    def __init__(self, loadtime, duration, capacity, name):
        self.loadtime = int(loadtime)
        self.duration = int(duration)
        self.capacity = int(capacity)
        self.line = 0
        self.in_action = 0
        self.maxLine = 0
        self.minLine = 1000
        self.maxCart = 0
        self.minCart = self.capacity
        self.name = name
        self.time = 0
        self.on = True
        self.loading = True
        self.running = False
        
    def stats(self):
        """tells you each countable statistic"""
        print('line length:', self.line)
        print('people on the ride:', self.inaction)
        print('largest number of people in the line:', self.maxLine)
        print('least number of people in line:', self.minLine)
        if self.on == True:
            print("""---Status---
                  The ride is on""")
        else:
            print("""---Status---
ride is off""")

    def _change_max_min_Line(self, humancount):
        """changes the variables self.maxLine and self.minLine to the respective max and min amounts of people inside"""
        if humancount > self.maxLine:
            self.maxLine = humancount
        if humancount < self.minLine:
            self.minLine = humancount
    
    def step(self):
        """checks which mode the cart is in for the attration and decides wether to move it to the next one"""
        if self.on == True
            if self.loading == True and self.running == False:
                self.time = self.time - 1
                if self.time == 0:
                    self.loading = False
                    self.running = True
                    self.time = self.duration
                
            elif self.running == True and self.loading == False:
                self.time = self.time - 1
                if self.time == 0:
                    self.loading = True
                    self.running = False
                    self.time = self.loadtime
                
            else:
                raise RuntimeError('shouldnt get here')
            
            
    def put_someone_in_line(self, count = 1):
        """add people to the line (self.line)"""
        self.line += int(count)
