import time


PATH = 'otpMicroservice.txt'


def writeToFile(msg):
    fileWrite = open(PATH, "w")
    fileWrite.write(msg)
    fileWrite.close()

"""
This function takes in a string and checks to make sure that it
contains only characters that are valid for OTP.
"""
def checkValidCharacters(string):
    allowedCharacters = set(('ABCDEFGHIJKLMNOPQRSTUVWXYZ '))
    isValid = set((string.upper()))
    return isValid.issubset(allowedCharacters)

"""
This function checks the validity of a given key by verifying that it contains only valid
characters, is all uppercase, and is at least as long as the message to be encoded. If the
key is valid, the function returns True. If the key is invalid, the function writes an error
message to a file and returns a tuple containing False and the error message.
"""
def checkKeyValidity(key, messageLength):
    errorMessage = 'ERROR: Invalid Key | Please use a Key from the Key Generator'
    if checkValidCharacters(key) and key.isupper() and len(key) >= messageLength:
        return True
    writeToFile(errorMessage)
    return (False, errorMessage)

"""
This function checks the validity of a given message by verifying that it contains only valid
characters (A-Z and space). If the message is valid, the function returns True. If the
message is invalid, the function writes an error message to a file and returns a tuple
containing False and the error message.
"""
def checkMessageValidity(message):
    errorMessage = 'ERROR: Invalid Message | Only A-Z and Space characters are Acceptable'
    if checkValidCharacters(message):
        return True
    writeToFile(errorMessage)
    return (False, errorMessage)

"""
This function takes a string and splits it into three parts: the type of encryption, the key,
and the message to be encrypted. The string is assumed to be in a specific format where the
parts are separated by the string '!0!'. The function returns a tuple containing the three
parts.
"""
def splitKeyAndMessage(string):
    splitString = string.split('!0!')
    type = splitString[0]
    key = splitString[1]
    message = splitString[2]
    return (type, key, message)

"""
This function checks the validity of a given key and message by calling the functions
checkMessageValidity and checkKeyValidity. If both the message and the key are valid, the
function returns True. If either the message or the key is invalid, the function returns a
tuple containing False and the corresponding error message.
"""
def checkGoodInput(key, message):
    if checkMessageValidity(message) == True:
        if checkKeyValidity(key, len(message)) == True:
            return True
        else:
            previousOutput = checkKeyValidity(key, len(message))[1]
            return (False, previousOutput)
    else:
        previousOutput = checkMessageValidity(message)[1]
        return (False, previousOutput)
    
"""
This function takes a string and returns a list of integers representing the alphabetical
indices of each character in the string. The input string is assumed to contain only
alphabetic characters (A-Z) and spaces. The function converts the input string to uppercase
and maps spaces to integer 26. The resulting list contains integers between 0 and 26,
inclusive, as they represent the alphabetical indices of the characters.
"""
def stringToAlphIndextArr(string):
    string = string.upper()
    result = []
    for character in string:
        if ord(character) == 32:
            result.append(26)
        else:
            result.append((ord(character) - 65))
    return result

"""
# This function takes a list of integers representing alphabetical indices and returns a string 
# by mapping the indices to their corresponding uppercase alphabetical characters. The function 
# assumes the input list contains integers between 0 and 26, inclusive, where integer 26 
# represents a space. Function loops over each integer in the input list, maps it to its 
# corresponding alphabetical character, and appends it to a string. 
# If the integer is 26, it is temporarily mapped to -33 before being converted to a character.
"""
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

"""
This function encrypts a message using a key, both assumed to contain only alphabetic 
characters and spaces. It converts the message and key to lists of alphabetical indices, adds 
the corresponding indices of the message and key, and maps the resulting list to uppercase 
alphabetical characters to return an encrypted message.
"""
def encrypt(message, key):
    messageNumberArr = stringToAlphIndextArr(message)
    keyNumberArr = stringToAlphIndextArr(key)
    resultNumberArr = []
    i = 0
    while i<len(messageNumberArr):
        resultNumberArr.append((messageNumberArr[i] + keyNumberArr[i]) % 27)
        i+=1
    encryptedMessage = alphNumberArrToString(resultNumberArr)
    return encryptedMessage

"""
This function decrypts a message that has been previously encrypted using a key. It converts 
the message and key to lists of alphabetical indices, subtracts the corresponding indices of the 
key from the message, and maps the resulting list to uppercase alphabetical characters to return 
the original message. Both the message and the key are assumed to contain only alphabetic 
characters and spaces.
"""
def decrypt(message, key):
    messageNumberArr = stringToAlphIndextArr(message)
    keyNumberArr = stringToAlphIndextArr(key)
    resultNumberArr = []
    i = 0
    while i<len(messageNumberArr):
        valueAfterCombination = messageNumberArr[i] - keyNumberArr[i]
        if valueAfterCombination < 0:
            valueAfterCombination += 27     
        resultNumberArr.append(valueAfterCombination)
        i+=1
    decryptedMessage = alphNumberArrToString(resultNumberArr)
    return decryptedMessage

def main():

    print("\nOTP Micro-Service    \n    By: Taijen Ave-Lallemant    \n")
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
                    processedKeyAndMessage = splitKeyAndMessage(textInFile)
                    type = processedKeyAndMessage[0]
                    key = processedKeyAndMessage[1]
                    message = processedKeyAndMessage[2]
                    print(type)
                    if checkGoodInput(key, message) == True:
                        if type == 'encrypt':
                            previousOutput = encrypt(message, key)
                        else:
                            previousOutput = decrypt(message, key)
                        writeToFile(previousOutput)
                    else:
                        previousOutput = checkGoodInput(key, message)[1]
                        print('output: ' + previousOutput)

main()