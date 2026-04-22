# this file is fully responsible for making plan from the goal provided by workflow engine and act
# - accordingly to make the steps of goal and return
from ai_agents.planner_agent import generate_plan
from utils.helpers import json_list_load


def make_plan(goal):
    print("Planning ...")

    step_json = generate_plan(goal)
    step_list = json_list_load(step_json)

    return step_list






