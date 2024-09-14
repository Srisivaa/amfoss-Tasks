
```rust
use std::io;

fn print_diamond(n: usize) {
    for i in 0..n {
        println!("{}{}", " ".repeat(n - i - 1), "*".repeat(2 * i + 1));
    }
    for i in (0..n-1).rev() {
        println!("{}{}", " ".repeat(n - i - 1), "*".repeat(2 * i + 1));
    }
}

fn main() {
    let mut input = String::new();
    println!("Enter a number: ");
    io::stdin().read_line(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    print_diamond(n);
}
```
