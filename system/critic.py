from ai_agents.critic_agent import generate_critic
from ai_agents.executor_agent import generate_refine_report
from utils.helpers import json_dict_load


def check_content(report, goal):

    content = report
    count = 0
    while count <3:
        critic_report = generate_critic(content=content,
                                        goal=goal)
        critic_dict = json_dict_load(critic_report)
        print(critic_dict)

        score = critic_dict["score"]
        if score > 7.5:
            break
        else:
            refine_content = generate_refine_report(
                goal=goal,
                content=content,
                feedback_list=critic_dict["issues"]
            )
            content = refine_content
            count +=1

    return content

