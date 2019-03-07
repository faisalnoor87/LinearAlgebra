from vector import Vector

# v = Vector(['3.183', '-7.627'])
# w = Vector(['-2.668', '5.319'])

# result = v.angle_with(w)
# print(result)

print('check is parallel and orthogonal')
v = Vector(['2.118', '4.827'])
w = Vector(['0', '0'])

print('Is----Orthogonal')
print(v.is_orthoginal_to(w))
print('Is----Parallel')
print(v.is_paralled_to(w))
