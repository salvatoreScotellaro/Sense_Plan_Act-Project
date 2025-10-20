"""
    Class representing the planner used by the robot.
"""

import random

class Planner:
    
    def __init__(self, goal:str) -> None:

        """
            Method to initialize the planner. 

            Args:
                goal (str): string representing the current goal for the robot.
            
            Returns:
                Planner: new instance of the Planner class.
        """

        self._directions = ['left','right','forward','backward']

        self._goal: str = goal
        self._plans = {
            'wonder': [(self.check_battery, self.choose_dir)],
            'go': [(self.check_battery, self.choose_best_dir)],
            'search': [(self.target_reached, 'pick_up'),(lambda perceptions: perceptions['target'],'go'), (self.check_battery,'wonder')]
        }
        self._rules = [(lambda perceptions: perceptions['target'],'go'), (self.check_battery,'wonder')]
    
    def get_plans(self) -> dict:
        """
            Method to get all available plans for the robot.

            Returns:
                plans (dict): dictionary cf plans.
        """

        return self._plans

    def add_plan(self, goal:str, rules:list) -> None:
        """
            Method to add a plan in the to the library of plans

            Args:
                goal (str): string for the goal of the new plan.
                rules (list): list of condition-action rules composing the plan. 
        """
        self._plans[goal] = rules
    
    def compute_random_plan(self, n:int) -> list:
        """
            Method computing a plan as a list of n random condition-action rules.

            Args:
                n (int): integer representing the number of rules in the plan.
            
            Raises:
                TypeError: if n is not an integer.
        """

        if not isinstance(n, int): raise TypeError(f"{n} is not an integer.")  

        return [random.choice(self._rules) for _ in range(n)]

    def compute_subsumption_plan(self, goal:str) -> list:
        """
            Method computing a plan, for a given goal, as list of priority-ordered condition-action rules. 
            Rules are only based only on perceptions just received from the robot. 
            If no plan can be computed, a random plan is returned.

            Args:
                goal (str): string specifying the goal of the plan.
            
            Returns:
                plan (list): list of condition-action rules to be followed from the robot to reach the goal.
        """

        # Check if plan exists in plans' library
        for plan_goal, plan in self._plans.items():
            if goal == plan_goal: return plan

        # If no plan available
        return self.compute_random_plan(2)
    
    def select_action(self, plan:list, perceptions:dict) -> tuple:
        """
            Method that selects an action to perform from the possible condition-actions rules in the given plan. 
            Choice is based on just received perceptions.

            Args:
                plan (list): list of condition-action rules composing the plan to reach the goal.
                perceptions (dict): dictionary of perceptions received by the robot from sensors at last time step.
            
            Returns:
                action (str): string representing action to perform at current time step.
                action_type (str): string denoting the type of the action to be perfomed.
        """
        for (condition, action) in plan:
            if condition(perceptions) and action in self._plans: 
                action = self.select_action(self._plans[action], perceptions)
                if action is not None: return action
            elif condition(perceptions):
                if isinstance(action, str): return action 
                return action(perceptions)
        return None

    def check_battery(self, perceptions:dict) -> bool:
        """
            Method that checks if the battery level is different from zero percent.

            Args:
                perceptions (dict): dictionary of perceptions received by the robot from sensors at last time step.
            
            Returns:
                is_not_empty (bool): True if battery level is different from zero percent, False otherwise.
        """
        return perceptions['battery_level'] != 0
            
    def choose_dir(self, perceptions:dict) -> str:
        """
            Method determining the direction for next move not considering any distance metric to choose.

            Args:
                perceptions (dict): dictionary of perceptions received by the robot from sensors at last time step.
            
            Returns:
                direction (str): string defining the direction for next move of the robot.
        """

        for direction in self._directions:
            if perceptions[direction] == "free": return direction
        return 'trapped'

    def choose_best_dir(self, perceptions:dict) -> str:
        """
            Method determining the direction for next move minimizing manhattan distance to target.
            
            Args:
                perceptions (dict): dictionary of perceptions received by the robot from sensors at last time step.

            Returns:
                direction (str): string defining the direction for next move of the robot.
        """

        x,y = perceptions['position']
        xt,yt = perceptions['target']
        
        distancies = {'left': abs((x-1)-xt) + abs(y-yt),
                    'right': abs((x+1)-xt) + abs(y-yt),
                    'forward': abs(x-xt) + abs((y+1)-yt),
                    'backward': abs(x-xt) + abs((y-1)-yt)}
    
        sorted_directions = sorted(distancies, key=distancies.get, reverse=False)
        for direction in sorted_directions: 
            if perceptions[direction] == 'free': return direction
        return 'trapped'
    
    def target_reached(self, perceptions:dict) -> bool:
        """
            Method determining whether the robot has reached its target or not.
            
            Args:
                perceptions (dict): dictionary of perceptions received by the robot from sensors at last time step.

            Returns:
                reached (bool): True if target is reached, False otherwise.
        """
        if perceptions['target'] is None: return False
        x,y = perceptions['position']
        xt,yt = perceptions['target']
        return abs(x-xt) + abs(y-yt) == 1

if __name__ == "__main__":
    planner = Planner('search')

    # Test get_plans 
    for plan in planner.get_plans(): print(plan)

    # Test add_plan
    planner.add_plan('get_water', [(lambda perceptions: perceptions['in_front'] == 'water', 'take_water')])
    print(planner.get_plans()['get_water'])

    # Test compute_random_plan
    print(planner.compute_random_plan(2))

    # Test compute_subsumption_plan
    plan = planner.compute_subsumption_plan('search') 
    print(plan)
    print(planner.compute_subsumption_plan('get_energy'))

    # Test select_action
    print(planner.select_action(plan, {'battery_level':100, 'position': (10,10), 'left':'blocked', 'right':'free', 'forward':'blocked', 'backward':'blocked', 'target': None}))
    print(planner.select_action(plan, {'battery_level':100, 'position': (10,10), 'left':'blocked', 'right':'free', 'forward':'free', 'backward':'blocked', 'target': (20,10)}))
