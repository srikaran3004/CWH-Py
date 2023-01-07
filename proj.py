print("Enter the range(Natural numbers")
upper_limit=int(input("From:"))
lower_limit=int(input("To:"))
total_p_no=0
total_c_no=0
for r in range(upper_limit,lower_limit+1):
    if r<1:
        print("Enter a valid range")
        break
    elif r==1:
        print("! is neither prime nor composite")
    elif r >1:
        for n in range(2,r):
            if r%n ==0:
                print(r,"is composite")
                total_c_no+=1
                break
        else:
            print(r,'is prime')
            total_p_no+=1

print("Total prime  numbers",total_p_no)
print("total composite numbers",total_c_no)