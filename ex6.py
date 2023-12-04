def calcular_fatorial(numero):
    try:
        if not isinstance(numero, int) or numero < 0:
            raise ValueError("Argumento inválido - Deve ser um número inteiro positivo")
        
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado
    except ValueError as e:
        raise Exception(str(e))

# Exemplo de uso:
try:
    resultado_fatorial = calcular_fatorial(5)
    print("Fatorial de 5:", resultado_fatorial)
    
    resultado_fatorial_invalido = calcular_fatorial(-2)  # Isso levantará a exceção
    print("Fatorial de -2:", resultado_fatorial_invalido)
except Exception as e:
    print("Erro:", str(e))
