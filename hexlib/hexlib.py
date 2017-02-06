
def translateChar (inputChar):
  if str.isdigit(inputChar):
    return int(inputChar)
  elif (inputChar == "a" or inputChar == "A"):
    return 10
  elif inputChar == "b" or inputChar == "B":
    return 11
  elif inputChar == "c" or inputChar == "C":
    return 12
  elif inputChar == "d" or inputChar == "D":
    return 13
  elif inputChar == "e" or inputChar == "E":
    return 14
  elif inputChar == "f" or inputChar == "F":
    return 15
  return 0


def convertHexStringToDecimal (hexString):
  result = 0

  strLen = len(hexString)
# print ("strLen: {0}".format (strLen))
  range3 = range(strLen, 0, -1)
# print ("range3: {0}".format (range3))
  reversedStr = hexString[::-1]
  
  for currIndex in range3:
    adjustedIndex = currIndex -1
    print ("adjustedIndex: {0}".format (adjustedIndex))
    currMultiplier = 16 ** adjustedIndex
    print ("currMultiplier: {0}".format (currMultiplier))
    currDecimal = translateChar (reversedStr[adjustedIndex])
    print ("currDecimal: {0}".format (currDecimal))
    currPositionalResult = currMultiplier * currDecimal
    print ("currPositionalResult: {0}".format (currPositionalResult))
    result += currPositionalResult
    print ("result: {0}".format (result))
  
  return result
    
    
testString = 'cafedecaf'  
decimalValue = convertHexStringToDecimal (testString)

print ("final value of testString '{0}': {1}".format (testString, decimalValue))
