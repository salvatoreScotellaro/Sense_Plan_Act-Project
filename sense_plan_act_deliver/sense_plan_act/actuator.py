"""
    Class representing an actuator used by the robot to perform actions.
"""

import random

class Actuator:
    
    def __init__(self, type:str, max_speed:float, max_turning_speed:float, energy_cost:float) -> None:

        """
            Method to initialize an actuator. 

            Args:
                type (str): string representing the type of the actuator.
                max_speed (float): float representing the max speed the actuator can reach.
                energy_cors (float): float representing the energy cost for the usage of the actuator.
                is_active (bool): boolean denoting if the actuator is active or not.
            
            Returns:
                Actuator: new instance of the Actuator class.
        """
        
        self._type = type
        self._energy_cost = energy_cost

        self._max_speed = max_speed
        self._current_speed = 0.0 # Initial speed is zero

        self._max_turning_speed = max_turning_speed
        self._current_turning_speed = 0.0 # Initial turning speed is zero

        self._holding = None # Initally robot holds nothing
        self.is_active = False # Initially the actuator is not active
    
    def move_forward(self, speed:float) -> float:
        """
            Method to make the actuator move forward.

            Args:
                speed (float): speed requested for the movement.

            Returns:
                energy_consumed (float): energy consumed to perform the operation.
        """

        self._current_speed = speed if speed < self._max_speed else self._max_speed
        print(f"Moving forward at speed {self._current_speed}.")

        return self._energy_cost
        
    def turn(self, direction:str, speed:float) -> tuple:
        """
            Method to make the actuator turn in a requested direction and with a given speed.

            Args:
                direction (str): direction in which the robot will end its rotation.
                speed (float): speed requested for the movement.

            Returns:
                energy_consumed (float): energy consumed to perform the operation.
        """
        
        self._current_turning_speed = speed if speed < self._max_turning_speed else self._max_turning_speed
        print(f"Turning {direction} at speed {self._current_turning_speed}.")

        return self._energy_cost

    def pick_up(self, object:str) -> tuple:
        """
            Method to make the robot pick objects from the environment.

            Args:
                object (str): string representing the object to pick.

            Returns:
                result (tuple): tuple in the form (outcome,energy_consumed). Outcome is True if operation carried out successfully, and False otherwise.
        """
        success = random.choice([True, False])
        print(f"Picking up {object} from the environment.")
        if success: 
            self._holding = object
            print(f"Operation completed successfully. Now holding {object}")
        else: print(f"Operation failed, retry.")
        
        return (success, self._energy_cost)

    def put_down(self) -> float:
        """
            Method to make the robot put down objects picked from the environment.

            Returns:
                energy_consumed (float): energy consumed to perform the operation.
        """

        if self._holding is None: 
            energy_consumed = 0.0
            print(f"Nothing to put down. Operation skipped.")
        else: 
            energy_consumed = self._energy_cost
            print(f"Put down {self._holding} completed.")
            self._holding = None
        
        return energy_consumed
    
    def held_object(self) -> str:
        """
            Method to retrive the string representing the object held by the robot.
        """
        return self._holding
    
if __name__ == "__main__":
    
    # Initialize actuators
    motor = Actuator('motor', 10.0, 2.0, 10.0)
    gripper = Actuator('gripper', 2.0, 1.0, 2.0)
    servo = Actuator('servo', 3.0, 3.0, 5.0)

    # Test move_forward
    print(motor.move_forward(4.0))

    # Test turn
    print(servo.turn('right', 30.0))

    # Test pick_up 
    print(gripper.pick_up('pen'))

    # Test put_down
    print(gripper.put_down())
    print(gripper.put_down())


