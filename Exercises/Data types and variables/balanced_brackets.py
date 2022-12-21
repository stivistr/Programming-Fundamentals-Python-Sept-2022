number_of_lines = int(input())

opening_bracket = "("
closing_bracket = ")"

brackets_order = []
isBalanced = False

for text in range(number_of_lines):
    current_string = input()
    if current_string == opening_bracket:
        brackets_order.append(current_string)
    if current_string == closing_bracket:
        brackets_order.append(current_string)

for index in range(len(brackets_order)):
    if index % 2 != 0:
        if brackets_order[index] == opening_bracket:
            isBalanced = True


if isBalanced:
    print('UNBALANCED')
else:
    print('BALANCED')
