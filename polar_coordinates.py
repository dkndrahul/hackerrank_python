from cmath import phase

complex_input = complex(input())
print("{0:.3f}".format(abs(complex_input)))
print("{0:.3f}".format(phase(complex_input)))
