```elixir
defmodule Diamond do
  def print_diamond(n) do
    0..(n - 1)
    |> Enum.each(fn i ->
      IO.puts(String.duplicate(" ", n - i - 1) <> String.duplicate("*", 2 * i + 1))
    end)

    (n - 2)..0
    |> Enum.each(fn i ->
      IO.puts(String.duplicate(" ", n - i - 1) <> String.duplicate("*", 2 * i + 1))
    end)
  end
end

IO.write("Enter a number: ")
n = IO.gets("") |> String.trim() |> String.to_integer()
Diamond.print_diamond(n)
```