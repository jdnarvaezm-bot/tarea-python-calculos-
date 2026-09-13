# Definimos la función con dos parámetros
def calcularTotal(precio, cantidad):
    total = precio * cantidad
    return total

# Bloque principal del programa
if __name__ == "__main__":
    # Valores de ejemplo
    precio = 10
    cantidad = 3
    
    # Llamamos a la función
    resultado = calcularTotal(precio, cantidad)
    
    # Mostramos el resultado en consola
    print(f"El total a pagar es: {resultado}")