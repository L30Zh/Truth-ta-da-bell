


rideHeightOK = False
withAdult = False
healthHold = False

Dia = input("Are you tall enough for this ride? (yes/no) ")

if Dia == ("yes"):
    rideHeightOK = True
else:
    withAdult = input("Are you here with an adult? (yes/no) ")
    if withAdult == ("yes"):
        withAdult = True

healthHold = input("Do you have any health issues? (yes/no) ")
if healthHold == ("yes"):
    healthHold = True

if healthHold == True:
    print("Nah get out")
elif rideHeightOK or withAdult == True:
    print("alr get on")
else:
    print("Nah get out")















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