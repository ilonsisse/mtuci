arr = [i for i in range (1, 51)]
arr.sort(reverse=True)
for i in range(len(arr) - 3):
    a = arr[i]
    b = arr[i+1]
    c = arr[i+2]
    if a+b>c and a+c>b and b+c>a:
        p = (a+b+c)/2
        s = (p*(p-a)*(p-b)*(p-c))**0.5
        print(a, b, c, s)
        break
