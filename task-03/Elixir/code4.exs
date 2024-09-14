defmodule Diamond do
  def print_diamond(n) do
    upper_half = for i <- 0..(n-1), do: String.duplicate(" ", n - i - 1) <> String.duplicate("*", 2 * i + 1)
    lower_half = for i <- (n-2)..0, do: String.duplicate(" ", n - i - 1) <> String.duplicate("*", 2 * i + 1)
    Enum.concat(upper_half, lower_half) |> Enum.join("\n")
  end
end

n = File.read!("input.txt") |> String.trim() |> String.to_integer()
diamond = Diamond.print_diamond(n)
File.write!("output.txt", diamond)