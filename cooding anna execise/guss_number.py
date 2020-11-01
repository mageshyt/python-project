import random
random_number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
total_chance=5
reming_chance=0
guss_number=random.choice(random_number)
while True:
    user_guss=int(input("Enter the number between 1 to 20 :"))
    if total_chance<reming_chance:
        print("sorry u have lost the game")
        reming_chance+=1
        break
    elif guss_number== user_guss:
        print("you have won the ,collect your price from cooding anna 🤴")
        break
    elif  user_guss < guss_number:
        print("you have entered lesser than gusss number try again")
        reming_chance+=1
        continue
    elif guss_number< user_guss:
        print("you have execite the guss number try again")
        reming_chance+=1
    print(f"you have {total_chance+1-reming_chance} chance !")
    continue