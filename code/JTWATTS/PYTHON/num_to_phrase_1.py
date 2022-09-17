onez = {
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten"
    }

teen = {
    0:"zero",
    1:"eleven",
    2:"twelve",
    3:"thirteen",
    4:"forteen",
    5:"fifteen",
    6:"sixteen",
    7:"seventeen",
    8:"eithteen",
    9:"nineteen"
    }    
beyond = {
    2:"twenty",
    3:"thirty",
    4:"forty",
    5:"fifty",
    6:"sixty",
    7:"seventy",
    8:"eighty",
    9:"ninety",
    100:"hundred"
    }    


def num_to_phrase():
    x = int(input("give me a number between 1 and 100:  "))
    if x == 100:
        print(x)
    #this finds if a user place either a single digit or the second digit
    ones_digit = x%10
    #this finds the first digit if there is one
    tens_digit = x//10
    #determining if the first digit is between 11-19
    if ones_digit in onez:
        ones_digit = onez[ones_digit]
        #print(ones_digit)
    if tens_digit == 1:
        ten = teen[ones_digit]
        return ten    
    #determin if the first digit is between 20-90
    if tens_digit in beyond:
        tens_digit = beyond[tens_digit]  
        #print(tens_digit)  
     #determin the first digit is

    
  

        print(f'{tens_digit} {ones_digit}')

 
      


print(num_to_phrase())

   

    # if x in onez:
    #     print(onez[x])
 
    #     print(x) 
    # elif x in teen or beyond:
       
    #     fir = x
    #     if fir in teen:
    #         print(f'{teen[fir]}')
    #         print(fir)
    #     elif fir in beyond:
    #         print(f'{beyond[fir]}')    
    #         print(fir)



    #   print(f'{beyond[fir]} " " {onez[x]}')
       
    
    #return onez[second]
        # return beyond[first]
        # print(teen[first])
        # second = x[1]
        # # second = x[1]
        # second = int(second)
        # return onez[second]
    # tens_digit = x//10
    # ones_digit = x%10
    # print(num[x])

                # print(beyond[x])     
            
    # broken = x.split(",")
    # print(broken)
    # print(len(broken))
    # print(broken[0])


    # if len(broken) == 2:
    #     first, second = broken

    #     if first in teen:
    #         print(teen[first])
    #     elif first in beyond:
    #         print(beyond[first])    
    #     if len(broken) == 1:
    #         print(onez[broken])  

    # if input is in onez:
    #     print onez[input]
    # elif input turned string and find [0] in teen
    # elif input turned string and find [0] in beyond
    # e    