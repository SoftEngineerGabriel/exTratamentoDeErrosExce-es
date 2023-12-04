def validar_data(data):
    try:
        # Divide a data em dia, mês e ano
        dia, mes, ano = map(int, data.split('/'))

        # Tenta criar um objeto de data
        from datetime import datetime
        datetime(ano, mes, dia)

        # Se não houver exceção, a data é válida
        print("Data válida:", data)
    except ValueError:
        # Se houver exceção, a data é inválida
        raise Exception("Data inválida")

# Solicita a data ao usuário
data_input = input("Digite uma data no formato 'dd/mm/aaaa': ")

# Tenta validar a data
try:
    validar_data(data_input)
except Exception as e:
    print("Erro:", str(e))
