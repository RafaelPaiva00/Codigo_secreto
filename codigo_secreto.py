import random
from dataclasses import dataclass

@dataclass
class CodigoSecreto:
    codigo: list  # atributos class

    @staticmethod
    def gerar():
        digitos_possiveis = [str(i) for i in range(1, 8)]  # '1' a '7'
        random.shuffle(digitos_possiveis)
        codigo_gerado = digitos_possiveis[:4]  # Lista
        return CodigoSecreto(codigo=codigo_gerado)