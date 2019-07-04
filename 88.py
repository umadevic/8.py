ge11,se11=map(int,input().split())
maxima=max(ge11,se11)
while(1):
 if(maxima%ge11==0 and maxima%se11==0):
  print(maxima)
  break
 maxima+=1
