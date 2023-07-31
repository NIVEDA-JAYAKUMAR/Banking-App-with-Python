import math
print("Welcome to TRUE BANK")
def signin():
    global name #username
    global pin  #password
    global cb   #current balance
    name = str(input("please create your username : "))
    pin = str(input("please create your 6 digits pin : "))
    if len(pin) == 6:
        pin = pin
    else:
        print("The pin has to be 6 digits")
        newpin = str(input("Please create yout 6 digits pin"))
        if len(newpin) !=6:
            print("The pin has to be 6 digits")  
            signin()
        else:
            pin = newpin
    print("Thanks for creating your bank account")

def forgotpin():
    recoverpin = str(input("Plpease create your new 6 digits pin"))
    if len(recoverpin) != 6:
        print("The pin has to be in 6 digits")
        forgotpin()
    else:
        print("The pin has been stored, please log in")    
        pin = recoverpin
        login()        

def depositinsterest( p, r, t):
    # A = Pe^(rt) wwhich is the formula for the calculating the compund interest 
    p=float(p)
    r= float(r)
    t= float(t)
    rt = r * t
    e = math.exp(rt)
    #calculation
    a = p * e #fututre value of your investment
    return a 

def login():
    name1 = str(input("please enter your username"))
    pin1 = str(input("please enter the correct pin"))
    if name1 == name and pin1 == pin:
        print("welcome to the online banking application" + " " + name)
        print("please choose the menu down here")
        listmenu = ["1-Deposit", "2-Withdraw","3-Transfer","4-Cheack Balance","5-Deposit interest rate","6-Calculate compound interest"]         
        for b in listmenu:
            print(b)
        choose = int(input("Please enter of your choice "))
        d = 0 #deposit
        w = 0 #withdraw
        cb = 0 #current balance     
        if choose == 1:
            d= int(input("Enter the amount of your deposit"))
            cb = d
            print("Your current balance"+" "+ str(cb))
        elif choose == 2:
            w = int(input("Enter the amount of money that you want to withdraw"))
            if w > cb:
                print("Your current balance is not sufficient for this transaction")
                login()
            else:
                cb =  d - w
                print(str(w) + " " + "has been withdrawn from your account"+" "+"Your current balance is"+" "+ str(cb))
        elif choose == 3:
            dest = str(input("Please enter the account number of your destination in 8 digits"))       
            if len(dest) == 8:
               amount = int(input("Please enter the amount of money that you want to transfer"))
               if amount > cb:
                   print("Your current balance is not sufficient for this transaction")
                   login()
               else:
                   cd = d - amount
                   print("The amount of money that you have transfered is"+" "+ str(amount) + " "+"to the account number of"+" "+ str(dest) + " "+"Your current balance is"+" "+ str(cd))
            else:
                print("The transaction has been rejected since the destination account number is invalid")   
                login()
        elif choose == 4:
            print("Your current balance is"+" "+ str(cb))
        elif choose == 5:
            if d > 50000:
              rate = 3
            elif d > 10000:
                  rate = 2
            else:
                  rate = 1.5      
            print("your current deposit interest rate is"+" "+ str(rate)+"%")
        elif choose == 6:
            listoption = ["1-Calculate your deposit compound interest based on your CB","2-Calculate your deposit compound interest based on your deposit"]
            for n in listoption:
                print(n)
            choice = int(input("Please enter your choice from the option above"))
            if choice == 1:
               timing = str(input("how many years you want to invest your money"))
               if d > 50000:
                   ratex = 3/100
               elif d > 30000:
                   ratex = 2/100
               else:
                   ratex = 1.5/100
               print("Your current balance in"+" "+ timing + " " + "years will be")
               print(depositinsterest(cb,ratex,timing))
        elif choice == 2:
            timing1 = str(input("how many years you want to invest your money"))
            money = str(input("Please enter the amount of money you would like to deposit"))
            money = int(money)
            if d > 50000:
                   ratex = 3/100
            elif d > 30000:
                   ratex = 2/100
            else:
                   ratex = 1.5/100
            print("Your current balance in"+" "+ timing + " " + "years will be")
            print(depositinsterest(money,ratex,timing))
        else:
            print("option is not available, back to main menu")
            login()           
    else:
         print("either of your username or pin is wrong, did you create your account")
         list1 = ["1 - yes","2 - no"] 
         for i in list1:
             print(i)
         inp = int(input("enter your choice below"))
         if inp==1:
             list2 = ("1-Do you want to attempt to log in again","2-You forget your pin")
             for e in list2:
                 print(e)
             theanswer = str(input("please enter your choice"))
             theanswer = int(theanswer)
             if theanswer == 1:
                 login()
             elif theanswer ==2:
                 forgotpin()
             else:
                 print("option is not available")    
                 login()  
         elif inp == 2:
             print("please create your accoount")
             signin()
            
def mainmenu():
    optionone = int(input("Choose 1 to sign in and choose 2 to log in")) 
    if optionone == 1:
       signin()   
    elif optionone == 2:
       login()    
    else:
        print("Option is not available")
        mainmenu()
    
    exit()
    
def exit():
    answer = str(input("Do you still want to conduct transaction ? yes or no"))
    if answer == "yes":
        login()
    elif answer == "No":
        print("Thank you for using this app")
    else:
        print("Option is not available")
        mainmenu()         
mainmenu()