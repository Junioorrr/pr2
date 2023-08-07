def valList(array, var=None, string=None):
    status = True  # Inicializa la variable de estado como Verdadero por defecto
    
    if not isinstance(array, list):
        status = False
        print("El primer argumento no es una lista.")  # Imprime un mensaje si el primer argumento no es una lista
    
    if var is not None or string is not None:  # Si se proporciona var o string
        if string == "value":  # Si string es "value"
            if isinstance(var, list):  # Verifica si var es una lista
                if var != array:  # Si el contenido de var y array no son iguales
                    status = False
                    print("El contenido de la lista proporcionada y la variable no son iguales.")  # Cambia el estado y muestra un mensaje
            else:
                status = False
                print("La variable no es una lista.")  # Cambia el estado y muestra un mensaje si var no es una lista
        elif string == "len":  # Si string es "len"
            if isinstance(var, int):  # Verifica si var es un número entero
                var = str(var)  # Convierte var a cadena para comparar longitudes
                if len(array) != len(var):  # Si las longitudes no coinciden
                    status = False
                    print("La longitud de la lista no coincide con la variable proporcionada.")  # Cambia el estado y muestra un mensaje
            else:
                status = False
                print("La variable no es un número entero.")  # Cambia el estado y muestra un mensaje si var no es un entero
        else:  # Si string no es ni "value" ni "len"
            if not (isinstance(var, list) or isinstance(var, int)):  # Si var no es ni lista ni entero
                raise TypeError("El segundo argumento no es del tipo lista o entero.")  # Lanza un error de tipo
            else:
                raise ValueError("El tercer argumento no es 'value' ni 'len'.")  # Lanza un error de valor
        
    return status  # Devuelve el estado actual de la variable (Verdadero o Falso)

# Ejemplos de uso:
my_list = [1, 2, 3]
another_list = [1, 2, 3, 4]
length_var = 4

print("Resultado 1:", valList(my_list))  # Verifica si my_list es una lista (Verdadero) y lo imprime
print("Resultado 2:", valList(my_list, var=another_list, string="value"))  # Verifica si another_list es igual a my_list (Falso) y lo imprime
print("Resultado 3:", valList(my_list, var=length_var, string="len"))      # Verifica si la longitud de my_list coincide con length_var (Verdadero) y lo imprime
