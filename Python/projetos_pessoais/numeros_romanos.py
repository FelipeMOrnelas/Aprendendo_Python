def bug(romano):
    lista = []
    for n, i in enumerate(romano):
        lista.append(i)

    for i, n in enumerate(lista):
        if lista[i] + lista[i+1] == 'VI':
            continue
        elif lista[i] + lista[i + 1] == 'IV':
            lista.pop(i)
            lista.pop(i)
            lista.insert(i, 'IV')
        elif lista[i] + lista[i + 1] == 'IX':
            lista.pop(i)
            lista.pop(i)
            lista.insert(i, 'IX')
        elif lista[i] + lista[i + 1] == 'XL':
            lista.pop(i)
            lista.pop(i)
            lista.insert(i, 'XL')
        elif lista[i] + lista[i + 1] == 'XC':
            lista.pop(i)
            lista.pop(i)
            lista.insert(i, 'XC')
        elif lista[i] + lista[i + 1] == 'CD':
            lista.pop(i)
            lista.pop(i)
            lista.insert(i, 'CD')
        elif lista[i] + lista[i + 1] == 'CM':
            lista.pop(i)
            lista.pop(i)
            lista.insert(i, 'CM')
    romano = lista
    return romano

def verificar(romano):
    romano_lista = []
    lista_temporaria = []

    for n, i in enumerate(romano):
        romano_lista.append(i)
    for n, i in enumerate(romano_lista):
        if romano_lista[n] == 'I' or romano_lista[n] == 'IV' or romano_lista[n] == 'V' or romano_lista[n] == 'X' or romano_lista[n] == 'L' or romano_lista[n] == 'C' or romano_lista[n] == 'D' or romano_lista[n] == 'M':
            lista_temporaria.append(romano_lista[n])
        else:
            print(f'\nO "{romano_lista[n]}" não é um número romano!')
            print("Excluindo e continuando...")

    romano_lista = lista_temporaria
    return romano_lista

def conversor(romano):
    numero = []
    contador = 0

    for n, i in enumerate(romano):
        numero.append(i)

    repetir = len(numero)
    # numero.append()

    for n, i in enumerate(numero):
        if numero[n] == 'I':
            contador += 1
        elif numero[n] == 'IV':
            contador += 4
        elif numero[n] == 'V':
            contador += 5
        elif numero[n] == 'X':
            contador += 10
        elif numero[n] == 'L':
            contador += 50
        elif numero[n] == 'C':
            contador += 100
        elif numero[n] == 'D':
            contador += 500
        elif numero[n] == 'M':
            contador += 1000
        else:
            print("Errado")
    romano = int(contador)
    return romano

def converter(numero):
    n = []
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    while numero:
        div = numero // num[i]
        numero %= num[i]

        while div:
            n.append(sym[i])
            div -= 1
        i -= 1
    return n

romano = input("Digite o número romano para converter: ")

romano = bug(romano)

verificado_romano = verificar(romano)

contador = conversor(verificado_romano)

numero = int(contador)

correto = converter(numero)

verificado_romano = ''.join(verificado_romano)
correto = ''.join(correto)

if verificado_romano == correto:
    print(f'\nO número {verificado_romano} convertido é: {contador}')
else:
    print(f'\nO formato "{verificado_romano}" não existe')
    print(f'\nSe você quis dizer {correto} então é: {contador}')
