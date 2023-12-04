def contar_vogais(string):
    try:
        if not isinstance(string, str):
            raise ValueError("Argumento inválido - Deve ser uma string")
        
        vogais = "aeiouAEIOU"
        count = 0
        for char in string:
            if char in vogais:
                count += 1
        return count
    except ValueError as e:
        raise Exception(str(e))

# Exemplo de uso:
try:
    resultado_contagem = contar_vogais("Hello World")
    print("Número de vogais em 'Hello World':", resultado_contagem)
    
    resultado_contagem_invalido = contar_vogais(123)  # Isso levantará a exceção
    print("Número de vogais em 123:", resultado_contagem_invalido)
except Exception as e:
    print("Erro:", str(e))
