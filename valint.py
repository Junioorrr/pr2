def valInt(num, array=None):
    variable = True  # Inicializa la variable de estado como Verdadero por defecto
    
    if not isinstance(num, int):
        variable = False
        print("El primer argumento no es un número entero.")  # Imprime un mensaje si el primer argumento no es un número entero
        return variable  # Retorna el valor de la variable (Falso)
    
    if array is not None:  # Si se proporciona un segundo argumento (array no es nulo)
        if isinstance(array, (tuple, list)):  # Verifica si el segundo argumento es una tupla o una lista
            if array[0] >= array[-1]:
                raise ValueError("El rango proporcionado no está ordenado de manera creciente.")
                # Lanza un error si el primer valor del rango es mayor o igual al último
            elif len(array) != 2:
                raise ValueError("El rango proporcionado tiene más de dos elementos.")
                # Lanza un error si el rango no tiene exactamente dos elementos
            elif not (array[0] < num < array[-1]):
                variable = False
                print("El número entero no está dentro del rango proporcionado.")
                # Si el número entero no está dentro del rango, cambia la variable a Falso y muestra un mensaje
        else:
            raise TypeError("El segundo argumento no es del tipo correcto.")
            # Lanza un error si el segundo argumento no es una tupla ni una lista
        
    return variable  # Devuelve el estado actual de la variable (Verdadero o Falso)

# Ejemplos de uso:
num_int = 5
range_tuple = (0, 10)
range_list = [1, 5]

print("Resultado 1:", valInt(num_int))  # Verifica si num_int es un número entero (Verdadero) y lo imprime
print("Resultado 2:", valInt(num_int, range_tuple))  # Verifica si num_int está dentro del rango_tuple (Falso) y lo imprime
print("Resultado 3:", valInt(num_int, range_list))   # Verifica si num_int está dentro del range_list (Verdadero) y lo imprime
