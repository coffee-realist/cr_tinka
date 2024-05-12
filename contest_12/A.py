import math

print(*[(a * b) // math.gcd(a, b) for a, b in [map(int, input().split())]])
