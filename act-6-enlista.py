def chec_chars():
    palabra= input('Introduzca una palabra')
    special_i=["@", "#", "$", "%"]

    for i in palabra:
        if i in palabra:
            print("La palabra contiene el caracter", i)