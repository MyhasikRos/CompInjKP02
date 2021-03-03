
try:
    maxNorm = 50
    print("Start distance: ")
    distancePerDay = float(input())
    if distancePerDay < 0:
        raise ValueError
    print("Daily gain: ")
    dayGain = int(input())
    if dayGain < 0:
        raise ValueError
    daysGone = 0
    while maxNorm >= distancePerDay:
        distancePerDay += distancePerDay * dayGain / 100
        daysGone += 1
    print("It took %d days" % (daysGone))
except ValueError:
    print("Wrong input")
