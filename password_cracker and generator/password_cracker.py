from random import *
user_pass=input("Enter the password :").lower()
random_letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0']
guss=''
count_pass=0
while guss != user_pass:
    guss=''
    for letters in range(len(user_pass)):
        guss_pass=random_letters[randint(0,25)]
        guss=str(guss_pass) + str(guss)
    count_pass+=1
    print(guss)

print(f"your paswword was founded :{guss}")
print(count_pass)