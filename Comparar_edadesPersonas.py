nombre1 = input('Ingrese su nombre: ')
edad1 = int(input(f'{nombre1}, que edad tiene: '))
nombre2 = input('Ingrese su nombre: ')
edad2 = int(input(f'{nombre2}, que edad tienes: '))

if edad1 > edad2:
    print(nombre1+" es mayor que "+nombre2)
elif edad1 < edad2:
    print(nombre2+" es mayor que "+nombre1)
else:
    print(nombre1+" tienen la misma edad de "+ nombre2)