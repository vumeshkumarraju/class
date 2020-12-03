#write description

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("PLEASE ENTER A STRING FOR CHECKING.\n")
input_string=input("PLEASE ENTER A STRING :- ")

def function_vowel_count(a):
    count=0
    vowel=['a','e','i','o','u','A','E','I','O','U']
    for i in vowel:
        for j in a:
            if i==j:
                count+=1
    print("NUMBER OF VOWELS IN YOUR ENTERED STRING IS = ",count)
def function_digit_count(a):
    count=0
    for i in a:
        if i.isdigit():
            count+=1
    print("NUMBER OF DIGITS IN YOUR ENTERED STRING IS = ",count)

function_vowel_count(input_string)
function_digit_count(input_string)
