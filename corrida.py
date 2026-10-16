def primeiro_nome(nome):
    # Retorna o primeiro nome do participante:
    partes = nome.strip().split()
    primeiro_nome = partes[0]
    return  primeiro_nome

def Idade(idade):
    # Categoria de idade:
    if idade <=19 :
        return "Juvenil"
    elif idade <=39 :
        return "Adulto"
    elif idade <=59 :
        return "Master"
    else:
        return "Veterano"

def calculo_valor(distancia, lote, idade):
    # Calculo do valor da inscrição:
    if lote == 1:
        valor= 80
    else:
        valor = 100
    if distancia == 10:
        valor += 20
    if idade >=60:
        valor = valor/2

    return valor

def codigo(nome, idade):
    # Gera o código do participante:
    partes = nome.strip().split()
    nome1= partes[0:3].upper()
    nome2= partes[-1:3].upper()
    return nome1 + nome2 + str(idade)



def converter_tempo(tempo):
    # Converte o tempo para segundos:
    if len(tempo) !=8:
        return -1

    if tempo[2] != ':' or tempo[5] != ':':
        return -1

    for caractere in tempo:
        if caractere not in "0123456789:":
            return -1

    horas = tempo[0:2]
    minutos = tempo[3:5]
    segundos = tempo[6:8]

    if minutos > 59 or segundos > 59:
        return -1

    return horas * 3600 + minutos * 60 + segundos

def calcular_pace(tempo, distancia):
    # Calcula o ritmo médio (pace) do participante:
    segundos_por_km = tempo // distancia

    minutos = segundos_por_km // 60
    segundos = segundos_por_km % 60

    if segundos < 10:
        return str(minutos) + ":0" + str(segundos) + "min/km"
    else:
        return str(minutos) + ":" + str(segundos) + "min/km"

def premiacao(idade, distancia, tempo):
    # Verifica se o corredor atingiu o tempo de premiação:

    categoria = Idade(idade)

    if categoria == "Juvenil" or categoria == "Master":
        if distancia == 5:
            limite = 1500
        else:
            limite = 3120
    elif categoria == "Adulto":
        if distancia == 5:
            limite = 1320
        else:
            limite = 2760
    else:
        if distancia == 5:
            limite = 1800
        else:
            limite = 3780

    if tempo <= limite:
        return "Sim"
    else:
        return "Não"
    
def ler_numero(mensagem, tipo):
    # Solicita um número válido de acordo com o tipo.
    while True:
        entrada = input(mensagem)
        valido = True

        if entrada == "":
            valido = False

        for  caractere in entrada:
            if caractere not in "0123456789":
                valido = False
        if valido:
            numero = int(entrada)

            if tipo == "idade":
                if numero >=0:
                    return numero
            elif tipo == "distancia":
                if numero == 5 or numero == 10:
                    return numero
            elif tipo == "lote":
                if numero == 1 or numero == 2:
                    return numero
            elif tipo == "menu":
                if numero >=1 and numero <=3:
                    return numero
        else:
            print("Valor inválido. Tente novamente.")
