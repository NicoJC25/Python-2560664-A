Num1 = int(input('Ingrese el primer numerador: '))
Den1 = int(input('Ingrese el primer denominador: '))
Num2 = int(input('Ingrese el segundo numerador: '))
Den2 = int(input('Ingrese el segundo denominador: '))
ope = input('Elija el tipo de opearcion: ')
if ope == 'suma':
    if Den1 == Den2:
        Num1 = Num1 + Num2
        print ('La respuesta es: ',Num1, '/' ,Den1 )
    else:
        Num1 = (Num1 * Den2) + (Num2 * Den1)
        Den1 = Den1 * Den2
        print ('La respuesta es: ',Num1, '/' ,Den1 )
elif ope == 'resta':
    if Den1 == Den2:
        Num1 = Num1 - Num2
        print ('La respuesta es: ',Num1, '/' ,Den1 )
    else:
        Num1 = (Num1 * Den2) - (Num2 * Den1)
        Den1 = Den1 * Den2
        print ('La respuesta es: ',Num1, '/' ,Den1 )
elif ope == 'multiplicacion':
    Num1 = Num1 * Num2
    Den1 = Den1 * Den2
    print ('La respuesta es: ',Num1, '/' ,Den1 )
elif ope == 'division':
    Num1 = Num1 * Den2
    Den1 = Num2 * Den1
    print ('La respuesta es: ',Num1, '/' ,Den1 )
else:
    print ('La operacion no es valida')