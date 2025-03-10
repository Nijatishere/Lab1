import math

# u-nu hesablayırıq
e = math.e
ln3 = math.log(3)
sin1 = math.sin(1)
sqrt_val = math.sqrt(0.0548)
pay = 12.4 * e**2 + 0.6 * e**(-1) * sqrt_val
payda = 0.389 * (ln3 + sin1)
u = math.sqrt(pay / payda)

# v-ni hesablayırıq
sqrt3 = math.sqrt(3)
tg1 = math.tan(sqrt3 / 3)
tg2 = 5 * tg1
sin_val = (1/4) * math.sin(sqrt3 / 2)
v = math.tan(tg2 - sin_val)

# Şərtə uyğun l-ni hesablayırıq
if abs(u) < abs(v):
    l = (3 * u + v) / (u**2 + v**2)
else:
    l = u * v

# Nəticələri çap edirik
print(f"u = {u}")
print(f"v = {v}")
print(f"l = {l}")
