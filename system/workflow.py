# this file takes the goal provided from the user and return the report to main file after accordingly acting
# -

from system.critic import check_content
from system.executor import execute_steps
from system.planner import make_plan


def generate_report(goal):
    print("Started...")

#   pass the goal to planner and return the list of steps
    step_list = make_plan(goal=goal)
    print("plan made:")


#   take the list of steps and pass it to execute each step in executor
    report = execute_steps(step_list=step_list,
                           goal=goal)
    print("report made:")

#   now the raw report made pass to critic to get correction and feedback
    final_content = check_content(report=report,
                                  goal=goal)

    print("Final Report made")
    return final_content



