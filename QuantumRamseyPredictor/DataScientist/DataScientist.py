from agency_swarm.agents import Agent


class DataScientist(Agent):
    def __init__(self):
        super().__init__(
            name="DataScientist",
            description="Responsible for data preprocessing, pattern recognition, and implementing predictive models based on insights from the RamseyResearcher. Works with datasets to develop high-accuracy predictive models.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools"
        )
