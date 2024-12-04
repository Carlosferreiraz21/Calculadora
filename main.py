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
window.title("Calculadora Visual")
window.configure(bg="#f5f5f5")
window.geometry("300x300")

# Configurações visuais
title = tk.Label(window, text="Calculadora Visual", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333")
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

# Botões básicos com cores
btn_add = tk.Button(window, text="+", font=("Arial", 14), bg="#4CAF50", fg="white", command=lambda: calculate("+"))
btn_add.pack(side="left", padx=5)

btn_sub = tk.Button(window, text="-", font=("Arial", 14), bg="#FF5722", fg="white", command=lambda: calculate("-"))
btn_sub.pack(side="left", padx=5)

window.mainloop()



