"""module that sets up each ride and its attributes"""
# pylint: disable=too-many-instance-attributes
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
        self.time = 0
        self.on = True
        self.loading = True
        self.running = False

    def stats(self):
        """tells you each countable statistic"""
        print('line length:', self.line)
        print('people on the ride:', self.in_action)
        print('largest number of people in the line:', self.maxLine)
        print('least number of people in line:', self.minLine)
        if self.on == True:
            print("""---Status---
                  The ride is on""")
        else:
            print("""---Status---
ride is off""")

    def _change_max_min_line(self, humancount):
        """changes the variables self.maxLine and self.minLine to the respective max and min amounts of people inside"""
        if humancount > self.maxLine:
            self.maxLine = humancount
        if humancount < self.minLine:
            self.minLine = humancount
    
    def step(self):
        """checks which mode the cart is in for the attration and decides wether to move it to the next one"""
        if self.on == True:
            if self.line != 0:
                if self.loading == True and self.running == False:
                    self.time = self.time - 1
                    if self.time == 0:
                        self.time = self.duration
                        self.loading = False
                        self.running = True
                        self.in_action = self.in_load
                        self.in_load = 0
                    
                elif self.running == True and self.loading == False:
                    self.time = self.time - 1
                    if self.time == 0:
                        self.time = self.loadtime
                        self.loading = True
                        self.running = False
                        self.in_action = 0
                        if self.line < self.capacity:
                            self.in_load = self.line
                            self.line = 0
                            
                        else:
                            self.line -= self.capacity
                            self.in_action = self.capacity
                    
                else:
                    raise RuntimeError('shouldnt get here')
                
            else:
                if self.loading == True and self.running == False:
                    self.loading = False
                    self.in_load = 0

                else:
                    self.time = self.time - 1
                    if self.time == 0:
                        self.time = self.loadtime
                        self.loading = True
                        self.running = False
                        self.in_action = 0
                        if self.line < self.capacity:
                            self.in_load = self.line
                            self.line = 0
                            
                        else:
                            self.line -= self.capacity
                            self.in_action = self.capacity

    def off(self):
        self.line = 0
        self.on = False
        self.time = 0 #doesn't matter that much

    def run(self):
        self.on = True
        self.loading = True
        self.time = self.loadtime

    
    def put_someone_in_line(self, count=1):
        """add people to the line (self.line)"""
        self.line += int(count)
