ans = []
n=10000
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        ans.append("FizzBuzz")
    elif i % 3 == 0:
        ans.append("Fizz")
    elif i % 5 == 0:
        ans.append("Buzz")
    else:
        ans.append(str(i))
counter = 1
for x in ans:
    print(f"fizzy.put({counter}, \"{x}\");")
    counter+=1