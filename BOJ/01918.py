import sys

def priority(operator):
    if operator == '*' or operator == '/':
        return 4
    elif operator == '+' or operator == '-':
        return 2
    else:
        return 0

def _11365():
    Stack = []
    N = str(input())

    res = ''
    for i in range(len(N)):
        if N[i] == '+' or N[i] == '-' or N[i] == '*' or N[i] == '/':
            if Stack:
                if priority(Stack[-1]) >= priority(N[i]):
                    res += Stack.pop()
                    if Stack :
                        if priority(Stack[-1]) == priority(N[i]):
                            res += Stack.pop()
                            Stack.append(N[i])
                        else:
                            Stack.append(N[i])
                    else:
                        Stack.append(N[i])

                else :
                    Stack.append(N[i])

            else:
                Stack.append(N[i])

        elif N[i] == '(':
            Stack.append(N[i])

        elif N[i] == ')':
            while 1:
                if Stack[-1] == '(':
                    Stack.pop()
                    break
                else:
                    res += Stack.pop()
        else:
            res += N[i]

    if Stack:
        while 1:
            if not Stack:
                break
            res += Stack.pop()
    print(res)
_11365()