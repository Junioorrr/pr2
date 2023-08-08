# Definición de función que genera la clave utilizada para encriptar y desencriptar
def generar_clave():
    clave = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+=[]{}|;:,.<>? "
    return clave

# Definición de función para encriptar un mensaje
def encriptar(mensaje, clave):
    mensaje_encriptado = ""
    # Iteración sobre cada caracter en el mensaje
    for caracter in mensaje:
        # Si el caracter está en la clave
        if caracter in clave:
            # Obtener el índice del caracter en la clave
            indice = clave.index(caracter)
            # Agregar el caracter correspondiente en la clave al mensaje encriptado
            mensaje_encriptado += clave[indice]
        else:
            # Si el caracter no está en la clave, mantenerlo sin cambios
            mensaje_encriptado += caracter
    return mensaje_encriptado

# Definición de función para desencriptar un mensaje encriptado
def desencriptar(mensaje_encriptado, clave):
    mensaje_original = ""
    # Iteración sobre cada caracter en el mensaje encriptado
    for caracter in mensaje_encriptado:
        # Si el caracter está en la clave
        if caracter in clave:
            # Obtener el índice del caracter en la clave
            indice = clave.index(caracter)
            # Agregar el caracter correspondiente en la clave al mensaje original
            mensaje_original += clave[indice]
        else:
            # Si el caracter no está en la clave, mantenerlo sin cambios
            mensaje_original += caracter
    return mensaje_original

# Definición de función para obtener el mensaje del usuario
def obtener_mensaje_usuario():
    mensaje = input("Ingrese un mensaje: ")
    return mensaje

# Definición de la función principal del programa
def main():
    # Mensaje de bienvenida
    print("Bienvenido al Programa de Encriptación")
    
    # Generar la clave utilizando la función generar_clave()
    clave = generar_clave()

    # Obtener el mensaje del usuario utilizando la función obtener_mensaje_usuario()
    mensaje = obtener_mensaje_usuario()

    # Encriptar el mensaje utilizando la función encriptar()
    mensaje_encriptado = encriptar(mensaje, clave)
    print(f"Mensaje encriptado: {mensaje_encriptado}")

    # Desencriptar el mensaje encriptado utilizando la función desencriptar()
    mensaje_desencriptado = desencriptar(mensaje_encriptado, clave)
    print(f"Mensaje desencriptado: {mensaje_desencriptado}")


