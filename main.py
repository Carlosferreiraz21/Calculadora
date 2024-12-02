#Arquivo e branch MAIN principal
import tkinter as tk

# Funções para operações matemáticas
def add():
    result.set(float(entry_num1.get()) + float(entry_num2.get()))

def subtract():
    result.set(float(entry_num1.get()) - float(entry_num2.get()))

def multiply():
    result.set(float(entry_num1.get()) * float(entry_num2.get()))

def divide():
    try:
        result.set(float(entry_num1.get()) / float(entry_num2.get()))
    except ZeroDivisionError:
        result.set("Erro! Divisão por zero.")

# Criando a janela principal
window = tk.Tk()
window.title("Calculadora")

# Entradas para números
entry_num1 = tk.Entry(window, width=15, font=("Arial", 14))
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(window, width=15, font=("Arial", 14))
entry_num2.grid(row=0, column=1, padx=10, pady=10)

# Variável para exibir o resultado
result = tk.StringVar()

# Label para mostrar o resultado
label_result = tk.Label(window, textvariable=result, font=("Arial", 14))
label_result.grid(row=1, column=0, columnspan=2, pady=10)

# Botões de operação
button_add = tk.Button(window, text="+", font=("Arial", 14), command=add)
button_add.grid(row=2, column=0, padx=10, pady=10)

button_subtract = tk.Button(window, text="-", font=("Arial", 14), command=subtract)
button_subtract.grid(row=2, column=1, padx=10, pady=10)

button_multiply = tk.Button(window, text="*", font=("Arial", 14), command=multiply)
button_multiply.grid(row=3, column=0, padx=10, pady=10)

button_divide = tk.Button(window, text="/", font=("Arial", 14), command=divide)
button_divide.grid(row=3, column=1, padx=10, pady=10)

# Iniciando a interface gráfica
window.mainloop()
