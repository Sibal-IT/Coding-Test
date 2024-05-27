import sys


def main():
    tokens = list(map(str, input().rstrip()))     

    num_list = []
    
    for i in tokens:
        if i.isdigit():
            num_list.append(i)
        else:
            b = num_list.pop()
            a = num_list.pop()
            if i == '+':
                num_list.append(int(int(a) + int(b)))
            elif i == '-':
                num_list.append(int(int(a) - int(b)))
            elif i == '*':
                num_list.append(int(int(a) * int(b)))
            elif i == '/':
                num_list.append(int(int(a) / int(b)))
    
    print(int(num_list.pop()))


if __name__ == "__main__":
    main()
