from agency_swarm.tools import BaseTool
from pydantic import BaseModel, Field
import subprocess
import os
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CIIntegrationTool(BaseTool):
    """This tool enables continuous integration and deployment of machine learning models."""
    integration_details: str = Field(
        default="Automates CI/CD workflows including checking for new commits, running unit tests, and deployment.",
        description="Detailed description of the continuous integration workflow to be automated."
    )
    test_command: list = Field(
        default=["pytest"],
        description="Command to run unit tests."
    )
    deploy_command: list = Field(
        default=["./deploy.sh"],
        description="Command to run for deployment."
    )

    def run(self) -> str:
        try:
            # Pull the latest changes from the repository
            logging.info("Pulling latest changes from the repository...")
            subprocess.run(["git", "pull"], check=True)

            # Run unit tests
            logging.info("Running unit tests...")
            subprocess.run(self.test_command, check=True)

            # Deploy the latest version
            logging.info("Deploying the latest version...")
            subprocess.run(self.deploy_command, check=True)

            logging.info("Deployment successful.")
            return "Deployment successful."
        except subprocess.CalledProcessError as e:
            error_msg = f"An error occurred during {e.cmd}: {e}"
            logging.error(error_msg)
            return error_msg

# Example usage
if __name__ == "__main__":
    ci_tool = CIIntegrationTool()
    result = ci_tool.run()
    print(result)

