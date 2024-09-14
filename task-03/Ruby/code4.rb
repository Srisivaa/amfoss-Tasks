```ruby
def print_diamond(n)
  lines = []
  (0...n).each do |i|
    lines << ' ' * (n - i - 1) + '*' * (2 * i + 1)
  end
  (n - 2).downto(0) do |i|
    lines << ' ' * (n - i - 1) + '*' * (2 * i + 1)
  end
  lines.join("\n")
end

n = File.read('input.txt').to_i
diamond = print_diamond(n)
File.write('output.txt', diamond)
```