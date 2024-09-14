package main

import (
    "fmt"
    "io/ioutil"
    "os"
    "strconv"
    "strings"
)

func printDiamond(n int) string {
    var lines []string
    for i := 0; i < n; i++ {
        lines = append(lines, strings.Repeat(" ", n-i-1)+strings.Repeat("*", 2*i+1))
    }
    for i := n - 2; i >= 0; i-- {
        lines = append(lines, strings.Repeat(" ", n-i-1)+strings.Repeat("*", 2*i+1))
    }
    return strings.Join(lines, "\n")
}

func main() {
    content, err := ioutil.ReadFile("input.txt")
    if err != nil {
        panic(err)
    }
    n, err := strconv.Atoi(strings.TrimSpace(string(content)))
    if err != nil {
        panic(err)
    }
    diamond := printDiamond(n)
    err = ioutil.WriteFile("output.txt", []byte(diamond), 0644)
    if err != nil {
        panic(err)
    }
}