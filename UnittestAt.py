'''unittest for attributes.py'''
import unittest
from Attributes import Attraction

class Unittest(unittest.TestCase):
    def test_loading_greater_than_zero(self):          
        at1 = Attraction(loadtime=1, duration=5, capacity=25, name='rollercoaster1')
        at1.line = 5
        at1.in_action = 5
        at1.time = 5
        at1.step()
        self.assertEqual(at1.time, 4)
        self.assertEqual(at1.loadtime, 1)
        self.assertEqual(at1.duration, 5)
        self.assertEqual(at1.capacity, 25)
        self.assertEqual(at1.name, 'rollercoaster1')
        self.assertEqual(at1.line, 5)
        self.assertEqual(at1.in_action, 5)
        self.assertEqual(at1.on, True)
        self.assertEqual(at1.loading, True)
        self.assertEqual(at1.running, False)
    def test_loading_equal_zero(self):
        '''if '''
        at1 = Attraction(loadtime=1, duration=5, capacity=25, name='rollercoaster2')
        at1.line = 5
        at1.in_action = 5
        at1.time = 1
        at1.step()
        self.assertEqual(at1.time, 0)
        self.assertEqual(at1.loadtime, 1)
        self.assertEqual(at1.duration, 5)
        self.assertEqual(at1.capacity, 25)
        self.assertEqual(at1.name, 'rollercoaster2')
        self.assertEqual(at1.line, 5)
        self.assertEqual(at1.in_action, 5)
        self.assertEqual(at1.on, True)
        self.assertEqual(at1.loading, False)
        self.assertEqual(at1.running, True)
            
    def test_running_greater_than_zero(self):
        at1 = Attraction(loadtime=1, duration=5, capacity=25, name='rollercoaster3')
        at1.line = 5
        at1.in_action = 5
        at1.time = 5
        at1.loading = False
        at1.running = True
        at1.step()
        self.assertEqual(at1.time, 4)
        self.assertEqual(at1.loadtime, 1)
        self.assertEqual(at1.duration, 5)
        self.assertEqual(at1.capacity, 25)
        self.assertEqual(at1.name, 'rollercoaster3')
        self.assertEqual(at1.line, 5)
        self.assertEqual(at1.in_action, 5)
        self.assertEqual(at1.on, True)
        self.assertEqual(at1.loading, False)
        self.assertEqual(at1.running, True)
    def test_running_equal_zero(self):
        at1 = Attraction(loadtime=1, duration=5, capacity=25, name='rollercoaster4')
        at1.line = 5
        at1.in_action = 5
        at1.time = 1
        at1.loading = False
        at1.running = True
        at1.step()
        self.assertEqual(at1.time, 0)
        self.assertEqual(at1.loadtime, 1)
        self.assertEqual(at1.duration, 5)
        self.assertEqual(at1.capacity, 25)
        self.assertEqual(at1.name, 'rollercoaster4')
        self.assertEqual(at1.line, 5)
        self.assertEqual(at1.in_action, 5)
        self.assertEqual(at1.on, True)
        self.assertEqual(at1.loading, True)
        self.assertEqual(at1.running, False)        

    def test_off(self):
        at1 = Attraction(loadtime=1, duration=5, capacity=25, name='rollercoaster52')
        at1.line = 5
        at1.in_action = 0
        at1.time = 1
        at1.on = False
        self.assertEqual(at1.time, 0)
        self.assertEqual(at1.loadtime, 1)
        self.assertEqual(at1.duration, 5)
        self.assertEqual(at1.capacity, 25)
        self.assertEqual(at1.name, 'rollercoaster52')
        self.assertEqual(at1.line, 0)
        self.assertEqual(at1.in_action, 0)
        self.assertEqual(at1.on, False)
        self.assertEqual(at1.loading, False)
        self.assertEqual(at1.running, False)
            
unittest.main(verbosity=2)
