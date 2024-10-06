while 1:
    try:
        a,b = list(map(int,input().split()))
    except:
        break
    
    if b == 1:
        print("Boring!")
        continue
    
    out = str(a)
    while a > 1:
        x = a/b
        if a == x*b and x% b == 0:
            a = int(x)
            out = f"{out} {a}"
        elif x == 1:
            out += " 1"
            break
        else:
            out = "Boring!"
            break
    print(out) 
