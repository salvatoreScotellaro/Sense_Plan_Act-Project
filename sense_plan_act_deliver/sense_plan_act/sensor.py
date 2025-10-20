"""
    Class representing the sensors available to the robot.
"""

import random
import numpy as np

id_counter:int = 0

class Sensor:
    
    def __init__(self, type:str, range:float, max_samples:int) -> None:

        """
            Method to initialize a robot. 

            Args:
                type (str): string representing the type of the sensor.
                range (float): float representing the range of the sensor.
                max_samples (int): integer representing maximum number of samples in memory.
            
            Returns:
                Sensor: new instance of the Sensor class.
        """

        global id_counter

        self._id: int = id_counter
        self._type = type
        self._range = range
        self._max_samples = max_samples
        self._available = True
        self._position = (0,0) # Initial position for the sensors and for the robot

        self._directions = ['left', 'right', 'forward', 'backward']

        id_counter += 1

    def __str__(self) -> str:
        return f"This is a {self._type} sensor. Sensor's id is: {self._id} and range is: {self._range}"
    
    def get_data(self, data_samples:int) -> list:
        """
            Method to get data from the sensor.

            Args:
                data_samples (int): integer representing the number of data samples to retrieve.

            Returns:
                data (list): list containing values of collected data.
        """
        return [random.uniform(1,100) for _ in range(data_samples)]

    def get_all_data(self) -> None:
        """
            Method to get data all the data from the sensor.

            Args:
                data_samples (int): integer representing the number of data samples to retrieve.

            Returns:
                data (list): list containing values of collected data.
        """

        return [random.uniform(1,100) for _ in range(self._max_samples)]
    
    def target_visible(self) -> tuple:
        """
            Method determining if the target is visible and which is its position.

            Returns:
                is_visible (bool): boolean determining if the target is visible or not.
                position (tuple): tuple representing x,y position of the target.
        """
        is_visible = True if np.random.binomial(1, 0.1) == 1 else False
        target_position = (25,20) if is_visible else None

        return is_visible, target_position
    
    def get_directions_state(self) -> dict:
        """
            Method determining for each possible movement direction whether it is free or blocked.

            Returns:
                directions_state (dict): dictionary associating to each direction either 'free' or 'blocked' state.
        """
        states = ['free','blocked']
        return {direction: states[np.random.binomial(1,0.2)]  for direction in self._directions}

    def get_position(self) -> tuple:
        """
            Method determining the position of the robot.

            Returns:
                position (tuple): x,y position for the robot.
        """
        return self._position
    
    def update_position(self, direction:str) -> None:
        """
            Method to update the position of the robot depending on the direction.
        """
        x,y = self._position
        if direction == 'forward': self._position = x,y+1
        elif direction == 'right': self._position = x+1,y
        elif direction == 'left': self._position = x-1,y
        else: self._position = x,y-1

    def restore_sensor(self) -> None:
        """
            Method to restore the availability of a sensor.
        """

        self._available = True

if __name__ == "__main__":

    # Test initialization and to string
    sensor1 = Sensor("Temperatura", 100.0, 30)
    sensor2 = Sensor("Pressione", 90.0, 50)
    print(sensor1)
    print(sensor2)

    # Test get_data
    data = sensor1.get_data(10)
    print(data)

    # Test get_all_data
    all_data = sensor1.get_all_data()
    print(all_data)

    # Test restore_sensor
    sensor1._available = False
    print(sensor1._available)
    sensor1.restore_sensor()
    print(sensor1._available)
