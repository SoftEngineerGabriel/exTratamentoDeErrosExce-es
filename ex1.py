def dividir_numeros(numero1, numero2):
    try:
        resultado = numero1 / numero2
        return resultado
    except ZeroDivisionError:
        raise Exception("Divisão por zero não permitida")

# Exemplo de uso:
try:
    resultado_divisao = dividir_numeros(10, 2)
    print("Resultado da divisão:", resultado_divisao)
    
    resultado_divisao_por_zero = dividir_numeros(5, 0)  # Isso levantará a exceção
    print("Resultado da divisão por zero:", resultado_divisao_por_zero)
except Exception as e:
    print("Erro:", str(e))

