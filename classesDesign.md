## Classes Design

In this file we outline necessary attributes and methods that the classes to implement the sense - plan - act paradigm should have. In particular, as requested in the homework assignment, we design the following four classes.

- **Robot Class**: this is the main class that represents the robot. It represents its physical characteristics, and its state.
- **Sensor Class**: this class represents all the sensors the robot has to retrieve data from the environment.
- **Planner Class**: this class implements the planning abilities of the robot. This means it takes data retrieved from sensors, the state of the robot, and its goal and determines the sequence of actions it should perform.
- **Actuator Class**: this class represents the actuators of the robot. This means that implements each of the possible actions of the robot in concrete operations the robot can physically do.

Given this brief overview of the classes, now they are designed one by one defining for each of them which should be their attributes and methods.

### Robot Class

- **Attributes**:

  - **dimensions**: represents the height and width of the robot.
  - **weight**: specifies the weight of the robot.
  - **battery Level**: keeps track dynamically of the battery level of the robot.
  - **id**: defines a unique identifier for the robot.
  - **name**: string defining a name for the robot.
  - **target_position**: tuple defining the target position x,y for the robot. This is initially None and assumes a value when the robot is able to see the target. Introduced just to implement an example of application of the paradigm.
  - **orientation**: string defining the current orientation of the robot.
  - **sensors**: dictionary of sensors associating to each type of sensor a Sensor object.
  - **actuators**: dictionary of actuators associating to each type of actuator an Actuator object.
  - **planner**: Planner object used by the robot to compute plans, and select actions dynamically.

- **Methods**:
  - **init**: default constructor for the class that allows to initialize the robot.
  - **__str__**: default method to define a string representation of the robot.
  - **reload_battery**: completely restores the battery level of the robot.
  - **set_battery_level**: method allowing to manually set the battery level of the robot.

### Sensor Class

- **Attributes**:

  - **type**: defines the type of the sensors, and so the kind of data it collects.
  - **range**: defines the maximum range for the sensor to collect the data.
  - **id**: defines a unique identifier for the sensor.
  - **available**: defines if the sensor is believed to be alive or to be no more available.
  - **max_samples**: integer definining the maximum amount of data samples to store for the sensor.
  - **position**: tuple defining the position of the sensor, and so also of the robot. This should have been an attribute only of the gps sensor defined as subclass of the sensor class, but in this simple implementation this is avoided.

- **Methods**:
  - **init**: default constructor for the class that allows to initialize a sensor.
  - **__str__**: default method to define a string representation of the robot.
  - **get_data**: method used to retrieve a specific type of data from all sensors that collect it. This is a dummy implementation that simply extracts random numbers.
  - **get_all_data**: method used to retrieve all data from all available sensors. This is a dummy implementation that simply extracts random numbers.
  - **target_visible**: method used to determine if the robot is able to see the target and, in such a case, where it is located. Again, this is introduced just to implement the example application of the paradigm. Moreover, this method should have been a method only of the camera sensors, but also in this case the implementation of subclasses is avoided.
  - **get_directions_state**: method used to determine if each of the possible moving directions is free or blocked by some obstacle. Again, this should have been a method only of cameras or ultra-sounds sensors.
  - **update_position**: method used to update the position of the sensor, and so of the robot, based on the actions planned and performed through actuators. Also this method should have been only for gps sensors.
  - **restore_sensor**: dummy method that restores the availability of a sensors which was no more utilizable.

### Planner Class

- **Attributes**:
  - **goal**: string defining the current goal of the robot.
  - **plans**: a dictionary defining the library of plans for the robot. Each value of this dictionary is a list of tuples that represent condition-action rules.
  - **rules**: a list of all the condition-action rules available to the robot.

- **Methods**:
  - **init**: default constructor for the class that allows to initialize the planner.
  - **get_plans**: method to get all plans currently available to the robot.
  - **add_plan**: method to add a plan to the library of plans of the robot.
  - **compute_random_plan**: method to compute a plan composed by random condition-action rules, regardless of the goal.
  - **compute_subsumption_plan**: method to compute a plan for a given a goal. The plan is defined as for a subsumption architecture, which means that conditions are checked in order and the first verified results in the action performed by the robot.
  - **select_action**: method that given a plan checks in order the conditions and returns the first action for which the condition is verified to be True.
  - **check_battery**: method used to check if the battery level is still greater than 0%. This is used to verify one of the possible conditions for the actions.
  - **choose_dir**: method used the direction when the action to at current time step perform is chosen to be a movement. This simply returns the first direction verified to be free.
  - **choose_best_dir**: method used the direction when the action to at current time step perform is chosen to be a movement. This returns the direction that minimized the manhattan distance from the target.
  - **target_reached**: method used to verify if the target has been reached. This is the condition used to then perform the pick up action.

### Actuator Class

- **Attributes**:
  - **type**: defines the type of the actuator, and so the actions that it can perform.
  - **energy_cost**: defines the amount of energy consumed by the robot to use the actuator.
  - **max_speed**: defines the maximum possible speed that the actuator can reach.
  - **current_speed**: defines the current speed that the actuator is being used at.
  - **max_turning_speed**: defines the maximum possible turning speed that the actuator can reach.
  - **turning_speed**: defines the current turning speed that the actuator is being used at.
  - **holding**: string defining what the robot is holding. None if the robot holds nothing.
  - **is_active**: boolean value defining whether the actuator is being used or not.

- **Methods**:
  - **init**: default constructor for the class that allows to initialize an actuator.
  - **move_forward**: method to make the robot use its actuators to move forward in current orientation with required speed.
  - **turn**: method to make the robot use its actuators to turn in a given direction with required speed.
  - **pick_up**: method to make the robot use its actuators to pick up an object in front of him. This can action can also fail, depending on a random extraction, in which case it is retried.
  - **put_down**: method to make the robot use its actuators to put down an object it is holding. If it is holding nothing the action is not performed and does not consume any energy.