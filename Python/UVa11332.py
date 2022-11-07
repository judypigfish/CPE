While(1):
  a = input()
  if a=="0":
    break
  
  while(len(a)>1):
    x=0
    for i in range(len(a)):
      x += int(a[i])
     a = str(x)
  print(a)
