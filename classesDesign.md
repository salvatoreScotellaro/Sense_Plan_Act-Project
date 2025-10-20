## Classes Design

In this file we outline necessary attributes and methods that the classes to implement the sense - plan - act paradigm should have. In particular, as requested in the homework assignment, we design the following four classes.

- **Robot Class**: this is the main class that represents the robot. It represents its physical characteristics, and its state.
- **Sensor Class**: this class represents all the sensors the robot has to retrieve data from the environment.
- **Planner Class**: this class implements the planning abilities of the robot. This means it takes data retrieved from sensors, the state of the robot, and its goal and determines the sequence of actions it should perform.
- **Actuator Class**: this class represents the actuators of the robot. This means that implements each of the possible actions of the robot in concrete operations the robot can physically do.

Given this brief overview of the classes, now they are designed one by one defining for each of them which should be their attributes and methods.

### Robot Class

- **Attributes**:

  - **size**: represents the dimensions of the robot.
  - **weight**: specifies the weight of the robot.
  - **battery Level**: keeps track dynamically of the battery level of the robot.
  - **id**: defines a unique identifier for the robot.
  - **holding**: string defining what the robot is holding. None if the robot holds nothing.

- **Methods**:
  - **init**: default constructor for the class that allows to initialize the robot.
  - **reload_battery**: completely restores the battery level of the robot.
  - **set_battery_level**: method allowing to manually set the battery level of the robot.

### Sensor Class

- **Attributes**:

  - **type**: defines the type of the sensors, and so the kind of data it collects.
  - **range**: defines the maximum range for the sensor to collect the data.
  - **id**: defines a unique identifier for the sensor.
  - **available**: defines if the sensor is believed to be alive or to be no more available.
  - **max_samples**: integer definining the maximum amount of data samples to store for the sensor.

- **Methods**:
  - **init**: default constructor for the class that allows to initialize a sensor.
  - **get_data**: method used to retrieve a specific type of data from all sensors that collect it.
  - **get_all_data**: method used to retrieve all data from all available sensors.
  - **restore_sensor**: method applicable to a sensor to restore its availability.

### Planner Class

- **Attributes**:
  - **goal**: string defining the current goal of the robot.
  - **plans**: a dictionary defining the library of plans for the robot.
  - **actions**: a list of all the actions available to the robot.

- **Methods**:
  - **init**: default constructor for the class that allows to initialize the planner.
  - **get_plans**: method to get all plans currently available to the robot.
  - **add_plan**: method to add a plan to the library of plans of the robot.
  - **compute_random_plan**: method to compute a plan composed by random actions, regardless of the goal.
  - **compute_plan**: method to compute a plan for a given a goal. 

### Actuator Class

- **Attributes**:
  - **motors**: 
  - **servos**: 

- **Methods**:
  - **init**: default constructor for the class that allows to initialize an actuator.
  - **move_forward**: method to make the robot use its actuators to move forward.
  - **turn**: method to make the robot use its actuators to turn in a given direction.
  - **pick_up**: method to make the robot use its actuators to pick up an object in front of him.
  - **put_down**: method to make the robot use its actuators to put_down an object it is holding.