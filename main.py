import tkinter as tk
from tkinter import messagebox

def obtener_tramos_impuesto():
    # Tramos del Impuesto Único de Segunda Categoría para noviembre de 2024
    # Fuente: Servicio de Impuestos Internos (SII)
    tramos = [
        (0, 899478.00, 0, 0),
        (899478.01, 1998840.00, 0.04, 35979.12),
        (1998840.01, 3331400.00, 0.08, 115932.72),
        (3331400.01, 4663960.00, 0.135, 299159.72),
        (4663960.01, 5996520.00, 0.23, 742235.92),
        (5996520.01, 7995360.00, 0.304, 1185978.40),
        (7995360.01, 20654680.00, 0.35, 1553764.96),
        (20654680.01, float('inf'), 0.4, 2586498.96)
    ]
    return tramos

def calcular_impuesto_renta(renta_imponible):
    tramos = obtener_tramos_impuesto()
    for tramo in tramos:
        if tramo[0] <= renta_imponible <= tramo[1]:
            impuesto = renta_imponible * tramo[2] - tramo[3]
            return max(impuesto, 0)
    return 0

def calcular_sueldo_liquido():
    try:
        renta_bruta = float(entry_renta.get())
        if renta_bruta <= 0:
            messagebox.showerror("Error", "El ingreso bruto debe ser un número positivo.")
            return
        
        # Cálculo de deducciones
        afp = renta_bruta * 0.10
        salud = renta_bruta * 0.07
        seguro_cesantia = renta_bruta * 0.006
        renta_imponible = renta_bruta - (afp + salud + seguro_cesantia)
        impuesto_renta = calcular_impuesto_renta(renta_imponible)
        total_descuentos = afp + salud + seguro_cesantia + impuesto_renta
        
        sueldo_liquido = renta_bruta - total_descuentos
        
        # Mostrar los resultados
        resultado_afp.set(f"AFP (10%): ${afp:,.2f}")
        resultado_salud.set(f"Salud (7%): ${salud:,.2f}")
        resultado_seguro.set(f"Seguro Cesantía (0.6%): ${seguro_cesantia:,.2f}")
        resultado_impuesto.set(f"Impuesto Renta: ${impuesto_renta:,.2f}")
        resultado_liquido.set(f"Sueldo Líquido: ${sueldo_liquido:,.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")

def reiniciar():
    entry_renta.delete(0, tk.END)
    resultado_afp.set("")
    resultado_salud.set("")
    resultado_seguro.set("")
    resultado_impuesto.set("")
    resultado_liquido.set("")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Sueldo Líquido (Chile)")

# Etiqueta e ingreso de renta bruta
tk.Label(root, text="Ingreso Bruto Mensual (CLP):").grid(row=0, column=0, padx=10, pady=10)
entry_renta = tk.Entry(root)
entry_renta.grid(row=0, column=1, padx=10, pady=10)

# Botón para calcular
tk.Button(root, text="Calcular Sueldo Líquido", command=calcular_sueldo_liquido).grid(row=1, column=0, columnspan=2, pady=10)

# Resultados
resultado_afp = tk.StringVar()
resultado_salud = tk.StringVar()
resultado_seguro = tk.StringVar()
resultado_impuesto = tk.StringVar()
resultado_liquido = tk.StringVar()

tk.Label(root, textvariable=resultado_afp, fg="blue").grid(row=2, column=0, columnspan=2, pady=5)
tk.Label(root, textvariable=resultado_salud, fg="blue").grid(row=3, column=0, columnspan=2, pady=5)
tk.Label(root, textvariable=resultado_seguro, fg="blue").grid(row=4, column=0, columnspan=2, pady=5)
tk.Label(root, textvariable=resultado_impuesto, fg="blue").grid(row=5, column=0, columnspan=2, pady=5)
tk.Label(root, textvariable=resultado_liquido, fg="green").grid(row=6, column=0, columnspan=2, pady=10)

# Botón para reiniciar
tk.Button(root, text="Reiniciar", command=reiniciar).grid(row=7, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
root.mainloop()
