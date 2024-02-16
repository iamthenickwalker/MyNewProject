from agency_swarm.tools import BaseTool
from pydantic import BaseModel, Field
import numpy as np
from scipy import linalg
import json

class NumPySciPyTool(BaseTool):
    computation_details: str = Field(..., description="JSON-formatted details about the computation.")

    def run(self) -> str:
        try:
            # Parse computation details from JSON string
            details = json.loads(self.computation_details)
            operation = details['operation']
            data = details.get('data', {})

            # Map operation to method
            operation_method = getattr(self, f"_{operation}", None)
            if operation_method and callable(operation_method):
                result = operation_method(**data)
                return f"Operation {operation} completed successfully. Result: {result}"
            else:
                return "Unsupported operation."
        except Exception as e:
            return f"Error during computation: {str(e)}"

    def _matrix_inverse(self, matrix):
        A = np.array(matrix)
        return linalg.inv(A).tolist()

    def _solve_linear_system(self, A, b):
        A = np.array(A)
        b = np.array(b)
        return linalg.solve(A, b).tolist()

# Example usage with detailed operation specification
details = {
    "operation": "solve_linear_system",
    "data": {
        "A": [[1, 2], [3, 4]],
        "b": [5, 6]
    }
}
tool = NumPySciPyTool(computation_details=json.dumps(details))
result = tool.run()
print(result)
