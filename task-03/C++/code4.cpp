#include <iostream>
#include <fstream>
#include <string>

void printDiamond(std::ofstream& outfile, int n) {
    for (int i = 0; i < n; i++) {
        outfile << std::string(n - i - 1, ' ') << std::string(2 * i + 1, '*') << std::endl;
    }
    for (int i = n - 2; i >= 0; i--) {
        outfile << std::string(n - i - 1, ' ') << std::string(2 * i + 1, '*') << std::endl;
    }
}

int main() {
    std::ifstream infile("input.txt");
    std::ofstream outfile("output.txt");
    
    if (!infile || !outfile) {
        std::cerr << "Error opening file" << std::endl;
        return 1;
    }

    int n;
    infile >> n;
    printDiamond(outfile, n);

    infile.close();
    outfile.close();

    return 0;
}