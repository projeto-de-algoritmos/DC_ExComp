def divide_and_conquer(str):
  if len(str) == 1:
    # base case: single character string is already divided and conquered
    if str[0] == '@':
      print('a', end='')
    elif str[0] == '&':
      print('e', end='')
    elif str[0] == '!':
      print('i', end='')
    elif str[0] == '*':
      print('o', end='')
    elif str[0] == '#':
      print('u', end='')
    else:
      print(str[0], end='')
    return

  # divide the string into two equal halves
  mid = len(str) // 2
  left = str[:mid]
  right = str[mid:]

  # recursively apply the divide and conquer approach to each half of the string
  divide_and_conquer(left)
  divide_and_conquer(right)

while True:
  try:
    str = input()
    divide_and_conquer(str)
    print()
  except EOFError:
    break