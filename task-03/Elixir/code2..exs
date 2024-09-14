# Read from input.txt and write to output.txt
content = File.read!("input.txt")
File.write!("output.txt", content)
