lista=[]
def numeroDigitado (x):
    for d in range(0,x+1):
        if d%2 >0:
            print(d)
            lista.append(d)           
    print(sum(lista))
j =int(input('digite um numero : '))
numeroDigitado(j)
