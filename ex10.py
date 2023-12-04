try:
    numero_inteiro = int(input("Digite um número inteiro: "))
    
    # Tenta converter o número inteiro em uma string
    numero_string = str(numero_inteiro)
    
    print(f"Número inteiro convertido para string: {numero_string}")
except ValueError:
    print("Erro: Digite um número inteiro válido")
except Exception as e:
    print(f"Erro genérico: {str(e)}")
