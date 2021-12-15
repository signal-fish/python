def reverse_str(my_str):
    length = len(my_str)
    for i in range(length-1, -1, -1):
        yield my_str[i]

my_str = "画上荷花和尚画"
print(f"my_str = {my_str}")
print(f"reverse_str = ", end='')
for char in reverse_str(my_str):
    print(char, end='')
print()
