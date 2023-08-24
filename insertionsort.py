import tkinter as tk
import time
import psutil
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j][2] > key[2]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def agregar_producto():
    nombre_producto = entrada_producto.get()
    precio_producto = float(entrada_precio.get())
    cantidad_producto = int(entrada_cantidad.get())
    productos.append((nombre_producto, precio_producto, cantidad_producto))
    lista_productos.insert("end", f"{nombre_producto} - s/{precio_producto:.2f} - {cantidad_producto}")

def ordenar_productos():
    productos.clear()
    for item in lista_productos.get(0, "end"):
        nombre, precio, cantidad = item.split(" - ")
        precio = float(precio.split("s/")[1])
        cantidad = int(cantidad)
        productos.append((nombre, precio, cantidad))
    
    tiempo_inicio = time.time()
    insertion_sort(productos)
    tiempo_fin = time.time()

    tiempo_ejecucion = tiempo_fin - tiempo_inicio
    uso_memoria = psutil.Process().memory_info().rss / 1024 / 1024  # Uso de memoria en MB

    lista_productos.delete(0, "end")
    for producto in productos:
        lista_productos.insert("end", f"{producto[0]} - s/{producto[1]:.2f} - {producto[2]}")

    etiqueta_resultado.config(text=f"Ordenado en {tiempo_ejecucion:.6f} segundos\nUso de memoria: {uso_memoria:.2f} MB")

raiz = tk.Tk()
raiz.title("Ordenamiento de Productos por Cantidad con Insertion Sort")

productos = []

etiqueta_producto = tk.Label(raiz, text="Producto:")
etiqueta_producto.pack()

entrada_producto = tk.Entry(raiz)
entrada_producto.pack()

etiqueta_precio = tk.Label(raiz, text="Precio:")
etiqueta_precio.pack()

entrada_precio = tk.Entry(raiz)
entrada_precio.pack()

etiqueta_cantidad = tk.Label(raiz, text="Cantidad:")
etiqueta_cantidad.pack()

entrada_cantidad = tk.Entry(raiz)
entrada_cantidad.pack()

boton_agregar = tk.Button(raiz, text="Agregar Producto", command=agregar_producto)
boton_agregar.pack()

lista_productos = tk.Listbox(raiz)
lista_productos.pack()

boton_ordenar = tk.Button(raiz, text="Ordenar Productos", command=ordenar_productos)
boton_ordenar.pack()

etiqueta_resultado = tk.Label(raiz, text="")
etiqueta_resultado.pack()

raiz.mainloop()
