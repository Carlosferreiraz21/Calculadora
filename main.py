#Branch att Backend
import tkinter as tk

# Funções de cálculo avançadas
def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y if y != 0 else "Erro: Divisão por zero",
            "%": lambda x, y: x % y
        }
        result.set(operations[operation](num1, num2))
    except ValueError:
        result.set("Erro: Entrada inválida")
    except KeyError:
        result.set("Erro: Operação inválida")

# Janela principal
window = tk.Tk()
window.title("Calculadora Avançada")
window.geometry("300x200")

# Entradas de número
entry_num1 = tk.Entry(window, font=("Arial", 14), width=10)
entry_num1.pack(pady=10)
entry_num2 = tk.Entry(window, font=("Arial", 14), width=10)
entry_num2.pack(pady=10)

# Resultado
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result, font=("Arial", 14))
result_label.pack(pady=10)

# Botões avançados
operations = ["+", "-", "*", "/", "%"]
for op in operations:
    btn = tk.Button(window, text=op, font=("Arial", 14), command=lambda op=op: calculate(op))
    btn.pack(side="left", padx=5)

window.mainloop()
