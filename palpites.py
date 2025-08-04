from dataclasses import dataclass

@dataclass
class CodigoPalpite:
    lista_palp: list  # Lista de caracteres

    @staticmethod
    def gerar():
        while True:
            palpite = input("Digite aqui a sua tentativa: ")
            lista_palp = list(palpite)
            tamanho_palp = len(lista_palp)

            if tamanho_palp != 4 or not palpite.isdigit():
                print("Digite sua tentativa com as devidas regras!!!")
                continue

            erro = False
            for i in range(4):
                if int(lista_palp[i]) not in range(0, 8):  # De 0 a 7
                    erro = True
                    break

            if len(set(lista_palp)) != len(lista_palp):
                erro = True

            if erro:
                print("Digite sua tentativa com as devidas regras!!!")
                continue
            else:
                return CodigoPalpite(lista_palp=lista_palp)
