import tkinter as tk
from tkinter import font
import subprocess

def abrir_ajedrez():
    subprocess.Popen(["python", "ajedrez.py"])

def mostrar_enunciado():
    enunciado = "Deben realizar la implementación con interfaz gráfica y ustedes como humanos jugar contra la IA. Deben usar la metodología de árboles vista en clase, aplicar poda alfa/beta, determinar una buena heurística e implementar Minimax para la solución."
    ventana_enunciado = tk.Toplevel()
    ventana_enunciado.title("Enunciado del problema")
    ventana_enunciado.geometry("600x400")

    label_enunciado = tk.Label(ventana_enunciado, text=enunciado, wraplength=500)
    label_enunciado.pack(pady=20, padx=20)

def mostrar_programadores():
    programadores = "Realizado por: \n\n- Sebasttian Giraldo \n- Steven Muñoz \n- Daniel Ospina \n \n Presentado a: \n- Joshua Triana"

    ventana_programadores = tk.Toplevel()
    ventana_programadores.title("Programadores")
    ventana_programadores.geometry("200x200")

    label_programadores = tk.Label(ventana_programadores, text=programadores, wraplength=350)
    label_programadores.pack(pady=20, padx=20)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Menú")
ventana.geometry("800x600")
ventana.configure(bg="#313233")

# Estilo para los botones
estilo_botones = {"background": "#313233", "foreground": "white", "font": font.Font(size=14, weight="bold")}

# Botón 1: Juego de Ajedrez
boton_ajedrez = tk.Button(ventana, text="Juego de Ajedrez", width=20, height=2, command=abrir_ajedrez, **estilo_botones)
boton_ajedrez.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Botón 2: Mostrar Enunciado
boton_enunciado = tk.Button(ventana, text="Mostrar Enunciado", width=20, height=2, command=mostrar_enunciado, **estilo_botones)
boton_enunciado.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Botón 3: Mostrar Programadores
boton_programadores = tk.Button(ventana, text="Mostrar Programadores", width=20, height=2, command=mostrar_programadores, **estilo_botones)
boton_programadores.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Iniciar el bucle de la aplicación
ventana.mainloop()
