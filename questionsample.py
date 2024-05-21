import time
t=(time.strftime('%H:%M:%S'))
hour=int(time.strftime('%H'))
hour=int(input("enter the hour"))
print(hour)

if(hour<12):
    print("good morning")

elif(hour>=12 and hour<=15):
    print("good afternoon")
       
if(hour>15 and hour<20):
    print("good night")

else:
    print("good night")