def countingValleys(steps):
    level = valley = 0   #уровень моря и количество долин

    for i in steps:
        if i == 'U':
            level += 1
        else:
            level -= 1

        if i == 'U' and level == 0:
            valley += 1

    return valley
print(countingValleys(['D','D','U','U','U','U','D','D']))

