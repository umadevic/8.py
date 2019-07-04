uma=list(input())
xy=[]
for i in uma:
 if i not in xy:
  xy.append(i)
if(uma==xy):
 print("Yes")
else:
 print("No")
