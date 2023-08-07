def valFloat(num, array=None):
    variable = True  # Inicializa la variable de estado como Verdadero por defecto
    
    if not isinstance(num, float):
        variable = False
        print("El primer argumento no es un número de punto flotante.")  # Imprime un mensaje si el primer argumento no es un número de punto flotante
    
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
                print("El número de punto flotante no está dentro del rango proporcionado.")
                # Si el número de punto flotante no está dentro del rango, cambia la variable a Falso
        else:
            raise TypeError("El segundo argumento no es del tipo correcto.")
            # Lanza un error si el segundo argumento no es una tupla ni una lista
        
    return variable  # Devuelve el estado actual (Verdadero o Falso)

# Ejemplos de uso:
num_float = 3.5
range_tuple = (0.0, 10.0)
range_list = [1.0, 5.0]

print("Resultado 1:", valFloat(num_float))  # Verifica si num_float es un número de punto flotante (Verdadero) y lo imprime
print("Resultado 2:", valFloat(num_float, range_tuple))  # Verifica si num_float está dentro del rango_tuple (Falso) y lo imprime
print("Resultado 3:", valFloat(num_float, range_list))   # Verifica si num_float está dentro del range_list (Verdadero) y lo imprime

