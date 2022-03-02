#1 Estamos defininiendo la variable number_of_food_groups y le estamos enviando el valor 5 a dicha función por lo que al imprimirlo nos dara un resultado de 5 ya que "return" indica el final de la funcion pero tambien el valor que devolverá la función.
def number_of_food_groups():
    return 5
print(number_of_food_groups())


#2 Este código nos arrojará un error puesto que función number_of_days in a week_silicon_or_triangle_sides no ha sido definida aún.

# def number_of_military_branches():
#     return 5
# print (number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


#3 Este código nos arrojará un valor de 5 como resultado puesto que el primer "return"  en una función, indica que “se ha terminado” de procesar y se le asigno un valor de retorno de 5 a la funcion por lo que el el segundo return con 10 ya no será efectuado.
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())


#4 Este código nos arrojará un valor de 5 como resultado puesto que el "return"  en  una función, indica que “se ha terminado” de procesar y se le asigno un valor de retorno de 5 que sera impreso con la funcion print(funcion) que se encuentra fuera de la función.
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())


#5 Este código en  la primera funcion se imprimira el valor de 5, pero esto no significa que esta funcion devuelva un valor de 5 solo se esta imprmiendo y la funcion se esta quedando sin ningun valor por lo que que al asignarla a la variable x e imprimirla no arrogará ningun valor por que no hubo un "return"
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)


#6 No hay un "return" por lo que no hay valores para devolucion por ende no se puede efectuar la suma print(add(1,2)+add(2,3)), por separado si se imprmira un valor de 3 y 5, pero al efectuar la suma no se podra puesto que no existen valores.

def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))


#7 Este codigo arrojará un valor string de 25
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

#8 Con este código primero se obtendrá la impresion dentro de la funcion la variable b=100, luego entrará en el ciclo de la condicional if donde segun sea el caso y cumpla con la condicion, con un "return" se devolvera un valor para esta funcion y el return que se encuentra fuera del if no se tomara en cuenta puesto que previamente ya hubo un return efectuado, que dara un valor de 10 al momento de imprimir la función. En conclusión se imprimirá 199 y 10.
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#9 Este código devolverá como resultado 7, 14 y 21
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#10 Este código imprimirá como resultado 8
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))


#11 Este código imprimirá 500,500,300,500
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)


#12 Este código imprimirá 500,500,300,500
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


#13 Este código imprimirá 500,500,300,300
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


#14 Este código imprimirá la función foo(); 1, 3 y 2
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


#15 Este código imprimirá la variable y que es igual a la funcion foo la cual contiene: 1,3,5 y 10
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)