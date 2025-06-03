#include <cstdlib>
#include <sstream>
#include <string>
#include <vector>

bool is_safe(const std::vector<int> levels) {
    bool sign = (levels[0] - levels[1]) > 0;

    for (int i = 0; i < levels.size() - 1; i += 1) {
        int diff = levels[i] - levels[i + 1];

        if (sign == (diff > 0)) {
            diff = std::abs(diff);

            if (!(diff >= 1 && diff <= 3)) {
                return false;
            }
        } else {
            return false;
        }
    }

    return true;
}

std::string solution_part1(const std::vector<std::string> input) {
    std::string result = "Not Solved";
    int acc = 0;

    for (int i = 0; i < input.size(); i += 1) {
        std::vector<int> levels;
        std::stringstream ss(input[i]);
        std::string num;

        while (ss >> num) {
            levels.push_back(std::stoi(num));
        }

        if (is_safe(levels)) {
            acc += 1;
        }
    }

    result = std::to_string(acc);
    return result;
}

std::vector<int> remove_at(const std::vector<int> levels, int n) {
    std::vector<int> new_levels;
    for (int i = 0; i < levels.size(); i += 1) {
        if (i != n) {
            new_levels.push_back(levels[i]);
        }
    }

    return new_levels;
}

bool is_safe2(const std::vector<int> levels) {
    bool sign = (levels[0] - levels[1]) > 0;

    for (int i = 0; i < levels.size() - 1; i += 1) {
        int diff = levels[i] - levels[i + 1];

        if (sign == (diff > 0)) {
            diff = std::abs(diff);

            if (!(diff >= 1 && diff <= 3)) {
                bool levelsSafe1 = false;

                if (i > 0) {
                    levelsSafe1 = is_safe(remove_at(levels, i - 1));
                }

                bool levelsSafe2 = is_safe(remove_at(levels, i));
                bool levelsSafe3 = is_safe(remove_at(levels, i + 1));

                return levelsSafe1 || levelsSafe2 || levelsSafe3;
            }
        } else {
            bool levelsSafe1 = false;

            if (i > 0) {
                levelsSafe1 = is_safe(remove_at(levels, i - 1));
            }

            bool levelsSafe2 = is_safe(remove_at(levels, i));
            bool levelsSafe3 = is_safe(remove_at(levels, i + 1));

            return levelsSafe1 || levelsSafe2 || levelsSafe3;
        }
    }

    return true;
}

std::string solution_part2(const std::vector<std::string> input) {
    std::string result = "Not Solved";
    int acc = 0;

    for (int i = 0; i < input.size(); i += 1) {
        std::vector<int> levels;
        std::stringstream ss(input[i]);
        std::string num;

        while (ss >> num) {
            levels.push_back(std::stoi(num));
        }

        if (is_safe2(levels)) {
            acc += 1;
        }
    }

    result = std::to_string(acc);
    return result;
}
