
tpl_l = []
for i in range(1, 17):
    data = input(f"Enter your value {i} like(3.0, 5.0): ")

    tpl_v = tuple(map(float, data.split(',')))
    tpl_l.append(tpl_v)
m_4x4 = [tpl_l[i:i + 4] for i in range(0, 16, 4)]

for _ in m_4x4:
    print(_)

nash = []
for i in range(4):
    for j in range(4):
        n_A, n_B = m_4x4[i][j]

        if all(n_A >= m_4x4[x][j][0] for x in range(4)):
            if all(n_B >= m_4x4[i][y][1] for y in range(4)):

                nash.append(((i, j), (n_A, n_B)))

print('Nash in point:', nash)