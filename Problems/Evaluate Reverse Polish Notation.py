def evalRPN(tokens):
        operands = "+-*/"
        stack = []
        for i in tokens:
            if i not in operands:
                stack.append(i)
            else:
                temp = 0
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if i == "+":
                    temp = num1 + num2
                elif i == "-":
                    temp = num2 - num1
                elif i == "/":
                    temp = int(num2 / num1)
                else:
                    temp = num2 * num1
                stack.append(str(temp))
        return stack[0]
tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))