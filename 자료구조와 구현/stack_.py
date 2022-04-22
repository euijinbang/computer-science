
def recursive(data):
    if data < 0:
        print("ended")
    else:
        print(data)
        recursive(data-1)
        print("returned", data)

recursive(4)

# list 로 구현
data_stack = list()

def push(data):
    data_stack.append(data)

def pop():
    del data_stack[-1]
    return data_stack[-1]

for i in range(10):
    push(i)

print(data_stack)
push(33)
print(data_stack)
pop()
print(data_stack)