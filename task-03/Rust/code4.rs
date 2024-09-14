```rust
use std::fs;
use std::io::{self, BufRead};

fn print_diamond(n: usize) -> String {
    let mut lines = Vec::new();
    for i in 0..n {
        lines.push(format!("{}{}", " ".repeat(n - i - 1), "*".repeat(2 * i + 1)));
    }
    for i in (0..n-1).rev() {
        lines.push(format!("{}{}", " ".repeat(n - i - 1), "*".repeat(2 * i + 1)));
    }
    lines.join("\n")
}

fn main() -> io::Result<()> {
    let input = fs::read_to_string("input.txt")?;
    let n: usize = input.trim().parse().expect("Invalid number");
    let diamond = print_diamond(n);
    fs::write("output.txt", diamond)?;
    Ok(())
}
```