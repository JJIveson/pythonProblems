# Write method that returns true if two input strings are anagrams of each other.
def isAnagram(string1, string2):
    s = "".join(sorted(string1.lower()))
    d = "".join(sorted(string2.lower()))

    if s == d:
        return True
    else:
        return False


# Write a method which accepts array of strings and returns true if they're all anagrams.
def isArrayOfAnagrams(inputArray):
    if len(inputArray)<2:
        return False
   
    for count in range(0,len(inputArray)):
        sortedPrevious =''
        if count>0:
            sortedPrevious = "".join(sorted(inputArray[count-1].lower()))
            sortedCurrent = "".join(sorted(inputArray[count].lower()))
           
            if sortedPrevious != sortedCurrent:
                return False
    return True


# Write a method that returns true if two input strings are nearly anagrams of each other.
def isNearlyAnagram(s1, s2):
	#defined as 1 char difference between each
    sortedS1 = sorted(s1.lower())
    sortedS2 = sorted(s2.lower())
   
    map1 = getCharFrequencyMap(s1)
    map2 = getCharFrequencyMap(s2)

    if map1==map2:
        return True

    return isNearlyEqualComparison(map1, map2) and isNearlyEqualComparison(map2, map1)    
    
def isNearlyEqualComparison(leftMap, rightMap):
    differenceCount = 0
    for leftMapKey in leftMap:
        if leftMapKey not in rightMap:
            if leftMap[leftMapKey]>=2 or differenceCount==1:
                return False
            else:
                differenceCount=1        
        elif leftMap[leftMapKey]!=rightMap[leftMapKey]:      
            if leftMap[leftMapKey]-rightMap[leftMapKey]>=2 or differenceCount==1:
                return False
            else:
                differenceCount=1
    return True
   
def getCharFrequencyMap(inputString):
    arrayOfChars = sorted(inputString.lower())

    returnMap = {}
    for count in range(0,len(arrayOfChars)):
        key = arrayOfChars[count]
        if key in returnMap:
            valueForKey = returnMap[key]
            valueForKey = valueForKey+1
            returnMap[key] = valueForKey
        else:    
            returnMap[arrayOfChars[count]] = 1

    return returnMap


# Write a method that returns true if two input strings have the same number of vowels and consonants.
def isSameNumberOfVowelsAndConsonants(s1, s2):
	if(len(s1)!=len(s2)):
		return False
	if(countVowels(s1)==countVowels(s2)):
	    return True
	else:
	    return False  
    
def countVowels(inputString):
    inputStringArr = list(inputString)
    vowelCount = 0
    for i in range(0, len(inputStringArr)):
        if isVowel(inputStringArr[i]):
            vowelCount=vowelCount+1
    return vowelCount
   
def isVowel(char1):
    if char1=='a' or char1=='e' or char1=='i' or char1=='o' or char1=='u':
        return True
    return False
if __name__ == "__main__":	
    assert isAnagram("abcd", "abdc")==True, "FAILED"
    assert isAnagram("abcd", "abbc")==False, "FAILED"
    assert isAnagram("def", "ffe")==False, "FAILED"
   
    assert isArrayOfAnagrams(['aa'])==False, "FAILED"    
    assert isArrayOfAnagrams(['aa','aa'])==True, "FAILED"    
    assert isArrayOfAnagrams(['abcd','dcba','adcb'])==True, "FAILED"    
    assert isArrayOfAnagrams(['abc','cba','acb'])==True, "FAILED"    
    assert isArrayOfAnagrams(['abc','cba','acbb'])==False, "FAILED"    

    assert isNearlyAnagram('a','aa')==True, "FAILED"
    assert isNearlyAnagram('a','aaa')==False, "FAILED"
    assert isNearlyAnagram('acbd','cabd')==True, "FAILED"
    assert isNearlyAnagram('acbd','cabde')==True, "FAILED"
    assert isNearlyAnagram('acbde','cabd')==True, "FAILED"
    assert isNearlyAnagram('acbdee','cabd')==False, "FAILED"
    assert isNearlyAnagram('acbd','cabdee')==False, "FAILED"
    assert isNearlyAnagram('acbdd','cabd')==True, "FAILED"
    assert isNearlyAnagram('acbddd','cabd')==False, "FAILED"
    assert isNearlyAnagram('acbddd','cabddddd')==False, "FAILED"
    assert isNearlyAnagram('acbddd','cabcdddd')==False, "FAILED"
    assert isNearlyAnagram('basiparachromatin','marsipobranchiata')==True, "FAILED"
    
    assert isSameNumberOfVowelsAndConsonants('a','aa')==False, "FAILED"
    assert isSameNumberOfVowelsAndConsonants('a','a')==True, "FAILED"
    assert isSameNumberOfVowelsAndConsonants('ad','ae')==False, "FAILED"
