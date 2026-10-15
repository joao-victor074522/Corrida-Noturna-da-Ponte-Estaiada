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

def Calculo_valor(distancia, lote, idade):
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
