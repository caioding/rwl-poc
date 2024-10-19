class StepSubtracting:

    @staticmethod
    def run(orchestrator, pipeline) -> None:
        pipeline.result = orchestrator.bots.subtractor.sub(pipeline.result, 15)
        output = StepSubtracting.__format_output(pipeline)
        orchestrator.bots.printer.print_output(output)
    
    def __format_output(pipeline):
        return f"{pipeline.step} > {pipeline.result + 15} - 15 = {pipeline.result}"