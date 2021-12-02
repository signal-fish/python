def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)

print(f"times3(9) = {times3(9)}")
print(f"times5(9) = {times5(9)}")
