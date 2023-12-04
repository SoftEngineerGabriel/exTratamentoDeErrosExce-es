try:
    # Tenta abrir o arquivo para escrita
    with open('arquivo_existente.txt', 'w') as arquivo:
        # Se o arquivo já existir, isso levantará uma exceção FileExistsError
        arquivo.write("Conteúdo de exemplo")
    print("Arquivo aberto e modificado com sucesso.")
except FileExistsError:
    print("Erro: O arquivo já existe. Não é possível sobrescrever no modo de escrita.")
except IOError as e:
    print(f"Erro de E/S: {str(e)}")
except Exception as e:
    print(f"Erro desconhecido: {str(e)}")
