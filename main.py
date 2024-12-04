import tkinter as tk

# Função de cálculo básica
def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if operation == "+":
            result.set(num1 + num2)
        elif operation == "-":
            result.set(num1 - num2)
        elif operation == "*":
            result.set(num1 * num2)
        elif operation == "/":
            result.set(num1 / num2 if num2 != 0 else "Erro: Divisão por zero")
        elif operation == "%":
            result.set(num1 % num2)
    except ValueError:
        result.set("Erro: Entrada inválida")

# Janela principal
window = tk.Tk()
window.title("Calculadora Completa")
window.configure(bg="#f5f5f5")
window.geometry("300x400")

# Configurações visuais
title = tk.Label(window, text="Calculadora Completa", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333")
title.pack(pady=10)

# Frame para entradas
entry_frame = tk.Frame(window, bg="#f5f5f5")
entry_frame.pack(pady=10)
entry_num1 = tk.Entry(entry_frame, font=("Arial", 14), width=10)
entry_num1.grid(row=0, column=0, padx=5)
entry_num2 = tk.Entry(entry_frame, font=("Arial", 14), width=10)
entry_num2.grid(row=0, column=1, padx=5)

# Resultado
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result, font=("Arial", 14), bg="#f5f5f5", fg="#007700")
result_label.pack(pady=10)

# Botões com todas as operações
button_frame = tk.Frame(window, bg="#f5f5f5")
button_frame.pack(pady=10)
operations = [("+", "#4CAF50"), ("-", "#FF5722"), ("*", "#2196F3"), ("/", "#9C27B0"), ("%", "#FFC107")]

for op, color in operations:
    btn = tk.Button(
        button_frame, text=op, font=("Arial", 14), bg=color, fg="white", command=lambda op=op: calculate(op)
    )
    btn.pack(side="left", padx=5)

window.mainloop()


