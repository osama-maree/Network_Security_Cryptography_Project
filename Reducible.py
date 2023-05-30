from itertools import product
# to construct all polynomials less than degree by one
def generatePloynomial(n):
    p = list(product([0,1],repeat=n)) # Find all options for the n-bit 0 and 1 as bruteForce
    # example size=2 then ->p=[(0,0),(1,0),(0,1),(1,1)] must delete (0,0) and from (0,1) delete 0 to become (1)
    bruteForce = []                   # To Delete all zeros from the end of each option
    for i in p:
        item = list(i)
        while item and item[0] == 0:
            item.pop(0)
        if len(item)>1:              # greater than one becouse polynomial is reducible if there a factor other one
            bruteForce.append(item)  # and must whose degree is less than n
    return bruteForce                 # If size=2 ->return [[1],[1.0].[1,1]]

def DivideTwoPolynomial(divide, divisor): # take two parameter two polynomial 1-divide,2-divisor
    # degree for result of division is degree for divide/divisor now  in this solution divide as list and degree is last index
    # So degree for output len(divide)-len(divisor) and + 1  becouse list start from 0
    result =(len(divide)-len(divisor)+1)*[0]
    while len(divide) >= len(divisor):  # while degree for divide greater than divisor continue in divission
        # second item in result(output) equal coefficient for divide in list here represent as index
        result[len(divide) - len(divisor)] = divide[0]
        # The subtraction in the division operation is matched with x-or in division polynomial ex
        # if we have [1,1,0] - [0,0,1] in ploynomial = [1,1,0] ^ [0,0,1]=[1,1,1] each item(index) represent degree
        divide = [divide[i] ^ (divisor[i] if i < len(divisor) else 0) for i in range(len(divide))]
        while divide and divide[0] == 0: # now delete all zeros from the end of divide and end represent MSB
            divide.pop(0)
    # divide represent remainder of division operation becouse if degree for divide less than divisor break from while loop
    return result, divide
def isReducible(polynomial):
    bruteForce = generatePloynomial(len(polynomial)-1)  # to construct all polynomials less than degree by one
    # Divide the bolynomial on all possible probabilities If there is an factor that is divided by it without a remainder,
    # then  polynomial is reducible
    for i in bruteForce:
        quotient, remainder = DivideTwoPolynomial(polynomial, i)
        if len(remainder) == 0: # if remainder is zero then is factor for polynomial
            return quotient,remainder
    else:
        return False,False # if not found a factor for polynomial requrn false is irreducible


# [0, 1] represents x + 1,[1, 1, 0, 1] represents x^3 + x^2 + 1
print("the ploynomial :x^3 + x^2 + 1 represent as [1, 1, 0, 1]  please enter for same pattern to get right answer")
degree=int(input("plese enter Degree :"))
poly=[]
for i in range(degree+1):
    print("please enter the term number ",i," as binary ",end=": ")
    poly.insert(0,int(input()))

quotient, remainder=isReducible(poly)
print("the ploynomial ",poly,end=" ")
if  remainder != False:
    print("its reducible and result of division is: ",quotient)
    print("and remainder is: ", remainder)
else:
    print("its  irreducible")





    # dividend = [1, 0, 0, 1, 1]  # x^4 + x^3 + 1
    # divisor = [1, 0, 1]  # x^2 + 1

