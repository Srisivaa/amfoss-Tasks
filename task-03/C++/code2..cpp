#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream infile("input.txt");
    std::ofstream outfile("output.txt");
    std::string content;

    if (!infile || !outfile) {
        std::cerr << "Error opening file" << std::endl;
        return 1;
    }

    while (getline(infile, content)) {
        outfile << content << std::endl;
    }

    infile.close();
    outfile.close();

    return 0;
}
