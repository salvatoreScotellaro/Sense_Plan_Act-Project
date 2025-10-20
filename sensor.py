"""
    Class representing the sensors available to the robot.
"""

import random

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
