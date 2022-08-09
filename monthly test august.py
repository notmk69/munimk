


from os import mkdir


marks=0

print("MONTHLY TEST AUGUST") 
while True:                                  
       name=(input("enter your name:"))
       if name.isalpha() is True:
        break
       else: print("please enter alphabets only")
       continue
while True:                                        
       rollno=(input("enter your rollnumber:"))
       if rollno.isnumeric() is True:
        break
       else: print("please enter numbers only")
       continue
print("question number 1")
answer=int(input("1-10 how sus is amogus"))
if answer>=10:
    print("yessir no cap");newmarks=marks+1
else: print("BOO HOO FKIN LOSER");newmarks=marks                
moveon=int(input("next question? 1/0"))
if moveon==1: 
    print("question number 2")
answer2=int(input("is water wet? 1/0"))
if   answer2==1: 
      newmarks2=newmarks+1    
else: newmarks2=newmarks

result=int(input("do you want to reveal the result? 1/0"))
if result==1:
            print(name);print(rollno)
            print("your final marks are :",newmarks2)
            print("thank you for taking the test")
else: print("thank you for taking the test")            
