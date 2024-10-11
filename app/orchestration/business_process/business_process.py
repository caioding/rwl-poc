from ...models.pipeline import Pipeline
from .steps import StepStarted, StepAdding, StepDone, StepValidating, StepSubtracting, StepMultiplying
from typing import Any, List

class BusinessProcess:

    STARTED = "Started"
    ADDING = "Adding"
    #TODO: Implement the other steps
    VALIDATING = "Validating"
    SUBTRACTING = "Subtracting"
    MUTIPLYING = "Multiplying"
    DONE = "Done"

    @staticmethod
    def forward(pipeline: Pipeline):
        steps = BusinessProcess.get_steps()
        index = steps.index(pipeline.step)
        pipeline.step = steps[min(index+1, len(steps)-1)]

    @staticmethod
    def get_steps() -> List[str]:
        return [
            BusinessProcess.STARTED,
            BusinessProcess.VALIDATING,
            BusinessProcess.ADDING,
            #TODO: Implement the other steps
            BusinessProcess.SUBTRACTING,
            BusinessProcess.MUTIPLYING,
            BusinessProcess.DONE,
        ]
    
    @staticmethod
    def run(orchestrator, pipeline: Pipeline):
        if pipeline.step == BusinessProcess.STARTED:
            StepStarted.run(orchestrator, pipeline)
            BusinessProcess.forward(pipeline)
        if pipeline.step == BusinessProcess.VALIDATING:
            StepValidating.run(orchestrator, pipeline)
            BusinessProcess.forward(pipeline)
        if pipeline.step == BusinessProcess.ADDING:
            StepAdding.run(orchestrator, pipeline)
            BusinessProcess.forward(pipeline)
        #TODO: Implement the other steps
        if pipeline.step == BusinessProcess.SUBTRACTING:
            StepSubtracting.run(orchestrator, pipeline)
            BusinessProcess.forward(pipeline)
        if pipeline.step == BusinessProcess.MUTIPLYING:
            StepMultiplying.run(orchestrator, pipeline)
            BusinessProcess.forward(pipeline)
        if pipeline.step == BusinessProcess.DONE:
            StepDone.run(orchestrator, pipeline)