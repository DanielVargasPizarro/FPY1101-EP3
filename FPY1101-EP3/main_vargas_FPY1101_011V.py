import funciones_vargas_FPY1101_011V as fn

libros=[]

print(libros)

try:
    while True:
        op1=int(input('\nbinvenido a biblioteca vargas, seleccione la opcion que desea realizar:\n\n1.-Registrar libro\n2.-Prestar libro\n3.-Listar todos los libros\n4.-Imprimir reporte de prestamos\n5.-Salir del programa\n'))
        if op1 == 1:
            fn.registrar_libro(libros)
        elif op1 == 2:
            fn.prestar_libro(libros)
        elif op1 == 3:
            fn.listar_libros(libros)
        elif op1 == 4:
            print()
        elif op1==5:
            break
except ValueError:
    print ('error, seleccione nuevamente')