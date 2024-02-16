from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class DataAnalyst(Agent):
    def __init__(self):
        super().__init__(
            name="DataAnalyst",
            description="Tasked with conducting in-depth statistical and mathematical analysis of the dataset of random numbers, identifying potential patterns and insights. This role is integral to providing valuable inputs to the AIModeler agent for the development and refinement of the predictive model.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )
