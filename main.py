#Arquivo MAIN principal
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
    except ValueError:
        result.set("Erro: Entrada inválida")

# Janela principal
window = tk.Tk()
window.title("Calculadora")
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

# Botões básicos
btn_add = tk.Button(window, text="+", font=("Arial", 14), command=lambda: calculate("+"))
btn_add.pack(side="left", padx=5, pady=10)

btn_sub = tk.Button(window, text="-", font=("Arial", 14), command=lambda: calculate("-"))
btn_sub.pack(side="left", padx=5, pady=10)

window.mainloop()


