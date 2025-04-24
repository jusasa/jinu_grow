
def infix_to_postfix(infix_expression):
    priority = {'(' : 0,')' : 0,'+': 1, '-': 1, '*': 2, '/': 2}
    postfix_expression = []
    stack = []
    for char in infix_expression:
        if char not in priority:
            postfix_expression.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix_expression.append(stack.pop())
            stack.pop()
        else:
            while stack and priority[char] <= priority[stack[-1]]:
                postfix_expression.append(stack.pop())
            stack.append(char)
    while stack:
        postfix_expression.append(stack.pop())
    return ''.join(postfix_expression)
print(infix_to_postfix(input()))