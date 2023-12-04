try:
    lista = [1, 2, 3, 4, 5]
    indice = int(input("Digite um índice para acessar na lista: "))
    
    elemento = lista[indice]
    print(f"Elemento no índice {indice}: {elemento}")
except IndexError:
    print("Erro: Índice fora dos limites da lista")
except ValueError:
    print("Erro: Digite um índice válido (número inteiro)")
except Exception as e:
    print(f"Erro genérico: {str(e)}")
