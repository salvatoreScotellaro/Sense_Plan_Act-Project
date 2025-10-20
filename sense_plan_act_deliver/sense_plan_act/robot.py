"""
    Class representing the physical characteristics of the robot.
"""

from sense_plan_act.planner import Planner

id_counter:int = 0

class Robot:
    
    def __init__(self, name:str, dimensions:tuple, weight:float, sensors:list, actuators:list, planner:Planner) -> None:

        """
            Method to initialize a robot. 

            Args:
                name (str): string representing the name of the robot.
                dimensions (tuple): tuple in the form (height,width) for the dimensions of the robot.
                weight (float): float representing the weight of the robot.
                sensors (dict): dictionary of Sensor objects representing sensors of the robot.
                actuators (dict): dictionary of Actuator objects representing actuators of the robot.
                planner (Planner): planner object that allows robot to plan.
            
            Returns:
                Robot: new instance of the Robot class.
        """

        global id_counter

        self._id: int = id_counter
        self._name = name
        self._dimensions = dimensions
        self._weight = weight
        self._battery_level = 100 # Initial battery level in %

        self._target_position = None # Initially unknown target position
        self._orientation = 'forward' # Initial orientation of the robot

        self._sensors = sensors
        self._actuators = actuators
        self._planner = planner

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

    # Test held_object
    print(robot1.held_object())
    