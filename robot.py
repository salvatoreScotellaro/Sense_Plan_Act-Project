"""
    Class representing the physical characteristics of the robot.
"""

id_counter:int = 0

class Robot:
    
    def __init__(self, name:str, dimensions:tuple, weight:float) -> None:

        """
            Method to initialize a robot. 

            Args:
                name (str): string representing the name of the robot.
                dimensions (tuple): tuple in the form (height,width) for the dimensions of the robot.
                weight (float): float representing the weight of the robot.
            
            Returns:
                Robot: new instance of the Robot class.
        """

        global id_counter

        self._id: int = id_counter
        self._name = name
        self._dimensions = dimensions
        self._weight = weight
        self._battery_level = 100

        id_counter += 1

    def __str__(self) -> str:
        height, width = self._dimensions
        return f"Hi! I'm robot {self._name}, and these are my attributes. \n Id: {self._id} \n Height: {height} \n Width: {width} \
                                            \n Weight: {self._weight} \n Battery Level: {self._battery_level} %"
    
    def reload_battery(self) -> None:
        """
            Method to refill the battery of the robot
        """
        self._battery_level = 100

    def set_battery_level(self, battery_percentage:float) -> None:
        """
            Method to set the battery level of the robot to a given percentage value.

            Args:
                battery_percentage (float): float representing the percentage level of the battery.
        """
        self._battery_level = battery_percentage

if __name__ == "__main__":

    # Test initialization and to string
    robot1 = Robot("Primo", (100,10), 34.4)
    robot2 = Robot("Secondo", (200,15), 40.2)
    print(robot1)
    print(robot2)

    # Test set_battery_level
    robot1.set_battery_level(10)
    print(robot1)

    # Test set_battery_level
    robot1.reload_battery()
    print(robot1)
    