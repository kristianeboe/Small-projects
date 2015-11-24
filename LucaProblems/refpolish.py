def evalEqn(eqn):
    operators = ["add","subtract","multiply","divide"]
    stack = []
    for val in eqn:
        if val in operators:
            a = stack.pop()
            b = stack.pop()
            if val == "add":
                stack.append(b+a)
            if val == "subtract":
                stack.append(b-a)
            if val == "multiply":
                stack.append(b*a)
            if val == "divide":
                stack.append(b/a)
        else:
            stack.append(float(val))

    return stack[0]

test1 = [1,2,"add"]
test2 = [1,2,"add", 3, "subtract"]
test3 = [12, -8, "add", 2, 2, "multiply", 4, "add", "divide"]
test5 = [10, 6, "add", -2, "divide"]
print evalEqn(test1)
print evalEqn(test2)
print evalEqn(test5)

def extractEquation(eqnString):
    eqn = []
    operators = ["add","subtract","multiply","divide"]
    for val in eqnString.split(' '):
        if val in operators:
            eqn.append(val)
        else:
            if val == "negate":
                a = eqn.pop()
                eqn.append(-a)
            else:
                eqn.append(float(val))
    return eqn

print extractEquation("2 2 add 3 negate multiply")
