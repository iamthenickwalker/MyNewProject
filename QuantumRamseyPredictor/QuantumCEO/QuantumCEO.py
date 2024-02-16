from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class QuantumCEO(Agent):
    def __init__(self):
        super().__init__(
            name="QuantumCEO",
            description="Responsible for overseeing the agency's operations, managing communication between other agents, and interacting with the user for feedback incorporation. The role is crucial for integrating feedback into the predictive model and ensuring seamless operations within the agency.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )
