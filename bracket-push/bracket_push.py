def check_brackets(string: str) -> bool:
    all_brackets = {'}': '{', ']': '[', ')': '('}
    open_brackets = set(all_brackets.values())
    close_brackets = set(all_brackets.keys())

    if len(string) == 0:
        return True

    stack = []
    for i in range(len(string)):
        if string[i] in open_brackets:
            stack.append(string[i])
        elif string[i] in close_brackets:
            if len(stack) > 0 and stack[-1] == all_brackets[string[i]]:
                stack.pop()
            else: return False

    return len(stack) == 0
