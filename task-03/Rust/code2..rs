use std::fs;
use std::io::Result;

fn main() -> Result<()> {
    // Read from input.txt and write to output.txt
    let content = fs::read_to_string("input.txt")?;
    fs::write("output.txt", content)?;
    Ok(())
}
