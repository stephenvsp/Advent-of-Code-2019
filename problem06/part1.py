with open('problem6_input') as file:
    orbits = file.readlines()

# strip \n's out of strings
orbits = [orbit.strip() for orbit in orbits]

orbitMap = {}

for orbit in orbits:
    orbitee, orbital = orbit.split(')')

    # orbitee is not in the map already
    if (orbitee not in orbitMap):
        orbitMap[orbitee] = (0, [orbital])
    # else the orbitee is in the map and the orbital needs to be added
    else:
        depth, orbitalList = orbitMap[orbitee]
        orbitalList.append(orbital)

        orbitMap[orbitee] = (depth, orbitalList)


def updateDepth(currDepth, currOrbitee):
    depth, orbitalList = orbitMap[currOrbitee]

    # update depth in KVP
    orbitMap[currOrbitee] = currDepth, orbitalList

    # if there is something in the orbital list we can continue the recursive call
    for orbital in orbitalList:
        if orbital in orbitMap:
            updateDepth(currDepth + 1, orbital)
        else:
            orbitMap[orbital] = (currDepth + 1, [])


# updates depth starting at the base depth of COM
updateDepth(0, 'COM')

totalOrbits = 0

for key in orbitMap.keys():
    depth, orbitalList = orbitMap[key]

    totalOrbits += depth

print(totalOrbits)
