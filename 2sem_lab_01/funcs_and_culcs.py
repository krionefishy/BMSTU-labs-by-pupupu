
def check_if_valid(num1, operation, num2):
    
    if len(operation) != 1:
        return False
    
    if (operation in "+-") and (num1.count(".") <= 1) and (num2.count(".") <= 1) and \
        (all(j in "01234-." for j in num1)) and (all(j in "01234-." for j in num2)) and \
        (num1.count("-") <= 1) and (num2.count("-") <= 1):
        if "-" in num1:
            if num1[0] != "-":
                return False
        if "-" in num2:
            if num2[0] != "-":
                return False 
        
        return True
    
    return False 
            
            
def five_to_dec(num):
    if "-" in num:
        num = num[1:]
        has_minus = True 
    else:
        has_minus = False 
        
    if "." in num:
        left, right = num.split(".") 
        
        left_res = 0
        current = 0
        for i in left[::-1]:
            left_res += 5**(current) * int(i)
            current += 1
            
        right_res = 0
        current = -1
        for i in right:
            right_res += 5**(current) * int(i)
            current -= 1
        if has_minus:
            return -1 * (left_res + right_res)
        else:
            return left_res+right_res
        
    else:
        res = 0
        current = 0
        for i in num[::-1]:
            res += 5**(current) * int(i)
            current += 1
            
        if has_minus:
            return -1 * res 
        else:
            return res  
    


def dec_to_five(num):
    num = str(num)
    if "-" in num:
        has_minus = True 
        num = num[1:]
    else:
        has_minus = False
        
        
    if "." in num:
        left, right = num.split(".")
        left = int(left)
        right = float("0." + right)
        left_res = ""
        while left > 0:
            left_res += str(left % 5)
            left //= 5
        left_res = left_res[::-1]
        
        right_res = ""
        for _ in range(6):
            right *= 5
            right_res += str(int(right))
            right = right - int(right)    
            
        if has_minus:
            return "-" + left_res + "." + right_res
        else:
            return left_res + "." + right_res
        
    else:
        res = ""
        num = int(num)
        while num > 0:
            res += str(num % 5)
            num //= 5
        
        if has_minus:
            return "-" + res[::-1]
        else:
            return res[::-1]
        
        


def calc_minus(num1, num2):
    res = five_to_dec(num1) - five_to_dec(num2)
    return dec_to_five(res)

def calc_plus(num1, num2):
    res = five_to_dec(num1) + five_to_dec(num2)
    return dec_to_five(res)
    

if __name__ == "__main__":
    pass