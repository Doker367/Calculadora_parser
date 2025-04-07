import tkinter as tk
from tkinter import messagebox
import cv2
import threading
import speech_recognition as sr
from grammar_calculator import evaluate_expression
import tkinter.filedialog as fd

def on_calculate():
    expression = entry.get()
    result = evaluate_expression(expression)
    result_label.config(text=f"Resultado: {result}")

def on_button_click(value):
    entry.insert(tk.END, value)

def load_image():
    try:
        file_path = fd.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if not file_path:
            return
        image = cv2.imread(file_path)
        if image is None:
            raise ValueError("No se pudo cargar la imagen.")
        cv2.imshow("Imagen Cargada", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        messagebox.showerror("Error al Cargar Imagen", str(e))

def use_microphone():
    try:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            messagebox.showinfo("Micrófono", "Hable ahora...")
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language="es-ES")
            entry.insert(tk.END, text)
    except sr.UnknownValueError:
        messagebox.showerror("Error", "No se pudo entender el audio.")
    except sr.RequestError as e:
        messagebox.showerror("Error", f"Error con el servicio de reconocimiento: {e}")
    except OSError:
        messagebox.showerror("Error de Micrófono", "No se detectó un dispositivo de entrada de audio.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Entrada de texto
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones de números y operaciones
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, command=on_calculate, width=5, height=2)
    else:
        btn = tk.Button(root, text=text, command=lambda t=text: on_button_click(t), width=5, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5)

# Botones adicionales
image_button = tk.Button(root, text="Cargar Imagen", command=load_image, width=10, height=2)
image_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

microphone_button = tk.Button(root, text="Micrófono", command=use_microphone, width=10, height=2)
microphone_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# Etiqueta para mostrar el resultado
result_label = tk.Label(root, text="Resultado: ")
result_label.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()