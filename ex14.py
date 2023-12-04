try:
    senha = input("Digite uma senha com pelo menos 8 caracteres: ")
    
    if len(senha) < 8:
        raise ValueError("Senha muito curta - deve ter pelo menos 8 caracteres")
    
    print("Senha válida!")
except ValueError as e:
    print(f"Erro: {str(e)}")
except Exception as e:
    print(f"Erro genérico: {str(e)}")
