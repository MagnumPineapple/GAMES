import tkinter as tk
import time
import random
import sys

start_time = 0
mediciones = []
total_mediciones = 6
suma_mediciones = 0

def finalizar_juego():
    global suma_mediciones
    
    ventana.after_cancel(time)
    ventana.unbind("<Button-1>")
    label_tiempo.config(text="Juego terminado")
    promedio = round(suma_mediciones / total_mediciones, 2)
    label_promedio.config(text="Promedio: {} ms".format(promedio))
    
    if promedio <= 450:
        label_resultado.config(text="Aprobado", fg="green")
    else:
        label_resultado.config(text="Reprobado", fg="red")
    
    ventana.cget("bg") == "black"
    

def cambiar_color():
    global start_time
    global timer_id
    global suma_mediciones
    
    if len(mediciones) >= total_mediciones:
        finalizar_juego()
        return
    
    if ventana.cget("bg") == "green":
        end_time = time.time()
        tiempo_reaccion = round((end_time - start_time) * 1000, 2)
        mediciones.append(tiempo_reaccion)
        suma_mediciones += tiempo_reaccion
        label_tiempo.config(text="Tiempo de reacción: {} ms".format(tiempo_reaccion))
        ventana.configure(bg="red")
    else:
        start_time = time.time()
        ventana.configure(bg="green")
        ventana.after(2000, lambda: ventana.after(random.randint(3000, 6000), cambiar_color))

def on_clic_izquierdo(event):
    global suma_mediciones
    global start_time
    
    if ventana.cget("bg") == "green":
        end_time = time.time()
        tiempo_reaccion = round((end_time - start_time) * 1000, 2)
        mediciones.append(tiempo_reaccion)
        suma_mediciones += tiempo_reaccion
        label_tiempo.config(text="Tiempo de reacción: {} ms".format(tiempo_reaccion))
        ventana.configure(bg="red")
        
        if len(mediciones) >= total_mediciones:
            promedio = round(suma_mediciones / total_mediciones, 2)
            label_promedio.config(text="Promedio: {} ms".format(promedio))
        
        ventana.after(2000, lambda: ventana.after(random.randint(3000, 6000), cambiar_color))
    else:
        label_tiempo.config(text="Espera a que cambie a color verde!")
        ventana.configure(bg="gray")
        sys.exit()
        

ventana = tk.Tk()
ventana.title("Medidor de Tiempo de Reacción")
ventana.geometry("1280x720")

label_tiempo = tk.Label(ventana, text="Haz clic cuando cambie a verde", font=("Arial", 12))
label_tiempo.pack(pady=20)

label_promedio = tk.Label(ventana, text="Promedio: ", font=("Arial", 12))
label_promedio.pack(pady=6)

label_resultado = tk.Label(ventana, text="", font=("Arial", 12))
label_resultado.pack(pady=6)

ventana.bind("<Button-1>", on_clic_izquierdo)

ventana.after(2000, lambda: ventana.after(random.randint(3000, 6000), cambiar_color))

# finalizar_juego()

ventana.mainloop()