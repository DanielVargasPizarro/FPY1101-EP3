libros_prestados=[]
sku=[]
def registrar_libro(libros):
    nombre_libro=input('ingrese el nombre del libro\n').lower()
    autor_libro=input('ingrese el autor del libro\n').lower()
    ano_libro=input('ingrese el año del libro\n').lower()
    sku_libro=input('para crear el SKU guíese por el siguiente formato:\n6 primeras letras del título del libro-las 3 primeras letras del autor-año de publicación\n').lower()
    

    print('\nrecuerde llevar un registro propio de los datos para facilitar su trabajo\n')

    libros.append({
        'Nombre' : nombre_libro,
        'Autor' : autor_libro,
        'Año de libro' : ano_libro,
        'SKU' : sku_libro
    })

def prestar_libro(libros):
    libro_a_prestar=input('por favor ingrese el libro que desea solicitar\n').lower()
    if libro_a_prestar not in libros_prestados:
        for i in libros:
            libros_prestados.append(i)
            sku.append(i)
    else:
        print ('error, intente nuevamente')
    archivo_libros_prestados=f'librosprestados_{libros_prestados}.txt'

def listar_libros(libros):
    print(libros)

def imprimir_prestamos(libros_prestados):
    print(libros_prestados[0])
