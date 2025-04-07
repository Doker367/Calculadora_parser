# Calculadora con Interfaz Gráfica

Este proyecto es una calculadora con interfaz gráfica desarrollada en Python. Permite realizar operaciones matemáticas básicas, cargar imágenes y usar el micrófono para ingresar expresiones matemáticas mediante reconocimiento de voz.

## Requisitos

- Python 3.8 o superior
- pip (administrador de paquetes de Python)

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Doker367/Calculadora_parser.git
   cd tu-repositorio
   ```

2. Crea un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Activa el entorno virtual si no lo has hecho:
   ```bash
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

2. Ejecuta la calculadora:
   ```bash
   python3 gui_calculator.py
   ```

## Funcionalidades

- Operaciones matemáticas básicas: suma, resta, multiplicación y división.
- Logaritmo base 10.
- Potencia (n^n).
- Cargar imágenes.
- Reconocimiento de voz para ingresar expresiones matemáticas.

## Librerías utilizadas

- `tkinter`: Para la interfaz gráfica.
- `opencv-python`: Para cargar y mostrar imágenes.
- `speechrecognition`: Para el reconocimiento de voz.
- `ply`: Para el análisis léxico y sintáctico de expresiones matemáticas.

## Notas

- Asegúrate de que tu sistema tenga configurado un micrófono funcional si deseas usar la funcionalidad de reconocimiento de voz.
- Si no tienes una cámara disponible, puedes cargar imágenes desde tu sistema de archivos.

## Autor

Desarrollado por Doker367.