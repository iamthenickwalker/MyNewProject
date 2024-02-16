from agency_swarm.tools import BaseTool
from pydantic import Field
import statistics

class DataStatisticsTool(BaseTool):
    """Calculates basic statistical measures of a dataset."""
    dataset: list = Field(
        ..., description="A list of numbers representing the dataset."
    )

    def run(self):
        # Calculating statistical measures
        mean = statistics.mean(self.dataset)
        median = statistics.median(self.dataset)
        try:
            mode = statistics.mode(self.dataset)
        except statistics.StatisticsError:
            mode = "No mode (more than one mode)"
        variance = statistics.variance(self.dataset)
        stdev = statistics.stdev(self.dataset)
        
        # Returning the results
        return {
            "Mean": mean,
            "Median": median,
            "Mode": mode,
            "Variance": variance,
            "Standard Deviation": stdev
        }
