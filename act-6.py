def chec_chars():
    palabra= input('Introduce una palabra')
    for i in palabra:
        if"@"== i:
            print("La palabra tiene el caracter @")
        elif "#" == i:
            print("La palabra tiene el caracter #")