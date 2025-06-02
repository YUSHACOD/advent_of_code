#include <algorithm>
#include <sstream>
#include <string>
#include <vector>

std::string solution_part1(const std::vector<std::string> input) {
    std::string result = "Not Solved";

    std::vector<int> left_list{};
    std::vector<int> right_list{};

    for (int i = 0; i < input.size(); i += 1) {
        std::string left_num{"0"};
        std::string right_num{"0"};

        std::stringstream ss(input[i]);
        ss >> left_num >> right_num;

        left_list.push_back(std::stoi(left_num));
        right_list.push_back(std::stoi(right_num));
    }

    std::stable_sort(left_list.begin(), left_list.end());
    std::stable_sort(right_list.begin(), right_list.end());

    int distance = 0;
    for (int i = 0; i < input.size(); i += 1) {
        distance += std::abs(left_list[i] - right_list[i]);
    }
    result = std::to_string(distance);

    return result;
}

std::string solution_part2(const std::vector<std::string> input) {
    std::string result = "Not Solved";

    std::vector<int> left_list{};
    std::vector<int> right_list{};

    for (int i = 0; i < input.size(); i += 1) {
        std::string left_num{"0"};
        std::string right_num{"0"};

        std::stringstream ss(input[i]);
        ss >> left_num >> right_num;

        left_list.push_back(std::stoi(left_num));
        right_list.push_back(std::stoi(right_num));
    }

    int score = 0;
    for (int i = 0; i < input.size(); i += 1) {
        int oc = 0;
        for (int j = 0; j < input.size(); j += 1) {
            if (left_list[i] == right_list[j]) {
                oc += 1;
            }
        }
        score += left_list[i] * oc;
    }
    result = std::to_string(score);

    return result;
}
