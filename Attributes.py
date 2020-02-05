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
        self.time = 1
        self.on = True
        self.loading = True
        self.running = False

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

    def add_percentage():
        pass
    
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
                       self._change_max_min_line()
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
            self. _change_max_min_line()
            self.action = self.loadtime
                      
    def put_someone_in_line(self, count=1):
        """add people to the line (self.line)"""
        if self.on == True:
            self.line += int(count)
            self._change_max_min_line()

        else: #change some day
            print("Cant get in line; this ride is closed")
