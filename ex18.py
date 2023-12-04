while True:
    try:
        # Código dentro do loop infinito que pode gerar exceções
        numero = int(input("Digite um número: "))
        resultado = 10 / numero
        print("Resultado da operação:", resultado)
    except ZeroDivisionError:
        print("Erro: Divisão por zero")
    except ValueError:
        print("Erro: Digite um número válido")
    except KeyboardInterrupt:
        print("\nLoop interrompido pelo usuário")
        break
    except Exception as e:
        print(f"Erro genérico: {str(e)}")
