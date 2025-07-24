class Avaliacao:
    def __init__(self, cliente, nota):
        if not isinstance(nota, int):
            raise TypeError("Nota deve ser um inteiro")
        if not 1 <= nota <= 5:
            raise ValueError("Nota deve estar entre 1 e 5")
        self.cliente = cliente
        self.nota = nota