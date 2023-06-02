def div_func(num1,num2,division):
    '''for division num1 and num2'''
    if num2==0:
        return "can't division to zero"
    return num1/num2
num1=float(input())
num2=float(input())
operator =input()
if operator=='/':
    print(div_func(num1, num2, division))


