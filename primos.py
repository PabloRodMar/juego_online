from multiprocessing import Pool

def son_primos(numero):
    if numero < 2:
        return False
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
    return primo

if __name__ == "__main__":
    numeros = [29, 97, 221, 541, 104729, 1234567, 999331, 25, 2, 13]
    with Pool() as pool:
        resultados = pool.map(son_primos, numeros)
    for numero, resultado in zip(numeros, resultados):
        print(f"El número {numero} es", "primo" if resultado else "no primo")