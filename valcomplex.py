def valComplex(num, array=None):
    status = True  # Inicializa la variable de estado como Verdadero por defecto
    
    if not isinstance(num, complex):
        status = False
        print("El primer argumento no es un número complejo.")  # Imprime un mensaje si el primer argumento no es complejo
    
    if array is not None:  # Si se proporciona un segundo argumento (array no es nulo)
        complex_num_module = abs(num)  # Calcula el valor absoluto del número complejo

        if isinstance(array, (tuple, list)):  # Verifica si el segundo argumento es una tupla o una lista
            if array[0] >= array[-1]:
                raise ValueError("El rango proporcionado no está ordenado de manera creciente.")
                # Lanza un error si el primer valor del rango es mayor o igual al último
            elif len(array) != 2:
                raise ValueError("El rango proporcionado tiene más de dos elementos.")
                # Lanza un error si el rango no tiene exactamente dos elementos
            elif not (array[0] < complex_num_module < array[-1]):
                status = False
                print("El valor absoluto del número complejo no está dentro del rango proporcionado.")
                # Si el valor absoluto del número complejo no está dentro del rango, cambia el estado a Falso

        else:
            raise TypeError("El segundo argumento no es del tipo correcto.")
            # Lanza un error si el segundo argumento no es una tupla ni una lista
        
    return status  # Devuelve el estado actual (Verdadero o Falso)

# Ejemplos de uso:
num_complex = 3 + 4j
range_tuple = (0, 10)
range_list = [1, 5]

print("Resultado 1:", valComplex(num_complex))  # Verifica si num_complex es complejo (Verdadero) y lo imprime
print("Resultado 2:", valComplex(num_complex, range_tuple))  # Verifica si num_complex está dentro del rango_tuple (Falso) y lo imprime
print("Resultado 3:", valComplex(num_complex, range_list))   # Verifica si num_complex está dentro del range_list (Verdadero) y lo imprime

