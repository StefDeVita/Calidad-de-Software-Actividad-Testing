class Calculadora:
    """
    Clase que representa una calculadora básica con operaciones aritméticas.
    """
    def suma(self, a, b):
        """
        Realiza la suma de dos números.
        :param a: Primer número.
        :param b: Segundo número.
        :return: Resultado de la suma.
        """
        return a + b

    def resta(self, a, b):
        """
        Realiza la resta de dos números.
        :param a: Primer número.
        :param b: Segundo número.
        :return: Resultado de la resta.
        """
        return a - b

    def multiplicacion(self, a, b):
        """
        Realiza la multiplicación de dos números.
        :param a: Primer número.
        :param b: Segundo número.
        :return: Resultado de la multiplicación.
        """
        return a * b

    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: División por cero"
