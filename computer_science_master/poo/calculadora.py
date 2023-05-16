class Calculator:
    def __init__(self, value_a: int = None, value_b: int = None, op: str = None):
        self.__value_a = value_a
        self.__value_b = value_b
        self.__op = op
        self.valid_operators = ['+', '-', '*', '/']

    @property
    def value_a(self) -> int:
        return self.__value_a

    @value_a.setter
    def value_a(self, value_a: int):
        self.__value_a = value_a

    @property
    def value_b(self) -> int:
        return self.__value_b

    @value_b.setter
    def value_b(self, value_b: int):
        self.__value_b = value_b

    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @classmethod
    def test_value(cls, values: list[int]) -> bool:
        import re
        return all([re.match(r'^\d+$', str(value)) for value in values])

    def test_operator(self) -> bool:
        return self.op in self.valid_operators

    def calculate(self) -> int | float:
        match self.op:
            case '+':
                return self.value_a + self.value_b
            case '-':
                return self.value_a - self.value_b
            case '*':
                return self.value_a * self.value_b
            case '/':
                return self.value_a / self.value_b
            case _:
                return 0

    def show(self) -> None:
        print(f'{self.value_a} {self.op} {self.value_b} = {self.calculate()}')

    def capture_information(self) -> None:
        self.value_a = int(input('Digite o primeiro valor: '))
        self.value_b = int(input('Digite o segundo valor: '))
        self.op = input('Digite a operação: ')


if __name__ == '__main__':
    calculator = Calculator()

    while True:
        calculator.capture_information()
        if not calculator.test_value([calculator.value_a, calculator.value_b]):
            print('Digite apenas números inteiros')
            continue
        if not calculator.test_operator():
            print('Digite apenas operadores válidos:', calculator.valid_operators)
            continue
        calculator.show()
        break
