def intValidator(string: str) -> bool:
    try:
        num = int(string)
        if num < 0:
            return False
        return True
    except:
        ValueError
        return False
    
    
def strValidator(string: str) -> bool:
    if len(string) > 0: 
        return True
    return False 


def floatValidator(string: str) -> bool:
    try:
        num = float(string)
        if num <= 0:
            return False
        return True
    except:
        ValueError
        return False 
    

def filenameValidator(string: str) -> bool:
    return string.endswith(".bin")


if __name__ == "__main__":
    pass