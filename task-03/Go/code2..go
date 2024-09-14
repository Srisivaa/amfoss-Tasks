package main

import (
    "io/ioutil"
    "os"
)

func main() {
    // Read from input.txt and write to output.txt
    content, err := ioutil.ReadFile("input.txt")
    if err != nil {
        panic(err)
    }
    err = ioutil.WriteFile("output.txt", content, 0644)
    if err != nil {
        panic(err)
    }
}
