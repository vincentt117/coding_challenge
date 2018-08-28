# Aug 26, 18
# Palantir Fall '18 Summer Internship HR challenge

# Sample Input:
# John Sick PA LO DC
# Kelly Recovering PA DC DC
# Linda Healthy PA PA DC


import sys

def readFromSTDIN():
    numLinesToRead = int(sys.stdin.readline())
    details = {}
    states = set()
    usedSites = {} # Diciontary with bool value indicating whether site contains a sick employee

    print()

    for i in range(numLinesToRead):
        tempDetail = list(sys.stdin.readline().split())
        # Print all emp names
        print(tempDetail[0] + " ", end='')
        states.add(tempDetail[1])
        details[tuple(tempDetail[:2])] = tempDetail[2:]

    print()

    daysPassed = 0

    for j in details:
        # Print the first state of each employee
        print(j[1] + " ", end='')


    # Continue to go through the days so long as not all emps are healthy
    while states != {"Healthy"} and daysPassed < 365:
        print()
        states = set()
        # See if a site contains a sick employee
        for j in details:
            if details[j][daysPassed % len(details[j])] in usedSites:
                if j[1] == "Sick":
                    usedSites[details[j][daysPassed % len(details[j])]] = True
            else:
                usedSites[details[j][daysPassed % len(details[j])]] = (j[1] == "Sick")
        newDetails = {}
        # Move all employees to the next site and print their state
        for k in details:
            # If a person was sick, change into recovery
            if k[1] == "Sick":
                newDetails[tuple([k[0], "Recovering"])] = details[k]
                print( "Recovering" + " ", end='')
                states.add("Recovering")
                
            # If a person was recovery, change into healthy
            elif k[1] == "Recovering":
                newDetails[tuple([k[0], "Healthy"])] = details[k]
                print( "Healthy"  + " ", end='')
                states.add("Healthy")
            # If a person was healthy, do nothing, unless they were in an office with someone sick
            elif k[1] == "Healthy":
                if usedSites[details[k][daysPassed % len(details[k])]]:
                    newDetails[tuple([k[0], "Sick"])] = details[k]
                    print( "Sick" + " ", end='')
                    states.add("Sick")
                elif usedSites[details[k][daysPassed % len(details[k])]] == False:
                    newDetails[tuple([k[0], "Healthy"])] = details[k]
                    print( "Healthy" + " ", end='')
                    states.add("Healthy")
        details = newDetails
        usedSites = {}
        daysPassed += 1
    print()
    print(daysPassed)

readFromSTDIN()


