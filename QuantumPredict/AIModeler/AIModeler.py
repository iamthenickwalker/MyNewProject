from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class AIModeler(Agent):
    def __init__(self):
        super().__init__(
            name="AIModeler",
            description="Responsible for developing, implementing, and refining the machine learning model that predicts random numbers with high accuracy. This entails incorporating the insights and patterns identified by the DataAnalyst and integrating feedback mechanisms through Langchain tools to ensure continuous learning and improvement of the prediction model.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )
