try:
    # Tenta abrir e ler as configurações de um arquivo
    with open("configuracoes.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        
    # Processa as linhas do arquivo (exemplo: converte para dicionário)
    configuracoes = {}
    for linha in linhas:
        chave, valor = linha.strip().split("=")
        configuracoes[chave] = valor
    
    print("Configurações lidas:", configuracoes)
except FileNotFoundError:
    print("Erro: Arquivo de configurações não encontrado")
except ValueError:
    print("Erro: Arquivo de configurações mal formatado")
except Exception as e:
    print(f"Erro genérico: {str(e)}")
