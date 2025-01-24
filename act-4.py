def check_pass():
    contraseña_usuario = "usuario"
    intentos = 0

    while intentos < 3:
        user_pass = input('Introduce la contraseña')
        if contraseña_usuario == user_pass:
            print("Bienvneido")
            break
        else:
            tries += 1