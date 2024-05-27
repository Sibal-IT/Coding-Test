import sys


def main():
    str_input = input()
    arr = list(str_input[:])
    pop_check = False
    stack = list()
    cnt = 0
    ck = 0
    last_t = ''
    for i in arr:
        stack.append(i)
        if ( stack[-1] == ')' and last_t == '(' ):
            stack.pop()
            stack.pop()
            cnt += len(stack)
        elif( stack[-1] == ')' and last_t != '(' ):
            stack.pop()
            stack.pop()
            cnt += 1
        last_t = i
    print(cnt)

if __name__ == "__main__":
    main()
