#!/usr/bin/env python
import sys
from designing_unique_crews_and_agents.crew import DesigningUniqueCrewsAndAgentsCrew
from designing_unique_crews_and_agents.crew import DesignCrew
# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'type': '2',
        'market_data_url': 'sample_value',
        'research_focus': 'sample_value'
    }
    first_value = list(inputs.values())[0]

    if first_value == "1":
        print(f"hello type1 {first_value}")
        DesigningUniqueCrewsAndAgentsCrew().crew().kickoff(inputs=inputs)

    elif first_value == "2":
        print(f"hello type2 {first_value}")

        inputs = {
            'market_data_url': 'trial 2',
            'research_focus': 'akki'
        }
        DesignCrew().crew().kickoff(inputs=inputs)
    else:
        print("hello type3 wrong value")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'market_data_url': 'sample_value',
        'research_focus': 'sample_value'
    }
    try:
        DesigningUniqueCrewsAndAgentsCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        DesigningUniqueCrewsAndAgentsCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'market_data_url': 'sample_value',
        'research_focus': 'sample_value'
    }
    try:
        DesigningUniqueCrewsAndAgentsCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
