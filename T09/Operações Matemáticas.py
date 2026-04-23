a = 10
b = 3

print(f"Soma: {a + b}")           # 13
print(f"Subtração: {a - b}")      # 7
print(f"Multiplicação: {a * b}")  # 30
print(f"Divisão: {a / b}")        # 3.333...
print(f"Divisão inteira: {a // b}") # 3
print(f"Resto: {a % b}")          # 1
print(f"Potência: {a ** b}")      # 1000

# Prioridade: parênteses > potência > * / // % > + -
resultado = (2 + 3) * 4 ** 2
print(f"(2+3)*4² = {resultado}")  # 5 * 16 = 80