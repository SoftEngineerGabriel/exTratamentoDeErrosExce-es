def ordenar_strings(lista):
    try:
        if not all(isinstance(elemento, str) for elemento in lista):
            raise ValueError("Lista inválida - Deve conter apenas strings")
        
        return sorted(lista)
    except ValueError as e:
        raise Exception(str(e))

# Exemplo de uso:
try:
    lista_strings = ["banana", "maçã", "abacaxi", "laranja"]
    resultado_ordenacao = ordenar_strings(lista_strings)
    print("Lista ordenada alfabeticamente:", resultado_ordenacao)
    
    lista_invalida = ["banana", "maçã", 123, "laranja"]  # Isso levantará a exceção
    resultado_ordenacao_invalida = ordenar_strings(lista_invalida)
    print("Lista ordenada com elemento inválido:", resultado_ordenacao_invalida)
except Exception as e:
    print("Erro:", str(e))
