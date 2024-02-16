from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class ExpertCoder(Agent):
    def __init__(self):
        super().__init__(
            name="ExpertCoder",
            description="This agent is tasked with applying Ramsey Theory and other mathematical concepts to the datasets in order to predict the next number within a range of 0-36. It is also responsible for refining the mathematical models over time for improved prediction accuracy. The ExpertCoder should utilize machine learning and mathematical libraries, such as TensorFlow, PyTorch, NumPy, and SciPy, to analyze data and train models. A crucial part of this agent's role is also to implement continuous integration tools for automating the update of models, ensuring that the agency's predictive capabilities evolve over time.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )
