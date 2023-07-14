


def txtToMatrix(pFile):

    matrix = []
    result = []
    aux = []
    count = 0
    timetoappend = 0

    fp = open(pFile,'r')
    read = 'a'

    while read != '':
        read = fp.read(1)

        if read != "" and read != chr(32) and read != "\n" and read != ",":
            if ord(read) >= 48 and ord(read) <= 57 or ord(read) ==35:
                aux.append(read)

            if ord(read) >= 65 and ord(read) <= 90:
                aux.append(read)

            if ord(read) >= 97 and ord(read) <= 122 and count >= 4:
                aux.append(read)

        
        if read == chr(32) and aux != []:
            count+=1
            result.append("".join(aux))
            aux = []
        
        if read == ",":
            count = 0
            result.append(''.join(aux))
            matrix.append(result)
            result = []
            aux = []
        


    fp.close()

    fp2 = open('testing.txt', 'w')
    fp2.write(str(matrix))
    fp2.close()


txtToMatrix('testing_monalisa.txt')