import tkinter as tk
from tkinter import messagebox
import cv2
import threading
import speech_recognition as sr
from grammar_calculator import evaluar_expresion
import tkinter.filedialog as fd

def calcular():
    expresion = entrada.get()
    resultado = evaluar_expresion(expresion)
    etiqueta_resultado.config(text=f"Resultado: {resultado}")

def boton_click(valor):
    entrada.insert(tk.END, valor)

def cargar_imagen():
    try:
        ruta_archivo = fd.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png")])
        if not ruta_archivo:
            return
        imagen = cv2.imread(ruta_archivo)
        if imagen is None:
            raise ValueError("No se pudo cargar la imagen.")
        cv2.imshow("Imagen Cargada", imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        messagebox.showerror("Error al Cargar Imagen", str(e))

def usar_microfono():
    try:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            messagebox.showinfo("Micrófono", "Hable ahora...")
            audio = recognizer.listen(source)
            texto = recognizer.recognize_google(audio, language="es-ES")
            entrada.insert(tk.END, texto)
    except sr.UnknownValueError:
        messagebox.showerror("Error", "No se pudo entender el audio.")
    except sr.RequestError as e:
        messagebox.showerror("Error", f"Error con el servicio de reconocimiento: {e}")
    except OSError:
        messagebox.showerror("Error de Micrófono", "No se detectó un dispositivo de entrada de audio.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Entrada de texto
entrada = tk.Entry(ventana, width=30)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones de números y operaciones
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (texto, fila, columna) in botones:
    if texto == '=':
        btn = tk.Button(ventana, text=texto, command=calcular, width=5, height=2)
    else:
        btn = tk.Button(ventana, text=texto, command=lambda t=texto: boton_click(t), width=5, height=2)
    btn.grid(row=fila, column=columna, padx=5, pady=5)

# Botones adicionales
boton_imagen = tk.Button(ventana, text="Cargar Imagen", command=cargar_imagen, width=10, height=2)
boton_imagen.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

boton_microfono = tk.Button(ventana, text="Micrófono", command=usar_microfono, width=10, height=2)
boton_microfono.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()