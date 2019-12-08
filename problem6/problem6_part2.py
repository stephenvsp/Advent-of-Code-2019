with open('problem6_input') as file:
    orbits = file.readlines()

# strip \n's out of strings
orbits = [orbit.strip() for orbit in orbits]

orbitMap = {}

for orbit in orbits:
    orbitee, orbital = orbit.split(')')

    # orbitee is not in the map already
    if (orbitee not in orbitMap):
        orbitMap[orbitee] = (0, '', [orbital])
    # else the orbitee is in the map and the orbital needs to be added
    else:
        orbitMap[orbitee][2].append(orbital)


def updateDepthAndParentNode(currDepth, currOrbitee, currParent):
    # update depth and parent of current node in KVP
    orbitMap[currOrbitee] = currDepth, currParent, orbitMap[currOrbitee][2]

    # if there is something in the orbital list we can continue the recursive call
    for orbital in orbitMap[currOrbitee][2]:

        if orbital in orbitMap:
            updateDepthAndParentNode(currDepth + 1, orbital, currOrbitee)
        else:
            orbitMap[orbital] = (currDepth + 1, currOrbitee, [])


updateDepthAndParentNode(0, 'COM', '')

youParents = []
currNode = 'YOU'

while(currNode != 'COM'):
    parent = orbitMap[currNode][1]
    youParents.append(parent)
    currNode = parent

santaParents = []
currNode = 'SAN'

while(currNode != 'COM'):
    parent = orbitMap[currNode][1]
    santaParents.append(parent)
    currNode = parent

similarNodes = list(set(youParents) & set(santaParents))

deepestSimilarNode = max(similarNodes, key=lambda item: orbitMap[item][0])

distanceFromYouToSanta = orbitMap['YOU'][0] + \
    orbitMap['SAN'][0] - (orbitMap[deepestSimilarNode][0] * 2)

# subtract two because its actually distance from you's and santa's parents
print(distanceFromYouToSanta - 2)
