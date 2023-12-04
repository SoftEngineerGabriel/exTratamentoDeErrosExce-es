def dividir_lista(lista, num_partes):
    try:
        if len(lista) % num_partes != 0 or num_partes <= 0:
            raise ValueError("Número de partes inválido para dividir a lista")
        
        tamanho_parte = len(lista) // num_partes
        partes = [lista[i:i+tamanho_parte] for i in range(0, len(lista), tamanho_parte)]
        return partes
    except ValueError as e:
        raise Exception(str(e))

# Exemplo de uso:
try:
    minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numero_partes = int(input("Digite o número de partes para dividir a lista: "))
    
    resultado_divisao = dividir_lista(minha_lista, numero_partes)
    print("Lista dividida em partes iguais:", resultado_divisao)
except Exception as e:
    print("Erro:", str(e))
