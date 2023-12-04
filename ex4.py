def somar_elementos(lista):
    try:
        # Tenta somar os elementos da lista
        resultado = sum(lista)
        return resultado
    except TypeError:
        # Se houver um elemento que não é um número, levanta uma exceção personalizada
        raise Exception("Lista inválida - contém elemento não-numérico")

# Exemplo de uso:
try:
    numeros = [1, 2, 3, 4, 5]
    resultado_soma = somar_elementos(numeros)
    print("Soma dos elementos da lista:", resultado_soma)
    
    lista_invalida = [1, 2, 'a', 4, 5]  # Isso levantará a exceção
    resultado_soma_invalida = somar_elementos(lista_invalida)
    print("Soma dos elementos da lista inválida:", resultado_soma_invalida)
except Exception as e:
    print("Erro:", str(e))
