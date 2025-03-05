

def get_result(num: str):
    cur_num = abs(int(num))
    
    bin_var = bin(cur_num)[2:]
    bin_var = "0" + bin_var


    bin_var = bin_var.replace("0","zn")
    bin_var = bin_var.replace("1", "0")
    bin_var = bin_var.replace("zn", "1")
    
    res = int(bin_var, 2) + 1
    
    return bin(res)[2:]

if __name__ == "__main__":
    pass
    