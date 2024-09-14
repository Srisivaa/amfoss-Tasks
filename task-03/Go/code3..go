```go
package main

import (
    "fmt"
)

func printDiamond(n int) {
    for i := 0; i < n; i++ {
        fmt.Printf("%s%s\n", string(' ', n-i-1), string('*', 2*i+1))
    }
    for i := n - 2; i >= 0; i-- {
        fmt.Printf("%s%s\n", string(' ', n-i-1), string('*', 2*i+1))
    }
}

func main() {
    var n int
    fmt.Print("Enter a number: ")
    fmt.Scan(&n)
    printDiamond(n)
}
```
