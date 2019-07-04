s3,u4=map(int,input().split())
m=1
while(m<=s3 and m<=u4):
 if(s3%m==0 and u4%m==0):
  gcd1=m
 m=m+1
print(gcd1)
