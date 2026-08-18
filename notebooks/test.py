def calcular_fibonacci( n ):

    if not type(n)==int:
        return -1

    if n <= 0:
        return -2

    soma = 0
    a = 0
    b = 1
    for termo in range( 1 , n+1 , 1 ):
        
        if termo == 1:
            valor = 0
        elif termo == 2:
            valor = 1
        else:
            valor = a+b
            a = b
            b = valor
        print(f"O termo {n} da sequencia é {valor}")
    
    return soma

print (calcular_fibonacci(10))