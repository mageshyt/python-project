choice=int(input("Enter the choice 0---->patten in correct order  or 1---->patten in reverse order :"))
patten=int(input("enter the number of pattend row you want : "))

if choice==bool(0):
    for i in range(0,patten+1):
        print(i*'*')
       
elif choice==bool(1):
     while patten>=0:
        print(patten*'*')
        patten-=1
        
    