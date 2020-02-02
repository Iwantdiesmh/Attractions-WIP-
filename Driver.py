'''driver for the amusement park. Takes the values of each ride and steps through them everyone  'minute' in the program'''
import time
from Attributes import Attraction
rides = []
#1 sec = 1 minute

def create_the_rides():
    '''creates the ride (hardcoded currently) by calling create_the_ride and putting in the parameters'''
    create_the_ride(loadtime=1,duration=5,capacity=5,name="Rollercoaster")

def create_the_ride(loadtime, duration, capacity, name):
    '''checks if any of the values equal zero (because it wont work then) and adds it to the 'rides' list'''
    if loadtime==0 or duration==0 or capacity==0: #need to check for name. Dont know to do it
        raise Exception('no 0 values for input')
    
    ride = Attraction(loadtime, duration, capacity, name)
    rides.append(ride)

def run_the_ride(ride):
    '''puts a person in the ride and then steps'''
    ride.put_someone_in_line(count=1)
    ride.step()

def run_all_rides(spm=1):
    '''calls run_the_ride for every value in the list then sleeps for a in-game minute'''
    for ride in rides:
        run_the_ride(ride)
        ride.stats()
    time.sleep(spm)

def simulation(spm=1, minutes=6):
    '''runs the ride (broken)'''
    create_the_rides()
    for i in range(minutes):
        print()
        print("minutes =", i+1)
        run_all_rides(spm)

if __name__ == "__main__":
        simulation()
