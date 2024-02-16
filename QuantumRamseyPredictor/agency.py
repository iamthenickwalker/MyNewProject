from agency_swarm import Agency
from AgentCreator import AgentCreator
from DataScientist import DataScientist
from RamseyResearcher import RamseyResearcher
from QuantumCEO import QuantumCEO
from ExpertCoder import ExpertCoder

quantum_ceo = QuantumCEO()
ramseyResearcher = RamseyResearcher()
dataScientist = DataScientist()
agentCreator = AgentCreator()
dataScientist = DataScientist()
expertCoder = ExpertCoder()

agency = Agency([quantum_ceo, [quantum_ceo, ramseyResearcher],
 [quantum_ceo, dataScientist],
 [ramseyResearcher, dataScientist],
 [quantum_ceo, agentCreator],
 [quantum_ceo, expertCoder],
 [dataScientist, expertCoder]],
shared_instructions='./agency_manifesto.md')

if __name__ == '__main__':
    agency.demo_gradio()
