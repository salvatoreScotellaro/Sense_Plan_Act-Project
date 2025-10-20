from sense_plan_act.robot import Robot
from sense_plan_act.sensor import Sensor
from sense_plan_act.planner import Planner
from sense_plan_act.actuator import Actuator

if __name__ == "__main__":    
    
    # Initialize sensors
    sensors = {
        'position': Sensor('position', 1.0, 10),
        'camera': Sensor('camera', 0.0, 1),
        'ultra_sound': Sensor('ultra_sound', 100.0, 10),
        'temperature': Sensor('camera', 10.0, 5),
        'battery_level': Sensor('battery_level', 0.0, 1)
    }

    # Initialize actuators
    actuators = {
        'motor': Actuator('motor', 10.0, 2.0, 1.0),
        'gripper': Actuator('gripper', 2.0, 1.0, 0.2),
        'servo': Actuator('servo', 3.0, 3.0, 0.5)
    }

    # Initialize planner with initial goal
    goal = 'search'
    planner = Planner(goal)

    # Initialize robot 
    robot = Robot('WaterFinder', (1.5, 0.3), 20, sensors, actuators, planner)

    # Simulate Sense-Plan-Act for some time-steps. At each time step:
    #   1. Get data from sensors.
    #   2. Compute next action to perform through planner.
    #   3. Execute action with actuators.
    # When target is reached, battery expires or the robot is trapped stop.
    water_found = False
    trapped = False
    while robot._battery_level > 0 and not water_found and not trapped:

        # Get all sensors data
        sensors_data = {type: sensor.get_all_data() for type, sensor in robot._sensors.items()}
        sensors_data['battery_level'] = robot._battery_level

        # Determine visibility and position of the target
        camera = robot._sensors['camera']
        water_is_visible, water_position = camera.target_visible()
        robot._target_position = water_position if water_is_visible else robot._target_position
        
        # Determine for each direction whether there are obstacles or not
        directions_state = camera.get_directions_state()

        # Add camera info to perceptions
        sensors_data['target'] = robot._target_position
        for direction, state in directions_state.items(): sensors_data[direction] = state

        # Add position to perceptions
        gps_sensor = robot._sensors['position']
        sensors_data['position'] = gps_sensor.get_position()

        # Determine next action according to plan and perceptions
        plan = robot._planner.compute_subsumption_plan(goal)
        next_action = robot._planner.select_action(plan, sensors_data)

        # Perform action
        if next_action:
            if next_action == robot._orientation: 
                motor = robot._actuators['motor']
                consumed_energy = motor.move_forward(1.0)
                gps_sensor.update_position(robot._orientation)

            elif next_action in ['forward','left','right','backward']:
                servo = robot._actuators['servo']
                consumed_energy = servo.turn(next_action, 1.0)
                robot._orientation = next_action

            elif next_action == 'pick_up':
                gripper = robot._actuators['gripper']
                outcome, consumed_energy = gripper.pick_up('water')
                water_found = outcome

            elif next_action == 'trapped': 
                trapped = True 
                consumed_energy = 0.0

        robot.set_battery_level(robot._battery_level - consumed_energy)
        sensors_data = {}

    print(f"Robot position: {gps_sensor._position}")
    print(f"Water position: {robot._target_position}")
    print(f"Robot is trapped: {trapped}")
    print(f"Robot battery percentage: {robot._battery_level}")




