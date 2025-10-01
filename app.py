
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
        healthHold == True
    if rideHeightOK == True:
        input ("Do you have any health issues?")
        if input == ("yes"):
            healthHold == True
        else: 
            if input == ("no"):
                healthHold == False
else:
    input ("Are you here with an adult?")
    if input == ("yes"):
        withAdult == True
    else:
        if input == ("no"):
            healthHold == False
    if withAdult == True:
        input ("Do you have any health issues?")
        if input == ("yes"):
            healthHold == True
        else: 
            if input == ("no"):
                healthHold == False

if healthHold == True:
    print("Nah get out")
if withAdult or rideHeightOK == True and healthHold != True:
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