try:
    dicionario = {"a": 1, "b": 2, "c": 3}
    chave = input("Digite uma chave para acessar no dicionário: ")
    
    valor = dicionario[chave]
    print(f"Valor associado à chave '{chave}': {valor}")
except KeyError:
    print(f"Erro: Chave '{chave}' não encontrada no dicionário")
except Exception as e:
    print(f"Erro genérico: {str(e)}")
