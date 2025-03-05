import sympy as sp
import math

def hord_method(f, a: float, b: float, nmax: int, eps: float):
    try:
        if f(a) * f(b) > 0:
            return None, 0, 1 
    except (ValueError, ZeroDivisionError, TypeError):
        return None, 0, 3 

    co = 0
    x_prev = a
    while co < nmax:
        co += 1
        try:
            x_next = a - f(a) * (b - a) / (f(b) - f(a))
        except (ValueError, ZeroDivisionError, TypeError):
            return None, 0, 3 

        
        if abs(x_next - x_prev) < eps:
            return x_next, co, 0  

        try:
            fx_next = f(x_next)
            if fx_next * f(a) < 0:
                b = x_next
            else:
                a = x_next
        except (ValueError, ZeroDivisionError, TypeError):
            return None, 0, 3 

        x_prev = x_next

    return x_next, co, 2 

def get_func(funcstring: str):
    try:
        func = lambda x: (eval(funcstring, {"x": x, "math": math}) )
    except:
        ValueError
        func = None
    
    return func 


def get_first_d(f):
    df = str(sp.diff(f))
    df_func = lambda x: (eval(df, {"x", x}))
    return df_func


def get_second_d(df):
    df_2 = str(sp.diff(df))
    df2_func = lambda x: (eval(df_2, {"x": x}))
    return df2_func




    
def check_if_valid(num):
    
    if (num.count(".") <= 1) and (all(j in "0123456789-." for j in num)) and \
        (num.count("-") <= 1):
        if "-" in num:
            if num[0] != "-":
                return False
        return True
    
    return False 