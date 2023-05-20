from ICalculatorView import CalculatorView


class View(CalculatorView):
    def __init__(self, label):
        self.label = label

    def printResult(self, result):
        self.label["text"] = 'Ответ: ' + str(result)
        return self.label["text"]

    def displayError(self, message: str):
        self.label["text"] = message
        return self.label["text"]



