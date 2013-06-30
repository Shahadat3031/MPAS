from math import sqrt

r = [0.594, 0.928, 0.515, 0.055, 0.507, 0.351, 0.262, 0.797, 0.788, 0.442, 0.097, 0.798, 0.227, 0.127, 0.474, 0.825, 0.007, 0.182, 0.929, 0.852]

r.sort()
d_plus = max((i + 1) / len(r) - r_i for i, r_i in enumerate(r))
d_minus = max(r_i - i / len(r) for i, r_i in enumerate(r))
print([r[i] - i / len(r) for i in range(len(r))])

print("D+ = {}".format(d_plus))
print("D- = {}".format(d_minus))

d = max(d_plus, d_minus)

print("D  = {}".format(d))

d_alpha = 1.36/sqrt(len(r))
d_alpha = 0.565

if d <= d_alpha:
    print("H0 accepted")
else:
    print("H0 rejected")
