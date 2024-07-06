'''
請撰寫一程式，依照使用者輸入的n，畫出對應的等腰中空三角形。
'''
n= int(input("輸入需要的行數:"))
i=1
while i<=n:
   j=1
   while j<=n-i:
      print(" ",end="")
      j+=1
   k=1
   while k<=2*i-1:
      if k==1 or k==2*i-1 or i==n:
          print("*",end="")  
      else:
          print(" ",end="")
      k+=1
   print("")
   i+=1
   