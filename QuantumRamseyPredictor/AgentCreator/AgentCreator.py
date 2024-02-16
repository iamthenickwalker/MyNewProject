from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class AgentCreator(Agent):
    def __init__(self):
        super().__init__(
            name="AgentCreator",
            description="Responsible for creating or modifying other agents within the agency to adapt to evolving requirements and refine operational processes. Interfaces with Dynamic Agent Creation Tools to implement changes in agency structure and functionalities.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )
