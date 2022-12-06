#1
import operator
ops = { "+": operator.add, "-": operator.sub } # etc.

print (ops["+"](1,1)) # prints 2




import operator

def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.div,
        '%' : operator.mod,
        '^' : operator.xor,
    }[op]

def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)

print eval_binary_expr(*("1 + 3".split()))
print eval_binary_expr(*("1 * 3".split()))
print eval_binary_expr(*("1 % 3".split()))
print eval_binary_expr(*("1 ^ 3".split()))