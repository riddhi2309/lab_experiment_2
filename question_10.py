# 1 day = 24 hours = 86400 second(24*60*60)
day = int(input("enter the data :-"))
hours = int(day/(60*60))   #one hour is equal to 3600 second 
minute = int(day%(60*60)/60)        #on minute is equal to 60 second
second = int(day%(60*60)%60)
print(hours," hours ", minute , " minutes " , second , " second " )
