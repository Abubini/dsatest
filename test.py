

def push(stack, item):
    stack.append(item)
    print("pushed item", item)
    buble(stack)
def pop(stack):
    if is_empty(stack):
        print("stack is empty")

    else:
        stack.pop()
    print("stack after poped", stack)
def is_empty(stack):
    return len(stack) == 0
def display(stack):
    print(stack)

def buble(stack):
    for i in range (len(stack)):

        for j in range (len(stack)-1):
            if stack[j] > stack[j+1]:
                stack[j], stack[j+1] = stack[j+1], stack[j]



def sort_stack(stack):
    temp_stack = []

    while stack:
        # Pop the top element from the original stack
        current_element = stack.pop()

        # While the temporary stack is not empty and the top of the temp stack is greater than the current element
        while temp_stack and temp_stack[-1] < current_element:
            # Pop from the temporary stack and push it back to the original stack
            stack.append(temp_stack.pop())

        # Push the current element to the temporary stack
        temp_stack.append(current_element)

    # Transfer the sorted elements back to the original stack
    while temp_stack:
        stack.append(temp_stack.pop())

    return stack

# Example usage





stack = []

push(stack,5)
push(stack,6)
push(stack,2)
display(stack)


sorted_stack = sort_stack(stack)
print("Sorted Stack:", sorted_stack)

