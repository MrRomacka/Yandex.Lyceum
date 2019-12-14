coeffs = [[1], [1, 2, 1]]
N = int(input())
for i in range(2, N + 1):
    line_coeffs = [1] + [coeffs[i- 1][j] + coeffs[i- 1][j + 1] for j in range(len(coeffs[i - 1]) - 1)] + [1]
    coeffs.append(line_coeffs)
print(*coeffs, sep='\n')
