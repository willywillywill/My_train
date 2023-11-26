def priority(op):
    return 1 if op in "+-" else 2 if op in "*/" else 0
    
def toPostfix(infix):
    toStack, toOutput = ('(', ')')
    
    def procOpt(c, stack, output):
        if stack == "" or priority(stack[-1]) < priority(c):
            return (stack + c, output)
        else:
            return procOpt(c, stack[0:-1], output + stack[-1])
    
    def procPhs(stack, output):
        if stack[-1] == toStack:
            return (stack[0:-1], output)
        else:
            return procPhs(stack[0:-1], output + stack[-1])
            
    def procExpr(expr, stack = "", output = ""):
        if expr == "":
            return output + stack[::-1]
        elif expr[0] == toStack:
            return procExpr(expr[1:], stack + expr[0], output)
        elif expr[0] in "+-*/":
            return procExpr(expr[1:], *procOpt(expr[0], stack, output))
        elif expr[0] == toOutput:
            return procExpr(expr[1:], *procPhs(stack, output))
        else:
            return procExpr(expr[1:], stack, output + expr[0])
    
    output = procExpr(infix)
    return output

while 1:
    try:
        infix = input().replace(" ","")
        ans = list(toPostfix(infix))
        print(" ".join(ans))
    except:
        break



"""
a + b * c
a / b - c
a + b * ( c * ( d + e ) )
"""