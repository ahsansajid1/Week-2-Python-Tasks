# Safe int input loop.

while True:

    user_input= input('Enter a number :')
    try:
        number=int (user_input)
        print("Thank you ! You entered ", number)
        break
    except ValueError:

        print('invaild number! Please enter a valid number')
    


#  File opening code 
try:
    file= open ("summary_week2.txt", "r")
    content= file.read()
    print("File Content")
    print(content)
    file.close()

except FileNotFoundError:
    print('Print file fount yet, try again')

except Exception as e:
    print('An unexpected error occured:', e)