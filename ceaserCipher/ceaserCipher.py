import time


PATH = 'ceaserCipher.txt'

# This function takes in a string as a parameter it then
# opens the file located at the PATH global variable in 
# write mode. Finally it writes the message input into 
# the file and closes the file. 
#
# Note: the write method used in the function wipes the 
#       contents of the file being written to.
def writeToFile(msg):
    fileWrite = open(PATH, "w")
    fileWrite.write(msg)
    fileWrite.close()

# This function takes in a string and checks to make sure that it
# contains only characters that are valid for OTP.
def checkValidCharacters(string):
    allowedCharacters = set(('ABCDEFGHIJKLMNOPQRSTUVWXYZ '))
    isValid = set((string.upper()))
    return isValid.issubset(allowedCharacters)

# This function takes in a string parameter 'string' and splits it into two parts based on the delimiter '!0!'.
# The first part represents the 'shift' value and the second part represents the 'message'.
# the function returns a tuple containing the 'shift' and 'message' values.
# 
# Note: if the input string does not contain the delimiter '!0!'
#       this function will raise an IndexError.
def splitShiftAndMessage(string):
    splitString = string.split('!0!')
    shift = splitString[0]
    message = splitString[1]
    return (shift, message)

# This function takes a string and returns a list of integers representing the alphabetical 
# indices of each character in the string. The input string is assumed to contain only 
# alphabetic characters (A-Z) and spaces. The function converts the input string to 
# uppercase and maps spaces to integer 26.
def stringToAlphIndexArr(string):
    string = string.upper()
    result = []
    for character in string:
        if ord(character) == 32:
            result.append(26)
        else:
            result.append((ord(character) - 65))
    return result

# This function takes a list of integers and returns a string representation of the 
# corresponding alphabets. The input list is assumed to contain only integers between 0 and 26, 
# inclusive.
#  
# Note: The function replaces integer 26 with -33 to handle the space character.
def alphNumberArrToString(arr):
    result = ''
    i = 0
    while i < len(arr):
        if arr[i] == 26:
            arr[i] = -33
        asciiValue = chr(arr[i] + 65)
        result += asciiValue
        i += 1
    return result

# This function takes a list of integers 'charArr' and an integer 'shift', and returns a new 
# list of integers representing the characters in 'charArr' shifted by 'shift'. Integer 26 is 
# used to represent the space character. The resulting list contains integers between 0 and 25, 
# inclusive, as they represent the shifted alphabetical indices.
def applyShift(charArr, shift):
    result = []
    for character in charArr:
        if character == 26:
            result.append(26)
        else:
            character = (character + int(shift)) % 26
            result.append(character)
    return result

def main():
    print("\nCEASER CIPHER    \n    By: Taijen Ave-Lallemant    \n")
    fileRead =  open(PATH, "r")
    textInFile = ''
    previousOutput = ''

    while True: 
        time.sleep(1.0)
        fileRead.seek(0,0)
        textInFile = fileRead.readline()
        if textInFile != previousOutput:
            match textInFile:

                case "exit":
                    print('EXITING PROGRAM')
                    writeToFile('')
                    break
            
                case _:
                    print('input: ' + textInFile)
                    processedInput = splitShiftAndMessage(textInFile)
                    shift = processedInput[0]
                    message = processedInput[1]
                    messageIntArr = stringToAlphIndexArr(message)
                    shiftedMessageIntArr = applyShift(messageIntArr, shift)
                    previousOutput = alphNumberArrToString(shiftedMessageIntArr)
                    writeToFile(previousOutput)
                    
main()