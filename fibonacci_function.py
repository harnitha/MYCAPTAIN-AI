def fibo(k):
  temp=0
  temp1=1
  print(temp,end=",")
  print(temp1,end=",")
  for i in range(0,k-2):
    sum=temp+temp1
    print(sum,end=",")
    temp,temp1=temp1,sum


fibo(int(input()))
