
rideHeightOK = any
withAdult = any
healthHold = any
CanRide =  any


Dia = input ("are you tall enough for this ride?")
if Dia == ("yes"):
    rideHeightOK == True
    input ("Do you have any health issues?")
    if input == ("no"):
        healthHold == False
    elif input == ("yes"):
        healthHold == False
else:
    input ("Are you here with an adult?")
    if input == ("yes"):
        withAdult == True
        input ("Do you have any health issues?")
        
    elif input == ("no"):
        withAdult == False
    if input == ("no"):
        healthHold == False
    elif input == ("yes"):
        healthHold == True

if healthHold == True:
    print("Nah get out")
elif withAdult or rideHeightOK == True:
    print("alr get on")



""" if rideHeightOK == True and healthHold == False:
    CanRide == True
if rideHeightOK == True and healthHold == True:
    CanRide == False
if rideHeightOK == False and withAdult == True and healthHold == False:
    CanRide == True
if rideHeightOK == False and withAdult == True and healthHold == True:
    CanRide == False
if rideHeightOK == False and withAdult == False:
    CanRide == False

if CanRide == True:
    print("You can ride")
else:
    print("You are not permitted to ride")

 """