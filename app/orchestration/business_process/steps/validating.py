class StepValidating:

    @staticmethod
    def run(orchestrator, pipeline) -> None:
        if not (
            isinstance(pipeline.lhs, int) and
            isinstance(pipeline.rhs, int) and
            pipeline.lhs > 0 and
            pipeline.rhs > 0
        ):
            raise Exception("Both numbers must be positive integers")
        output = StepValidating.__format_output(pipeline)
        orchestrator.bots.printer.print_output(output)
    
    def __format_output(pipeline):
        return f"{pipeline.step} > {pipeline.lhs} + {pipeline.rhs}"