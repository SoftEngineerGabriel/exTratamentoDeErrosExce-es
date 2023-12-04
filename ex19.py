try:
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        raise ValueError("Erro interno - divisão por zero")
except ValueError as e:
    print(f"Erro aninhado: {str(e)}")
except Exception as e:
    print(f"Erro genérico: {str(e)}")
