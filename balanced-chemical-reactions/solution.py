def isBalancedReaction(reaction):
    left, right = reaction.split(" -> ")

    leftMols = left.split(" + ")
    rightMols = right.split(" + ")

    leftCount = dict()
    rightCount = dict()

    # count the molecules on each side
    for mol in leftMols:
        chems = chemCount(mol)
        addChemCountToTotal(leftCount, chems)

    for mol in rightMols:
        chems = chemCount(mol)
        addChemCountToTotal(rightCount, chems)
    
    # verify that counts dicts are the same
    for key in leftCount:
        if key not in rightCount or rightCount[key] != leftCount[key]:
            return False
    
    for key in rightCount:
        if key not in leftCount or rightCount[key] != leftCount[key]:
            return False

    return True

def addChemCountToTotal(totalCount, chemCount):
    for key in chemCount:
        if key in totalCount:
            totalCount[key] += chemCount[key]
        else:
            totalCount[key] = chemCount[key]

def chemCount(molecule):
    res = molecule.split(" ")
    if len(res) > 1:
        multiplier = int(res[0])
        mol = res[1]
    else:
        multiplier = 1
        mol = res[0]

    elems = {}
    currElem = ""
    currElemMult = 1

    i = 0
    while i < len(mol):
        char = mol[i]
        if char.isupper():
            if len(currElem) > 0:
                addToDict(elems, currElem, multiplier * currElemMult)
            currElem = char
            currElemMult = 1
        
        if len(currElem) > 0:
            if mol[i:i+2].isdigit():
                currElemMult = int(mol[i:i + 2])
                i += 1
            elif char.isdigit():
                currElemMult = int(char)
            elif not char.isupper():
                currElem += char

        i += 1
    if len(currElem) > 0:
        addToDict(elems, currElem, multiplier * currElemMult)
    currElem = char
    currElemMult = 1
    return elems

def addToDict(dicti, key, increment):
    if key in dicti:
        dicti += increment
    else:
        dicti[key] = increment
