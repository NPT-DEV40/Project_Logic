def ReadFile(fileNameIn):
    # read file
    array = [] 
    with open(fileNameIn, 'r') as f:
        lines = f.readlines()
    for line in lines:
        array.append(line.split())
    return array

# delete element 'OR'
def DeleteOR(x):
    tmp = []
    for i in range(len(x)):
        if 'OR' in x[i]:
            continue
        else:
            tmp.append(x[i])
    return tmp

def Negative(x):
    tmp = []
    for i in range(len(x)):
        # check string has element '-'
        if '-' in x[i]:
            #delete element '-'
            tmp.append(x[i].replace('-', ''))
        else:
            #add element '-'
            tmp.append('-' + x[i])
    return tmp


def SortAlphabet(array):
    tmp = []
    for i in range(len(array)):
        # replace element '-A' with 'A'
        if '-' in array[i]:
            array[i] = array[i].replace('-', '')
            tmp.append(array[i])
    array.sort()
    for i in range(len(array)):
        if array[i] in tmp:
            array[i] = '-' + array[i]
    return array       

def CombineClause(self, other):
    store = []
    result = []
    tmp = self + other
    len1 = len(tmp)
    for i in range(len(tmp) - 1):
        for j in range(i + 1,len(tmp)):
            if tmp[i] == '-' + tmp[j] or '-' + tmp[i] == tmp[j]:
                store.append(tmp[i])
                store.append(tmp[j])
    # delete element in array1 duplicate in array2
    for i in range(len(tmp)):
        if tmp[i] not in store:
            result.append(tmp[i])
    result = list(set(result))
    if len(result) == 1 and len1 > 3:
        return 
    return result



def PL_Resolution(array, fileNameIn):
    array = ReadFile(fileNameIn)
    arrayData = []
    arrayTransform = []

    for i in range(len(array)):
        arrayData.append(DeleteOR(array[i]))
    # add element in array from 2 to end
    for i in range(2, len(arrayData)):
        arrayTransform.append(arrayData[i])
    for i in Negative(arrayData[0]):
        arrayTransform.append([i])
    tmpArray = []
    var = 0
    Length = len(arrayTransform)

    while var != len(arrayTransform): # check len(arrayTransform) change or not
        check = True
        arrayTest = []
        for i in range(len(arrayTransform) - 1): # for loop
            for k in range(len(arrayTransform[i])):
                for j in range(i + 1, len(arrayTransform)):
                    for l in range(len(arrayTransform[j])):
                        if arrayTransform[i][k] == '-' + arrayTransform[j][l] or '-' + arrayTransform[i][k] == arrayTransform[j][l]:
                            if CombineClause(arrayTransform[i], arrayTransform[j]) == [] and len(arrayTransform[i]) != 1:
                                continue
                            arrayTest.append(CombineClause(arrayTransform[i], arrayTransform[j]))
        # delete elements have value None in arrayTest
        arrayTest = [x for x in arrayTest if x != None]
        # delete string elements duplicate in arrayTest
        arrayTest = [list(x) for x in set(tuple(x) for x in arrayTest)] 
        var = len(arrayTransform)
        for array in arrayTest:
            if SortAlphabet(array) not in arrayTransform:
                arrayTransform.append(SortAlphabet(array))
        tmpArray.append(len(arrayTransform) - var) # add an amount of element in arrayTransform matched in each loop 
        if [x for x in arrayTest if x == []] == [[]]: # check arrayTest have element [] or not
            break

    # add 'OR' in among elements in arrayTransform
    for i in range(len(arrayTransform)):
        for j in range(len(arrayTransform[i])):
            if j == len(arrayTransform[i]) - 1:
                break
            arrayTransform[i][j] = arrayTransform[i][j] + ' OR'

    # add each of the elements in tmpArray to arrayTransform so that the start element at Length and end element at Length + len(tmpArray) + 1
    k = 0
    tmp = Length
    while(k < len(tmpArray)):
        arrayTransform.insert(tmp, [str(tmpArray[k])])
        tmp += tmpArray[k] + 1 
        k += 1
    if [] in arrayTransform:
        arrayTransform.append(['YES'])
    else:
        arrayTransform.append(['NO'])
    return [arrayTransform, Length]


def WriteFile(array, fileNameOut, Length):
    with open(fileNameOut, 'w') as f:
        for i in range(Length, len(array)):
            if array[i] == []:
                f.write('{}')
            else:            
                f.writelines(' '.join(array[i]))
            f.write('\n')


# Main function
array = []
for i in range(1, 6):
    arrayTransform = PL_Resolution(array, 'INPUT/input' + str(i) +'.txt')
    WriteFile(arrayTransform[0], 'OUTPUT/output' + str(i) +'.txt', arrayTransform[1])



    
               

            



        
        


