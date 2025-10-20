# Sense-Plan-Act Hierchical Paradigm
In this project the Sense-Plan-Act paradigm is implemented. Then, in this README file a brief and general description of the project is presented, and it is also given a list of the few simple steps necessary to make the project run to test it. 

---

## Project Description
Starting from the discussion of what has been effectively done througout the files, this is just what can be summarized in the following points.

- In the files `robot.py`, `sensor.py`, `planner.py` and `actuator.py` all the modules necessary to represent all the parts of the robot and of the paradigm are implemented. A deeper discussion of these and on their design is given in the apposite `.md` file.

- In the `main.py` file an example of all the modules co-operating is implemented to simulate a robot designed to search for a target. In this case the robot is called `WaterFinder` as the target is supposed to be water in some form. What the robot actually does, then, is always the same sequence of operations at any discrete time step: it senses the surroundings, determines the action to perform depending on the plan it is executing and on the just arrived perceptions, and finally performs the action. Moreover, after any action the battery level of the robot is decreased. The robot stops its search when any of the following conditions is met.
    - The battery is expired.
    - The target has been reached.
    - The robot is blocked and believes to be trapped. This can happen just because the implementation of this example is made just to show the general functioning of the paradigm, but there is no actual model of the world. The perceptions of the walls blocking the robot are extracted randomly at each time step, and so can happen that it perceives a wall on all four available directions. 

---

## How to Run
To run the project just follow the steps in the points here below.

- Start WSL and create a new directory for the project with any name.
- Clone this repository, whose link is https://github.com/salvatoreScotellaro/Sense_Plan_Act-Project.git.
- Call the directory cloned with command `cd Sense_Plan_Activate-Project`.
- Create a new virtual environment with `python3 -m venv venv`.
- Activate the virual environment using `source venv/bin/activate`.
- Install project with required dependencies using `pip install .`.
- Run the main with command `python3 main.py`.

Other than this way, another possibility is use the .zip file provided as delivery of the homework. In this case 
