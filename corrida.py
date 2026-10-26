# Etapa 2 - Corrida Noturna da Ponte Estaiada
# Categorias e tempos-limites em segundos:
CATEGORIAS = {
    ("Juvenil", 1500, 3120),
    ("Adulto", 1320, 2760),
    ("Master", 1500, 3120),
    ("Veterano", 1800, 3780)
}

# Funções da Etapa 1:

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
    nome1= partes[0][:3].upper()
    nome2= partes[-1][:3].upper()
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

    horas = int(tempo[0:2])
    minutos = int(tempo[3:5])
    segundos = int(tempo[6:8])

    if minutos > 59 or segundos > 59:
        return -1

    return horas * 3600 + minutos * 60 + segundos

def calcular_pace(tempo, distancia):
    # Calcula o ritmo médio (pace) do participante:
    segundos_por_km = tempo // distancia

    minutos = segundos_por_km // 60
    segundos = segundos_por_km % 60

    if segundos < 10:
        return str(minutos) + ":0" + str(segundos) + " min/km"
    else:
        return str(minutos) + ":" + str(segundos) + " min/km"

def premiacao(idade, distancia, tempo):
    # Verifica se o corredor atingiu o tempo de premiação:

   if idade < 16 or tempo < 0:
       return "Não"

   categoria = Idade(idade)

   for dados in CATEGORIAS:
       if dados[0] == categoria:
           if distancia == 5:
               limite = dados[1]
           else:
               limite = dados[2]
           return tempo <= limite
   return False
# Novas funções para a etapa 2:

def codigo_unico(nome, idade, codigos_usados):
    # Evita codigos repetidos acrescentando um número ao final do código:
    base = codigo(nome, idade)
    codigo = base
    numero = 2

    while codigo in codigos_usados:
        codigo = base + "-" + str(numero)
        numero += 1
    return codigo

def formatar_tempo(tempo):
    # Converte o tempo em segundos para o formato HH:MM:SS:
    horas = tempo // 3600
    minutos = (tempo % 3600) // 60
    segundos = tempo % 60

    h = str(horas)
    m = str(minutos)
    s = str(segundos)

    if horas < 10:
        h = "0" + h
    if minutos < 10:
        m = "0" + m
    if segundos < 10:
        s = "0" + s

    return h + ":" + m + ":" + s

def buscar_indice(corredores, codigo):
    # Busca um corredor pelo código e retorna sua posição na lista:
    for indice in range(len(corredores)):
        if corredores[indice]["codigo"] == codigo:
            return indice
    return -1

def contar_categorias(corredores):
    # Conta os inscritos de cada categoria:
    contagem ={}

    for dados in CATEGORIAS:
        contagem[dados[0]] = 0

    for corredor in corredores:
        categoria = corredor["categoria"]
        contagem[categoria] += 1

    return contagem

def corredores_com_tempo(corredores):
    # Retorna corredores que já possuem tempo registrado.

    return [corredor for corredor in corredores if corredor["tempo"] != -1]
