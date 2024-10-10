class StepMultiplying:

    @staticmethod
    def run(orchestrator, pipeline) -> None:
        pipeline.result = orchestrator.bots.multiplier.multiply(pipeline.lhs, pipeline.rhs)
        output = StepMultiplying.__format_output(pipeline)
        orchestrator.bots.printer.print_output(output)

    def __format_output(pipeline):
        return f"{pipeline.step} > {pipeline.lhs} * {pipeline.rhs} = {pipeline.result}"