def checkBraces(string):
    stack = []
    pairs = {"{": "}", "(": ")", "[": "]"}
    for s in string:
        if s in "{([":
            stack.append(s)
        elif len(stack) > 0 and s == pairs[stack[-1]]:
            stack.pop()
        else:
            return False
    return len(stack) == 0
    
s = "{[()]}"
print(s, checkBraces(s))