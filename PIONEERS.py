pyramid = '1\n'\
          '8 4\n'\
          '2 6 9\n'\
          '8 5 9 3\n'

p = '215\n' \
    '193 124\n' \
    '117 237 442\n' \
    '218 935 347 235\n' \
    '320 804 522 417 345\n' \
    '229 601 723 835 133 124\n' \
    '248 202 277 433 207 263 257\n' \
    '359 464 504 528 516 716 871 182\n' \
    '461 441 426 656 863 560 380 171 923\n' \
    '381 348 573 533 447 632 387 176 975 449\n' \
    '223 711 445 645 245 543 931 532 937 541 444\n' \
    '330 131 333 928 377 733 017 778 839 168 197 197\n' \
    '131 171 522 137 217 224 291 413 528 520 227 229 928\n' \
    '223 626 034 683 839 053 627 310 713 999 629 817 410 121\n' \
    '924 622 911 233 325 139 721 218 253 223 107 233 230 124 233\n'

def is_prime(i):
    if i >= 2:
        for j in range(2,i):
            if ( i % j ) == 0:
                return False
    else:
	    return False
    return True

def greatest_sum_finder(input):

    sum = 0
    array = {}   # KEY WILL BE ROW NUMBER AND VALUE WILL BE THE LIST OF AVAILABLE NUMBERS IN THAT ROW
    row_number = 1
    lst = []
    for i in input:
        if row_number not in array:
            array[row_number] = []
        if i == ' ':
            num = ''.join(lst)
            array[row_number].append(int(num))
            lst = []
        lst.append(i)

        if i == '\n':
            num = ''.join(lst)
            array[row_number].append(int(num))
            lst = []
            row_number += 1

    for row in array:
        try:
            num1 = array[row][ix]
            num2 = array[row][ix+1]
            if is_prime(num1) == False and is_prime(num2) == False:
                current_number = max(num1,num2)
                sum += current_number
                ix = array[row].index(current_number,ix)
            elif is_prime(num1) == True and is_prime(num2) == False:
                current_number = num2
                sum += current_number
                ix = array[row].index(current_number,ix)
            elif is_prime(num1) == False and is_prime(num2) == True:
                current_number = num1
                sum += current_number
                ix = array[row].index(current_number,ix)
        except:
            current_number = array[row][0]
            ix = array[row].index(current_number)
            if is_prime(current_number) == False:
                sum += current_number

    return sum


print greatest_sum_finder(p)
















