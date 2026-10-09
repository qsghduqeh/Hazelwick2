Rows=6
Seats=8

plan=[]

for i in range(Rows):
  plan.append(["0"*Seats])
  plan=[[0]*Seats for i in range(Rows)]
print(plan)