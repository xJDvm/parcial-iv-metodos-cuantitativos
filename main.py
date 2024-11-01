import os
import tkinter as tk
from tkinter import scrolledtext
import subprocess

def ejecutar_archivo(archivo, output_text):
    if archivo:
        output_text.delete(1.0, tk.END)

        
        output_text.insert(tk.END, f"Ejecutando {archivo}...\n")
        output_text.see(tk.END)
        output_text.update()
        
        # Ejecutar el archivo y capturar la salida
        process = subprocess.Popen(['python', archivo], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        
        # Mostrar la salida en el widget de texto
        output_text.insert(tk.END, stdout)
        if stderr:
            output_text.insert(tk.END, stderr)
        output_text.see(tk.END)
    else:
        output_text.insert(tk.END, "Opción no válida. Intente de nuevo.\n")
        output_text.see(tk.END)

def main():
    root = tk.Tk()
    root.title("Menú de Archivos")

    archivos = {
        '1': 'RAMIFICACIONACOTACION.PY',
        '2': 'BINARIA.PY',
        '3': 'ENTERAMIXTA.PY',
        '4': 'ENTERAPURA.PY',
        '5': 'PLANOSCORTES.PY',
        '6': 'MOCHILA.PY'
    }

    output_text = scrolledtext.ScrolledText(root, width=80, height=20)
    output_text.pack()

    for key, archivo in archivos.items():
        button = tk.Button(root, text=f"Opción {key}: {archivo}", command=lambda a=archivo: ejecutar_archivo(a, output_text))
        button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()