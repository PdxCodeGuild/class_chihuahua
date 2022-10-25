
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
    9:"nine"
    }

teen = {
    #0:"ten",
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
thou = {
    1:"one hundred",
    2:"two hundred",
    3:"three hundred",
    4:"four hundred",
    5:"five hundred",
    6:"six hundred",
    7:"seven hundred",
    8:"eight hundred",
    9:"nine hundred"

}      



def num_to_phrase(x):
       # x = int(input("give me a number between 1 and 100:  "))
    # if x == 100:
    if x == 100:
        
        return "one hundred"
    if x == 10:
        return "ten"    
    #this finds if a user place either a single digit or the second digit
    ones_digit = x%10
    #this finds the first digit if there is one
    tens_digit = x//10

    tens_digit = tens_digit%10
    #find the first of 3 numbers
    hun_digit = x//100
    if hun_digit == 0:
        pass


    # if ones_digit > 10:
    #     one = onez[ones_digit] 
    #     return one 
    if hun_digit == 0 and tens_digit== 1 and ones_digit> 0:
        return teen[ones_digit]
    if hun_digit == 0 and tens_digit!= 0 and ones_digit== 0:
        return beyond[tens_digit]
    if hun_digit == 0 and tens_digit ==0:
        return onez[ones_digit]    
    if ones_digit in onez and tens_digit==0 :    # 
        # return thou[hun_digit] + " "+onez[ones_digit]
        #print(ones_digit)
        return thou[hun_digit] +" "+onez[ones_digit]
    if tens_digit in onez and ones_digit==0 :    # 
        return thou[hun_digit]+ " " +beyond[tens_digit]   
    if hun_digit!=0 and tens_digit!=0 and ones_digit==0 :    # 
        return thou[hun_digit]+ " " +beyond[tens_digit]    
    if hun_digit ==0 and tens_digit ==1 :
        return teen[ones_digit]
        return ten 

    if hun_digit !=0 and tens_digit== 1 and ones_digit!=0:  
        return  thou[hun_digit] +" "+teen[ones_digit]   
    if hun_digit !=0 and tens_digit!= 0 and ones_digit!=0:   
        return  thou[hun_digit] +" "+beyond[tens_digit]+ " " +onez[ones_digit]
    if hun_digit !=0 and tens_digit!= 0 and ones_digit==0:   
        return  thou[hun_digit] +" "+beyond[tens_digit]
    #determin if the first digit is between 20-90
    # if ones_digit == 0:
    #     tens_digit = beyond[tens_digit]  
        return tens_digit
    if tens_digit in beyond:
        return beyond[tens_digit]  +" "+ onez[ones_digit]
        # return beyond[tens_digit]+ " " +onez[ones_digit]  
    if hun_digit >= 1 and hun_digit <=9:
        return thou[hun_digit]  

    # print(thou[hun_digit] +beyond[tens_digit] + ten+onez[ones_digit] )    
print(num_to_phrase(999))
