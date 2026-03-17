while True:
 
      # Display menu with operations #
 print('Select operation:')
 print('1. Add', end='     ')
 print('2. Subtract')
 print('3. Multiply', end='     ')
 print('4. Divide')
 print('5. Exponentiate', end='     ')
 print('6. Root')
 print('7. Percentage', end='   ')
 print('8. Hypotenuse')
 print('9. Exit')
      
      # Choose operations from menu #
 choice = input('Enter choice (1/2/3/4/5/6/7/8/9): ')

      # ensure accurate operation selection #
 if choice == '9':
    print('Exiting...')
    break
 if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
    print('invalid input, try again!')
    break 

      # Recieve Input data which must be intergers #
 num1 = int(input('Enter first number: '))
 num2 = int(input('Enter second number: '))

      # Starting operations based on user earlier selection #
 if choice == '1':
    print('Result:', int(num1) + int(num2))
 elif choice == '2':
    print('Result:', int(num1) - int(num2))
 elif choice == '3':
    print('Result:', int(num1) * int(num2))
 elif choice == '4':
    if num2 != 0:
       print('Result:', int(num1) / int(num2))
    else:
        print('Error: Divided by zero')
 elif choice == '5':
    if num1 != 0 and num2 != 0:
       print('Result:', int(num1) ** int(num2))
    else:
        print('Error: Exponentiation with zero')
 elif choice == '6':
    if num1 != 0 and num2 != 0:
        print('Result:', int(num1) * (int(num2) ** 0.5))
    else:
        print('Error: It is zero or negative value')
 elif choice == '7':
    if num2 != 0:
        print('Result:', int((int(num1) / int(num2)) * 100), '%')
    else:
        print('Error: Divided by zero')
 elif choice == '8':
    print('Result:', float('{:.2f}'.format((int(num1) ** 2 + int(num2) ** 2) ** 0.5)))
 elif choice == '9':
    print('Exiting...')
    break
 else:
    print('Invalid input, try again!')