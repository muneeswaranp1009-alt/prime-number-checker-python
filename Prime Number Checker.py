def prime_check(number):
    if number <= 1:
        return True
    
    limit = int(number ** 0.5) +1
    
    for i in range(2,number):
        if number % i == 0:
            return False
        
    return True

print("\n..............Prime Number Checker..................\n")
user_input = int(input("Enter Number to Check:"))

if prime_check(user_input):
    print(f"\n The Entered {user_input} is a Prime Number!\n")
else:
    print(f"\n The Entered {user_input} is Not a Prime Number!\n")