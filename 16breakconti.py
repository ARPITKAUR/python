# with break it leaves the loop
for i in range(10):
    if(i==5):
      break 
    print('5 x' , i, '=', 5*i)

#   with continue it only leaves the iteration i.e skips only that partivular iteration
for j in range(12):
   if(j==6):
      print("6 has been skipped ")
      continue
   print('5 X' , j, "=", 5*j)
    
    