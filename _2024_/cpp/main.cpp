#include <fstream>
#include <iostream>
#include <string>
#include <vector>

std::string solution_part1(const std::vector<std::string>);
std::string solution_part2(const std::vector<std::string>);

int main(int argc, char *argv[]) {
    std::ifstream inputFile{argv[1]};

    if (!inputFile) {
        std::cerr << "Error opening file: " << argv[1] << '\n';
        return 1;
    }

    std::string line{};
    std::vector<std::string> input{};

    while (std::getline(inputFile, line)) {
        input.push_back(line);
    }

    std::string result = solution_part1(input);
    std::cout << "Solution Part 1: " << result << '\n';

    result = solution_part2(input);
    std::cout << "Solution Part 2: " << result << '\n';

    return 0;
}
