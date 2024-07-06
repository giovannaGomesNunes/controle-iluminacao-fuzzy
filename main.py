import regras as reg
import universo_variaveis as universo

if __name__ == "__main__":
    def validar_entrada(numero, limite):
        while True:
            try:
                valor = int(input(numero))
                if 0 <= valor <= limite:
                    return valor
                else:
                    print(f"Insira um valor entre 0 e {limite}")
            except ValueError:
                print("Insira um valor válido.")

    print("Digite valores inteiros de sua preferência:")
    reg.valores.input['luminosidade_natural'] = validar_entrada("Insira a luminosidade natural (em um intervalo de 0 a 100): ", 100)
    reg.valores.input['deteccao_presenca'] = validar_entrada("Insira a deteccao de presenca (em um intervalo de 0 a 100): ", 100)
    reg.valores.input['temperatura_ambiente'] = validar_entrada("Insira a temperatura ambiente (em um intervalo de 0 a 50°C): ", 50)
    reg.valores.input['preferencia_usuarios'] = validar_entrada("Insira a preferencia dos usuarios (em um intervalo de 0 a 100): ", 100)
    reg.valores.input['horario_dia'] = validar_entrada("Insira o horario do dia (0 - manha, 1 - tarde, 2 - noite): ", 2)
    reg.valores.input['nivel_atividade'] = validar_entrada("Insira o nivel de atividade (em um intervalo de 0 a 100): ", 100)
    reg.valores.input['idade_usuarios'] = validar_entrada("Insira a idade dos usuarios (0 - jovem, 1 - adulto, 2 - idoso): ", 2)

    valor_final = reg.valores.compute()
    print(f"Intensidade da iluminação ideal: {reg.valores.output['intensidade_iluminacao']}%")

    universo.intensidade_iluminacao.view(reg.valores)
    universo.luminosidade_natural.view(reg.valores)
    universo.deteccao_presenca.view(reg.valores)
    universo.temperatura_ambiente.view(reg.valores)
    universo.preferencia_usuarios.view(reg.valores)
    universo.horario_dia.view(reg.valores)
    universo.nivel_atividade.view(reg.valores)
    universo.idade_usuarios.view(reg.valores)

    input("Pressione ENTER para finalizar a execução do programa: ")
