try:
    resultado = 10 / 0
    minha_lista = [1, 2, 3]
    elemento = minha_lista[5]
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except IndexError:
    print("Erro: Índice fora dos limites da lista")
except Exception as e:
    print(f"Erro genérico: {str(e)}")
