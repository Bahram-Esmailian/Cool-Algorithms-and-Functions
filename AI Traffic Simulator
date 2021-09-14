#AI Traffic Simulator created and written by Bahram Esmailian

import time
from sys import stdout
from time import sleep


class TrafficLight(object):
    """ This is a traffic light. Every traffic light has 3 states. Green, Orange, and Red.
        The Green and Red states last 5 time steps and Orange lasts over 1 times time step."""

    def __init__(self, state, position):
        """Initiates a traffic light with a supplied position and starting state"""
        self.p = position
        self.s = state
        self.t = 0 

    def update(self,arr):
        self.t += 1
        if self.s == 'G' and self.t == 5:
            self.s = 'O'
            self.t = 0
        elif self.s == 'O' and self.t == 1:
            self.s = 'R'
            self.t = 0
        elif self.s == 'R' and self.t == 5:
            self.s = 'G'
            self.t = 0

class Car(object):
    """A car which moves through the road array until it reaches another car or a Red/Orange stoplight."""
    
    def __init__(self, position):
        """Initiates a car with the supplied position"""
        self.p = position
        self.s = 'C'

    def update(self, arr):
        if self.p+1 == len(arr):
            self.p = 0
        elif arr[self.p+1] == 'G' or arr[self.p+1] == '':
            self.p +=1


def simulate_traffic(n,arr):
    lights = []
    cars = []
    print(arr)

    for a in range(len(arr)):
        if arr[a] == 'C':
            cars = [Car(a)] + cars
        elif arr[a] == 'G':
            lights.append(TrafficLight('G',a))
        elif arr[a] == 'O':
            lights.append(TrafficLight('O',a))
        elif arr[a] == 'R':
            lights.append(TrafficLight('R',a))

    for i in range(n):
        for j in range(len(arr)):
            arr[j] = ''
        for light in lights:
            light.update(arr)
            arr[light.p] = light.s
        for car in cars:
            car.update(arr)
            arr[car.p] = car.s
        road_str = ''
        for k in arr:
            if k == '':
                road_str = road_str + '.'
            else:
                road_str = road_str + k
        stdout.write('\r%s' % road_str)
        stdout.flush()
        sleep(.5)

#create a map of the road in the form ['C','','R','O','G'], where C is a car, empty '' is an empty space,
#'R' is a red light, O is an orange/yellow light, and G is a green light
#NOTE: The red and green lights last 5 time increments and the orange light lasts 1 time increment
#NOTE: Cars cannnot stack on top of each other, they will stop behind the closest car to their right (towards increasing road map index)
#enter the number of time increments you want to simulate in the first function argument
simulate_traffic(1000,['C','C','','R'])
