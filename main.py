from codigo_secreto import CodigoSecreto
from palpites import CodigoPalpite
from x_and_o import Acertos





# --- Bloco Introdutório do Jogo ---

print("==================================================")
print("       BEM-VINDO AO JOGO DO CÓDIGO SECRETO!")
print("==================================================")
print("\nEu sou a Máquina Pensante, e acabei de gerar um código...")
print("Ele é um código secreto de 4 dígitos. Cada dígito é único")
print("e está entre 1 e 7 (sem repetições!).")
print("\nSua missão, se aceitar, é decifrar esse código!")
print("Você terá um número limitado de tentativas.")
print("A cada palpite, eu darei pistas:")
print("  - x: Dígito correto E na posição certa.")
print("  - o: Dígito correto, mas na posição errada.")
print("_"*50)

input("\ndigite enter para começar: ")

print("_" * 50)
print("\n" * 8)

codigo = CodigoSecreto.gerar()
codigo_list = codigo.codigo

tentativas = 0

while True:

    palpite = CodigoPalpite.gerar()
    palpite_list = palpite.lista_palp

    acertos = Acertos.calcular(codigo_list, palpite_list)

    print("".join(acertos.vetor_acertos))
    
    tentativas += 1

    if acertos.vetor_acertos.count("x") == 4:
        print(f"Parabéns! Você descobriu o código {codigo_list} em {tentativas} tentativas!")
        break

    if tentativas > 12:
        print("vc é bot perdeu kkkkkkkkkk")
        break