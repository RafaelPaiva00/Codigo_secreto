from codigo_secreto import CodigoSecreto
from palpites import CodigoPalpite
from dataclasses import dataclass

@dataclass
class Acertos:
    vetor_acertos: list

    @staticmethod
    def calcular(codigo_list, palpite_list):
        # Inicialização
        vetor_verificacao = [False, False, False, False]
        vetor_acertos = ["", "", "", ""]

        for i in range(4):
            if palpite_list[i] == codigo_list[i]:
                vetor_verificacao[i] = True
                vetor_acertos[i] = "x"  

        for i in range(4):
            if vetor_acertos[i] == "":
                for j in range(4):
                    if not vetor_verificacao[j] and palpite_list[i] == codigo_list[j]:
                        vetor_acertos[i] = "o"
                        vetor_verificacao[j] = True
                        break
                    
        return Acertos(vetor_acertos=vetor_acertos)

