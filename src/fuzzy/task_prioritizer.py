import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np

class TaskPrioritizer:

    CLASSIFICATION = {
        'lowest': 0,
        'low': 1,
        'medium': 2,
        'high': 3,
        'highest': 4 
    }

    def __init__(self):
        relevancy = ctrl.Antecedent(np.arange(0, 5, 1), 'relevancy')
        impact = ctrl.Antecedent(np.arange(0, 5, 1), 'impact')
        complexity = ctrl.Antecedent(np.arange(0, 5, 1), 'complexity')
        priority = ctrl.Consequent(np.arange(0, 11, 1), 'priority')

        relevancy.automf(names=['lowest', 'low', 'medium', 'high', 'highest'])
        impact.automf(names=['lowest', 'low', 'medium', 'high', 'highest'])
        complexity.automf(names=['lowest', 'low', 'medium', 'high', 'highest'])

        priority['lowest'] = fuzz.trimf(priority.universe, [0, 1, 2])
        priority['low'] = fuzz.trimf(priority.universe, [1, 3, 4])
        priority['medium'] = fuzz.trimf(priority.universe, [2, 4, 6])
        priority['high'] = fuzz.trimf(priority.universe, [4, 6, 8])
        priority['highest'] = fuzz.trimf(priority.universe, [7, 9, 10])

        rules = [
            ctrl.Rule(relevancy['lowest'] & impact['lowest'] & complexity['lowest'], priority['low']),
            ctrl.Rule(relevancy['lowest'] & impact['lowest'] & complexity['low'], priority['lowest']),
            ctrl.Rule(relevancy['lowest'] & impact['lowest'] & complexity['medium'], priority['lowest']),
            ctrl.Rule(relevancy['lowest'] & impact['lowest'] & complexity['high'], priority['lowest']),
            ctrl.Rule(relevancy['lowest'] & impact['lowest'] & complexity['highest'], priority['lowest']),
            ctrl.Rule(relevancy['lowest'] & impact['low'] & complexity['lowest'], priority['low']),
            ctrl.Rule(relevancy['lowest'] & impact['low'] & complexity['low'], priority['low']),
            ctrl.Rule(relevancy['lowest'] & impact['low'] & complexity['medium'], priority['low']),
            ctrl.Rule(relevancy['lowest'] & impact['low'] & complexity['high'], priority['lowest']),
            ctrl.Rule(relevancy['lowest'] & impact['low'] & complexity['highest'], priority['lowest']),
            ctrl.Rule(relevancy['lowest'] & impact['medium'] & complexity['lowest'], priority['low']),
            ctrl.Rule(relevancy['lowest'] & impact['medium'] & complexity['low'], priority['low']),
            ctrl.Rule(relevancy['lowest'] & impact['medium'] & complexity['medium'], priority['low']),
            ctrl.Rule(relevancy['lowest'] & impact['medium'] & complexity['high'], priority['low']),
            ctrl.Rule(relevancy['lowest'] & impact['medium'] & complexity['highest'], priority['low']),
            ctrl.Rule(relevancy['lowest'] & impact['high'] & complexity['lowest'], priority['medium']),
            ctrl.Rule(relevancy['lowest'] & impact['high'] & complexity['low'], priority['medium']),
            ctrl.Rule(relevancy['lowest'] & impact['high'] & complexity['medium'], priority['low']),
            ctrl.Rule(relevancy['lowest'] & impact['high'] & complexity['high'], priority['low']),
            ctrl.Rule(relevancy['lowest'] & impact['high'] & complexity['highest'], priority['low']),
            ctrl.Rule(relevancy['lowest'] & impact['highest'] & complexity['lowest'], priority['medium']),
            ctrl.Rule(relevancy['lowest'] & impact['highest'] & complexity['low'], priority['medium']),
            ctrl.Rule(relevancy['lowest'] & impact['highest'] & complexity['medium'], priority['medium']),
            ctrl.Rule(relevancy['lowest'] & impact['highest'] & complexity['high'], priority['medium']),
            ctrl.Rule(relevancy['lowest'] & impact['highest'] & complexity['highest'], priority['low']),
            ctrl.Rule(relevancy['low'] & impact['lowest'] & complexity['lowest'], priority['low']),
            ctrl.Rule(relevancy['low'] & impact['lowest'] & complexity['low'], priority['low']),
            ctrl.Rule(relevancy['low'] & impact['lowest'] & complexity['medium'], priority['low']),
            ctrl.Rule(relevancy['low'] & impact['lowest'] & complexity['high'], priority['lowest']),
            ctrl.Rule(relevancy['low'] & impact['lowest'] & complexity['highest'], priority['lowest']),
            ctrl.Rule(relevancy['low'] & impact['low'] & complexity['lowest'], priority['low']),
            ctrl.Rule(relevancy['low'] & impact['low'] & complexity['low'], priority['low']),
            ctrl.Rule(relevancy['low'] & impact['low'] & complexity['medium'], priority['low']),
            ctrl.Rule(relevancy['low'] & impact['low'] & complexity['high'], priority['low']),
            ctrl.Rule(relevancy['low'] & impact['low'] & complexity['highest'], priority['low']),
            ctrl.Rule(relevancy['low'] & impact['medium'] & complexity['lowest'], priority['medium']),
            ctrl.Rule(relevancy['low'] & impact['medium'] & complexity['low'], priority['medium']),
            ctrl.Rule(relevancy['low'] & impact['medium'] & complexity['medium'], priority['low']),
            ctrl.Rule(relevancy['low'] & impact['medium'] & complexity['high'], priority['low']),
            ctrl.Rule(relevancy['low'] & impact['medium'] & complexity['highest'], priority['low']),
            ctrl.Rule(relevancy['low'] & impact['high'] & complexity['lowest'], priority['medium']),
            ctrl.Rule(relevancy['low'] & impact['high'] & complexity['low'], priority['medium']),
            ctrl.Rule(relevancy['low'] & impact['high'] & complexity['medium'], priority['medium']),
            ctrl.Rule(relevancy['low'] & impact['high'] & complexity['high'], priority['medium']),
            ctrl.Rule(relevancy['low'] & impact['high'] & complexity['highest'], priority['low']),
            ctrl.Rule(relevancy['low'] & impact['highest'] & complexity['lowest'], priority['high']),
            ctrl.Rule(relevancy['low'] & impact['highest'] & complexity['low'], priority['medium']),
            ctrl.Rule(relevancy['low'] & impact['highest'] & complexity['medium'], priority['medium']),
            ctrl.Rule(relevancy['low'] & impact['highest'] & complexity['high'], priority['medium']),
            ctrl.Rule(relevancy['low'] & impact['highest'] & complexity['highest'], priority['medium']),
            ctrl.Rule(relevancy['medium'] & impact['lowest'] & complexity['lowest'], priority['low']),
            ctrl.Rule(relevancy['medium'] & impact['lowest'] & complexity['low'], priority['low']),
            ctrl.Rule(relevancy['medium'] & impact['lowest'] & complexity['medium'], priority['low']),
            ctrl.Rule(relevancy['medium'] & impact['lowest'] & complexity['high'], priority['low']),
            ctrl.Rule(relevancy['medium'] & impact['lowest'] & complexity['highest'], priority['low']),
            ctrl.Rule(relevancy['medium'] & impact['low'] & complexity['lowest'], priority['medium']),
            ctrl.Rule(relevancy['medium'] & impact['low'] & complexity['low'], priority['medium']),
            ctrl.Rule(relevancy['medium'] & impact['low'] & complexity['medium'], priority['low']),
            ctrl.Rule(relevancy['medium'] & impact['low'] & complexity['high'], priority['low']),
            ctrl.Rule(relevancy['medium'] & impact['low'] & complexity['highest'], priority['low']),
            ctrl.Rule(relevancy['medium'] & impact['medium'] & complexity['lowest'], priority['medium']),
            ctrl.Rule(relevancy['medium'] & impact['medium'] & complexity['low'], priority['medium']),
            ctrl.Rule(relevancy['medium'] & impact['medium'] & complexity['medium'], priority['medium']),
            ctrl.Rule(relevancy['medium'] & impact['medium'] & complexity['high'], priority['medium']),
            ctrl.Rule(relevancy['medium'] & impact['medium'] & complexity['highest'], priority['low']),
            ctrl.Rule(relevancy['medium'] & impact['high'] & complexity['lowest'], priority['high']),
            ctrl.Rule(relevancy['medium'] & impact['high'] & complexity['low'], priority['medium']),
            ctrl.Rule(relevancy['medium'] & impact['high'] & complexity['medium'], priority['medium']),
            ctrl.Rule(relevancy['medium'] & impact['high'] & complexity['high'], priority['medium']),
            ctrl.Rule(relevancy['medium'] & impact['high'] & complexity['highest'], priority['medium']),
            ctrl.Rule(relevancy['medium'] & impact['highest'] & complexity['lowest'], priority['high']),
            ctrl.Rule(relevancy['medium'] & impact['highest'] & complexity['low'], priority['high']),
            ctrl.Rule(relevancy['medium'] & impact['highest'] & complexity['medium'], priority['high']),
            ctrl.Rule(relevancy['medium'] & impact['highest'] & complexity['high'], priority['medium']),
            ctrl.Rule(relevancy['medium'] & impact['highest'] & complexity['highest'], priority['medium']),
            ctrl.Rule(relevancy['high'] & impact['lowest'] & complexity['lowest'], priority['medium']),
            ctrl.Rule(relevancy['high'] & impact['lowest'] & complexity['low'], priority['medium']),
            ctrl.Rule(relevancy['high'] & impact['lowest'] & complexity['medium'], priority['low']),
            ctrl.Rule(relevancy['high'] & impact['lowest'] & complexity['high'], priority['low']),
            ctrl.Rule(relevancy['high'] & impact['lowest'] & complexity['highest'], priority['low']),
            ctrl.Rule(relevancy['high'] & impact['low'] & complexity['lowest'], priority['medium']),
            ctrl.Rule(relevancy['high'] & impact['low'] & complexity['low'], priority['medium']),
            ctrl.Rule(relevancy['high'] & impact['low'] & complexity['medium'], priority['medium']),
            ctrl.Rule(relevancy['high'] & impact['low'] & complexity['high'], priority['medium']),
            ctrl.Rule(relevancy['high'] & impact['low'] & complexity['highest'], priority['low']),
            ctrl.Rule(relevancy['high'] & impact['medium'] & complexity['lowest'], priority['high']),
            ctrl.Rule(relevancy['high'] & impact['medium'] & complexity['low'], priority['medium']),
            ctrl.Rule(relevancy['high'] & impact['medium'] & complexity['medium'], priority['medium']),
            ctrl.Rule(relevancy['high'] & impact['medium'] & complexity['high'], priority['medium']),
            ctrl.Rule(relevancy['high'] & impact['medium'] & complexity['highest'], priority['medium']),
            ctrl.Rule(relevancy['high'] & impact['high'] & complexity['lowest'], priority['high']),
            ctrl.Rule(relevancy['high'] & impact['high'] & complexity['low'], priority['high']),
            ctrl.Rule(relevancy['high'] & impact['high'] & complexity['medium'], priority['high']),
            ctrl.Rule(relevancy['high'] & impact['high'] & complexity['high'], priority['medium']),
            ctrl.Rule(relevancy['high'] & impact['high'] & complexity['highest'], priority['medium']),
            ctrl.Rule(relevancy['high'] & impact['highest'] & complexity['lowest'], priority['high']),
            ctrl.Rule(relevancy['high'] & impact['highest'] & complexity['low'], priority['high']),
            ctrl.Rule(relevancy['high'] & impact['highest'] & complexity['medium'], priority['high']),
            ctrl.Rule(relevancy['high'] & impact['highest'] & complexity['high'], priority['high']),
            ctrl.Rule(relevancy['high'] & impact['highest'] & complexity['highest'], priority['high']),
            ctrl.Rule(relevancy['highest'] & impact['lowest'] & complexity['lowest'], priority['medium']),
            ctrl.Rule(relevancy['highest'] & impact['lowest'] & complexity['low'], priority['medium']),
            ctrl.Rule(relevancy['highest'] & impact['lowest'] & complexity['medium'], priority['medium']),
            ctrl.Rule(relevancy['highest'] & impact['lowest'] & complexity['high'], priority['medium']),
            ctrl.Rule(relevancy['highest'] & impact['lowest'] & complexity['highest'], priority['low']),
            ctrl.Rule(relevancy['highest'] & impact['low'] & complexity['lowest'], priority['high']),
            ctrl.Rule(relevancy['highest'] & impact['low'] & complexity['low'], priority['medium']),
            ctrl.Rule(relevancy['highest'] & impact['low'] & complexity['medium'], priority['medium']),
            ctrl.Rule(relevancy['highest'] & impact['low'] & complexity['high'], priority['medium']),
            ctrl.Rule(relevancy['highest'] & impact['low'] & complexity['highest'], priority['medium']),
            ctrl.Rule(relevancy['highest'] & impact['medium'] & complexity['lowest'], priority['high']),
            ctrl.Rule(relevancy['highest'] & impact['medium'] & complexity['low'], priority['high']),
            ctrl.Rule(relevancy['highest'] & impact['medium'] & complexity['medium'], priority['high']),
            ctrl.Rule(relevancy['highest'] & impact['medium'] & complexity['high'], priority['medium']),
            ctrl.Rule(relevancy['highest'] & impact['medium'] & complexity['highest'], priority['medium']),
            ctrl.Rule(relevancy['highest'] & impact['high'] & complexity['lowest'], priority['highest']),
            ctrl.Rule(relevancy['highest'] & impact['high'] & complexity['low'], priority['high']),
            ctrl.Rule(relevancy['highest'] & impact['high'] & complexity['medium'], priority['high']),
            ctrl.Rule(relevancy['highest'] & impact['high'] & complexity['high'], priority['high']),
            ctrl.Rule(relevancy['highest'] & impact['high'] & complexity['highest'], priority['high']),
            ctrl.Rule(relevancy['highest'] & impact['highest'] & complexity['lowest'], priority['highest']),
            ctrl.Rule(relevancy['highest'] & impact['highest'] & complexity['low'], priority['highest']),
            ctrl.Rule(relevancy['highest'] & impact['highest'] & complexity['medium'], priority['highest']),
            ctrl.Rule(relevancy['highest'] & impact['highest'] & complexity['high'], priority['high']),
            ctrl.Rule(relevancy['highest'] & impact['highest'] & complexity['highest'], priority['high'])
        ]

        self.control_system = ctrl.ControlSystem(rules)
        self.simulation = ctrl.ControlSystemSimulation(self.control_system)


    def convert_classification_to_int(self, classification: str) -> int:
        return self.CLASSIFICATION.get(classification)


    def convert_value_to_classification(self, value: float) -> str:
        if value >= 0 and value <= 2:
            return 'lowest'
        elif value >= 2 and value <= 4:
            return 'low'
        elif value >= 4 and value <= 6:
            return 'medium'
        elif value >= 6 and value <= 8:
            return 'high'
        elif value >= 8 and value <= 9:
            return 'highest'    


    def set_priority(self, relevancy: str, impact: str, complexity: str) -> str:
        self.simulation.input['relevancy'] = self.convert_classification_to_int(relevancy)
        self.simulation.input['impact'] = self.convert_classification_to_int(impact)
        self.simulation.input['complexity'] = self.convert_classification_to_int(complexity)
        self.simulation.compute()
        return self.convert_value_to_classification(self.simulation.output['priority'])
