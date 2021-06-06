import datetime

filename = "acwr.txt"
workloads = []
thresholdMax = 1.40
thresholdMin = 0.80 

def writeNewData():
    f = open(filename, 'a')

    numberOfSessions = int(input("Enter the number of sessions"))
    sessionDuration = 0
    sessionIntensities = 0
    dayWorkload = 0

    for i in range(numberOfSessions):

        sessionDuration = int(input("Enter session {} duration".format(i)))
        sessionIntensity = int(input("Enter session {} intensity".format(i)))
        dayWorkload = dayWorkload + sessionDuration * sessionIntensity

    timing = datetime.datetime.now()

    outputString = str(dayWorkload) + " {}\n".format(timing)

    f.write(outputString)

def readData():
    
    stringRead = ""
    counter = 0

    f = open(filename, 'r')
    
    for line in f:
        stringRead = line
        if stringRead != '' :
            t = stringRead.split()
            print(t)
            workloads.append(int(t[0]))

def checkWorkload():

    sevenDayAverage = 0

    for i in range(7):
        sevenDayAverage = sevenDayAverage + workloads[-1-i] 

    sevenDayAverage = sevenDayAverage / 7

    twentyEightDayAverage = 0

    for i in range(28):
        twentyEightDayAverage = twentyEightDayAverage + workloads[-1-i] 
    
    twentyEightDayAverage /= 28

    workloadNumber = sevenDayAverage / twentyEightDayAverage

    if workloadNumber < thresholdMin :
        print("You are in danger of undertraining {}".format(workloadNumber))

    elif workloadNumber > thresholdMax :
        print("You are in danger of overtraining {}".format(workloadNumber))

    else :
        print("Perfect zone {}".format(workloadNumber))


readData()
checkWorkload()