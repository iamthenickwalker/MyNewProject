from agency_swarm.agents import Agent


class RamseyResearcher(Agent):
    def __init__(self):
        super().__init__(
            name="RamseyResearcher",
            description="Focuses on Ramsey Theory and additional mathematical frameworks to guide predictive modeling. Responsibilities include theoretical research, identifying relevant mathematical concepts, and collaborating with the DataScientist.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools"
        )
