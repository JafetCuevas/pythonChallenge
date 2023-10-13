{"filter":false,"title":"debug_caesar4.py","tooltip":"/debug_caesar4.py","undoManager":{"mark":5,"position":5,"stack":[[{"start":{"row":0,"column":0},"end":{"row":55,"column":24},"action":"insert","lines":["# Module Lab: Caesar Cipher Program Bug #4","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it.","","# Double the given alphabet","def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet","","# Get a message to encrypt","def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt","","# Get a cipher key","def getCipherKey():","    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")","    return shiftAmount","","# Encrypt message","def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + int(cipherKey)","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage","","# Decrypt message","def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, decryptKey, alphabet)","","# Main program logic","def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decrypted Message: {myEncryptedMessage}')","","# Main logic","runCaesarCipherProgram()"],"id":2}],[{"start":{"row":52,"column":34},"end":{"row":52,"column":35},"action":"remove","lines":["E"],"id":3}],[{"start":{"row":52,"column":34},"end":{"row":52,"column":35},"action":"insert","lines":["D"],"id":4},{"start":{"row":52,"column":35},"end":{"row":52,"column":36},"action":"insert","lines":["e"]}],[{"start":{"row":52,"column":32},"end":{"row":52,"column":36},"action":"remove","lines":["myDe"],"id":5},{"start":{"row":52,"column":32},"end":{"row":52,"column":50},"action":"insert","lines":["myDecryptedMessage"]}],[{"start":{"row":52,"column":50},"end":{"row":52,"column":51},"action":"remove","lines":["n"],"id":6},{"start":{"row":52,"column":50},"end":{"row":52,"column":51},"action":"remove","lines":["c"]},{"start":{"row":52,"column":50},"end":{"row":52,"column":51},"action":"remove","lines":["r"]},{"start":{"row":52,"column":50},"end":{"row":52,"column":51},"action":"remove","lines":["y"]},{"start":{"row":52,"column":50},"end":{"row":52,"column":51},"action":"remove","lines":["p"]},{"start":{"row":52,"column":50},"end":{"row":52,"column":51},"action":"remove","lines":["t"]},{"start":{"row":52,"column":50},"end":{"row":52,"column":51},"action":"remove","lines":["e"]},{"start":{"row":52,"column":50},"end":{"row":52,"column":51},"action":"remove","lines":["d"]},{"start":{"row":52,"column":50},"end":{"row":52,"column":51},"action":"remove","lines":["M"]},{"start":{"row":52,"column":50},"end":{"row":52,"column":51},"action":"remove","lines":["e"]},{"start":{"row":52,"column":50},"end":{"row":52,"column":51},"action":"remove","lines":["s"]},{"start":{"row":52,"column":50},"end":{"row":52,"column":51},"action":"remove","lines":["s"]},{"start":{"row":52,"column":50},"end":{"row":52,"column":51},"action":"remove","lines":["a"]},{"start":{"row":52,"column":50},"end":{"row":52,"column":51},"action":"remove","lines":["g"]}],[{"start":{"row":52,"column":50},"end":{"row":52,"column":51},"action":"remove","lines":["e"],"id":7}]]},"ace":{"folds":[],"scrolltop":502.5,"scrollleft":0,"selection":{"start":{"row":52,"column":50},"end":{"row":52,"column":50},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":32,"state":"start","mode":"ace/mode/python"}},"timestamp":1696993421138,"hash":"59ccac96631ec234ff7a94780656a56e25fb3b92"}