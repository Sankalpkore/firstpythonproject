from num2words import num2words

number = input("Enter Your Number : ")

try:
    number = int(number)
    word_form = num2words(number)
    print("In Word Form :",word_form)
except ValueError:
    print("Please Enter A Proper Integer")
