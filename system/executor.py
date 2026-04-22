# this file executes the steps given through the step_list and take each step from the list
#                   and passes it to the agent to make report according to steps
from ai_agents.executor_agent import generate_report


def execute_steps(step_list, goal):
    print("executing steps...")

    report = f"# Goal: {goal}\n\n"

    for i in range(len(step_list)-1):

        previous_task = step_list[i-1]["task"] if i>0 else ""
        previous_output = step_list[i-1]["expected_output"] if i>0 else ""
        current_task = step_list[i]["task"]
        current_output = step_list[i]["expected_output"]

        section = generate_report(
            previous_task=previous_task,
            previous_output=previous_output,
            current_task=current_task,
            current_output=current_output,
            goal=goal
        )

        report += f"{section}\n"

    return report


