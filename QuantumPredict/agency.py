from agency_swarm import Agency
from AIModeler import AIModeler
from DataAnalyst import DataAnalyst
from QuantumCEO import QuantumCEO

quantum_ceo = QuantumCEO()
data_analyst = DataAnalyst()
ai_modeler = AIModeler()

agency = Agency([quantum_ceo, [quantum_ceo, data_analyst],
                 [quantum_ceo, ai_modeler],
                 [data_analyst, ai_modeler]],
                shared_instructions='./agency_manifesto.md')

if __name__ == '__main__':
    agency.demo_gradio()