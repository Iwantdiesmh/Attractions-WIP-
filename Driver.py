'''driver for the amusement park. Takes the values of each ride and steps through them everyone  'minute' in the program'''
import time
import random
from Attributes import Attraction
rides = []
#1 sec = 1 minute

def create_the_rides():
    '''creates the ride (hardcoded currently) by calling create_the_ride and putting in the parameters'''
    create_the_ride(loadtime=2,duration=5,capacity=12,name="Rollercoaster") #1
    create_the_ride(loadtime=2,duration=5,capacity=25,name="Rollercoaster number 2") #2
    create_the_ride(loadtime=1,duration=5,capacity=30,name="Carousel") #3
    create_the_ride(loadtime=15,duration=10,capacity=60,name="Peter the Pan") #4
    create_the_ride(loadtime=1,duration=2,capacity=10,name="Drop Tower") #5
    create_the_ride(loadtime=1,duration=1,capacity=1,name="Pizza Hut") #6
    create_the_ride(loadtime=3,duration=5,capacity=40,name="Gravity Swing(?)") #7
    create_the_ride(loadtime=1,duration=3,capacity=4,name="Buzz Light year") #8
    create_the_ride(loadtime=5,duration=6,capacity=20,name="Slightly smaller than average mermaids") #9
    create_the_ride(loadtime=1,duration=1,capacity=1,name="Hot Dogs") #10
    
def create_the_ride(loadtime, duration, capacity, name):
    '''checks if any of the values equal zero (because it wont work then) and adds it to the 'rides' list'''
    if loadtime==0 or duration==0 or capacity==0: #need to check for name. Dont know to do it
        raise Exception('no 0 values for input')

    ride = Attraction(loadtime, duration, capacity, name)
    rides.append(ride)

def run_the_ride(ride):
    '''puts a person ithe ride a
nd then steps'''
    ride.put_someone_in_line()
    ride.step()

def run_all_rides(spm=1):
    '''calls run_the_ride for every value in the list then sleeps for a in-game minute'''
    for ride in rides:
        run_the_ride(ride)
        #ride.stats()
    time.sleep(spm)
    
def simulation(spm=1, minutes=10000):
    '''runs the ride (broken)'''
    create_the_rides()
    for i in range(minutes):
        #print("--------------------------------------------------------------------------------------------------")
        #print("minutes =", i+1)
        run_all_rides(spm=0)
    for ride in rides:
        ride.stats()
        
if __name__ == "__main__":
        simulation()

