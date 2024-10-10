from app.bots.adder import AdderBot
from app.bots.printer import PrinterBot
from app.bots.subtractor import SubtractorBot
from app.bots.multiplier import MultiplierBot

class FactoryBot:

    ADDER = "ADDER"
    PRINTER = "PRINTER"
    # TODO: Implement the other bots
    SUBTRACTOR = "SUBTRACTOR"
    MULTIPLIER = "MULTIPLIER"

    @staticmethod
    def create(bot):
        if bot == FactoryBot.ADDER:
            return AdderBot()
        elif bot == FactoryBot.PRINTER:
            return PrinterBot()
        #TODO: Implement the other bots
        elif bot == FactoryBot.SUBTRACTOR:
            return SubtractorBot()
        elif bot == FactoryBot.MULTIPLIER:
            return MultiplierBot()
        else:
            raise Exception("{bot} not found!")