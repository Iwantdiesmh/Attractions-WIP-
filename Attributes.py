"""module that sets up each ride and its attributes"""
# pylint: disable=too-many-instance-attributes
import random
class Attraction():
    """main class for the attributes"""
    def __init__(self, loadtime, duration, capacity, name):
        self.loadtime = int(loadtime)
        self.duration = int(duration)
        self.capacity = int(capacity)
        self.line = 0
        self.in_action = 0
        self.in_load = 0
        self.maxLine = 0
        self.minLine = 1000
        self.maxCart = self.minCart = self.capacity
        self.name = name
        self.time = 1
        self.on = True
        self.loading = True
        self.running = False
        self.p = 0
        
    def stats(self):
        """tells you each countable statistic"""
        print()
        print("Ride Name:", self.name)
        print('line length:', self.line)
        print('people on the ride:', self.in_action)
        print("people getting on the ride:", self.in_load)
        print('largest number of people in the line:', self.maxLine)
        print('least number of people in line:', self.minLine)
        if self.on == True:
            print("""---Status---
 The ride is on""")
            if self.loading == True:
                print("""The ride is loading""")
            else:
                print("""The ride is running""")
        else:
            print("""---Status---
ride is off""")

    def _change_max_min_line(self): 
        """changes the variables self.maxLine and self.minLine to the respective max and min amounts of people inside"""
        if self.line > self.maxLine:
            self.maxLine = self.line 
        if self.line  < self.minLine:
            self.minLine = self.line

    def add_percentage(self):
        if self.on == True:
            self.p = random.randint(0, 100)
            if self.line <= 5: #+/0/- ratio -> 90/10/0 | avg = 8.1
                if self.p >= 0 and self.p < 30: #30%
                    self.line += 15
                elif self.p >= 30 and self.p < 48: #18%
                    self.line += 13
                elif self.p >= 48 and self.p < 63: #15%
                    self.line += 10
                elif self.p >= 63 and self.p < 78: #15%
                    self.line += 6
                elif self.p >= 78 and self.p < 90: #12%
                    self.line += 3
                elif self.p >=  90 and self.p <= 100: #10%
                    self.line += 0
                elif self.p >= 101 and self.p < 0: #0%
                    self.line += -3
                elif self.p >= 101 and self.p < 0: #0%
                    self.line += -5
                elif self.p >= 101 and self.p < 0: #0%
                    self.line += -8
                elif self.p >= 101 and self.p < 0: #0%
                    self.line += -13

            elif self.line > 5 and self.line <= 20: #+/0/- ratio -> 79/11/10 | avg = 7.58
                if self.p >= 0 and self.p < 25: #25%
                    self.line += 15
                elif self.p >= 25 and self.p < 40: #15%
                    self.line += 13
                elif self.p >= 40 and self.p < 54: #14%
                    self.line += 10
                elif self.p >= 54 and self.p < 67: #13%
                    self.line += 6
                elif self.p >= 67 and self.p < 79: #12%
                    self.line += 3
                elif self.p >=  79 and self.p < 90: #11%
                    self.line += 0
                elif self.p >= 90 and self.p <= 100: #10%
                    self.line += -3
                elif self.p >= 101 and self.p < 0: #0%
                    self.line += -5
                elif self.p >= 101 and self.p < 0: #0%
                    self.line += -8
                elif self.p >= 101 and self.p < 0: #0%
                    self.line += -13

            elif self.line > 20 and self.line <= 40: #+/0/- ratio -> 63/15/22 | 6.18
                if self.p >= 0 and self.p < 20: #20%
                    self.line += 15
                elif self.p >= 20 and self.p < 35: #15%
                    self.line += 13
                elif self.p >= 35 and self.p < 48: #13%
                    self.line += 10
                elif self.p >= 48 and self.p < 60: #12%
                    self.line += 6
                elif self.p >= 60 and self.p < 63: #3%
                    self.line += 3
                elif self.p >=  63 and self.p < 78: #15%
                    self.line += 0
                elif self.p >= 78 and self.p < 89: #11%
                    self.line += -3
                elif self.p >= 89 and self.p <= 100: #11%
                    self.line += -5
                elif self.p >= 101 and self.p < 0: #0%
                    self.line += -8
                elif self.p >= 101 and self.p < 0: #0%
                    self.line += -13

            elif self.line > 40 and self.line <= 60: #+/0/- ratio -> 54/10/36 | avg 3.4
                if self.p >= 0 and self.p < 13: #13%
                    self.line += 15
                elif self.p >= 13 and self.p < 25: #12%
                    self.line += 13
                elif self.p >= 25 and self.p < 37: #12%
                    self.line += 10
                elif self.p >= 37 and self.p < 48: #11%
                    self.line += 6
                elif self.p >= 48 and self.p < 54: #6%
                    self.line += 3
                elif self.p >=  54 and self.p < 64: #10%
                    self.line += 0
                elif self.p >= 64 and self.p < 75: #11%
                    self.line += -3
                elif self.p >= 75 and self.p < 87: #12%
                    self.line += -5
                elif self.p >= 87 and self.p <= 100: #13%
                    self.line += -8
                elif self.p >= 101 and self.p < 0: #0%
                    self.line += -13

            elif self.line > 60 and self.line <= 80: #+/0/- ratio -> 38/12/50 | avg: 0.29
                if self.p >= 0 and self.p < 10: #10%
                    self.line += 15
                elif self.p >= 10 and self.p < 20: #10%
                    self.line += 13
                elif self.p >= 20 and self.p < 28: #8%
                    self.line += 10
                elif self.p >= 28 and self.p < 34: #6%
                    self.line += 6
                elif self.p >= 34 and self.p < 38: #4%
                    self.line += 3
                elif self.p >=  38 and self.p < 50: #12%
                    self.line += 0
                elif self.p >= 50 and self.p < 61: #11%
                    self.line += -3
                elif self.p >= 61 and self.p < 73: #12%
                    self.line += -5
                elif self.p >= 73 and self.p < 86: #13%
                    self.line += -8
                elif self.p >= 86 and self.p < 100: #14%
                    self.line += -13

            elif self.line > 80 and self.line <= 100: #+/0/- ratio -> 30/10/60 | avg: -1.15
                if self.p >= 0 and self.p < 8: #8%
                    self.line += 15
                elif self.p >= 8 and self.p < 16: #8%
                    self.line += 13
                elif self.p >= 16 and self.p < 22: #6%
                    self.line += 10
                elif self.p >= 22 and self.p < 26: #4%
                    self.line += 6
                elif self.p >= 26 and self.p < 30: #4%
                    self.line += 3
                elif self.p >=  30 and self.p < 40: #10%
                    self.line += 0
                elif self.p >= 40 and self.p < 55: #15%
                    self.line += -3
                elif self.p >= 55 and self.p < 70: #15%
                    self.line += -5
                elif self.p >= 70 and self.p < 85: #15%
                    self.line += -8
                elif self.p >= 85 and self.p < 100: #15%
                    self.line += -13

            elif self.line > 100: #+/0/- ratio -> 26/10/64 | avg: -5.14
                if self.p >= 0 and self.p < 8: #8%
                    self.line += 12
                elif self.p >= 8 and self.p < 16: #8%
                    self.line += 10
                elif self.p >= 16 and self.p < 22: #6%
                    self.line += 6
                elif self.p >= 22 and self.p < 26: #4%
                    self.line += 3
                elif self.p >= 26 and self.p < 30: #10%
                    self.line += 0
                elif self.p >=  30 and self.p < 40: #7%
                    self.line += -3
                elif self.p >= 40 and self.p < 55: #12%
                    self.line += -6
                elif self.p >= 55 and self.p < 70: #15%
                    self.line += -10
                elif self.p >= 70 and self.p < 85: #15%
                    self.line += -15
                elif self.p >= 85 and self.p < 100: #15%
                    self.line += -18

    def step(self): #i simplified the code by a lot
        """checks which mode the cart is in for the attration and decides wether to move it to the next one"""
        assert self.time > 0
        assert bool(self.loading) + bool(self.running) == 1
        if self.on == True:
            self.time = self.time - 1
            if self.time == 0:
                if self.loading == True:
                   self.time = self.duration
                   self.loading = False
                   self.running = True
                   self.in_action = self.in_load
                   self.in_load = 0
                elif self.running == True:
                   self.time = self.loadtime
                   self.loading = True
                   self.running = False
                   self.in_action = 0
                   if self.line < self.capacity:
                       self.in_load = self.line
                       self.line = 0
                   elif self.line == 0:
                        pass
                        
                   else: #self.line >= self.capacity
                        self.line -= self.capacity
                        self.in_load = self.capacity

                else: #self.running and self.loading both equal False/True
                   raise RuntimeError('shouldnt get here')
            
        else: #self.on = False
            self.loading = True
            self.running = False
            self.in_action = 0
            self.in_load = 0
            self.line = 0
            self.action = self.loadtime

        self._change_max_min_line()
        
    def put_someone_in_line(self):
        """add people to the line (self.line)"""
        self.add_percentage()
        self._change_max_min_line()

    def __str__(self):
        return str(self.name)

        
