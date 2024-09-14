```python
def print_diamond(n):
    lines = []
    for i in range(n):
        lines.append(' ' * (n - i - 1) + '*' * (2 * i + 1))
    for i in range(n - 2, -1, -1):
        lines.append(' ' * (n - i - 1) + '*' * (2 * i + 1))
    return '\n'.join(lines)

with open('input.txt', 'r') as infile:
    n = int(infile.read().strip())

diamond = print_diamond(n)

with open('output.txt', 'w') as outfile:
    outfile.write(diamond)
```