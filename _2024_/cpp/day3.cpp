#include <regex>
#include <sstream>
#include <string>
#include <vector>

long evaluate(const std::string op) {
    long num1 = 0;
    long num2 = 0;

    std::regex first_part("mul\\(");
    std::regex last_part("\\)");

    std::string s = std::regex_replace(std::regex_replace(op, first_part, ""),
                                       last_part, "");

    std::stringstream ss(s);
    std::string num;

    std::getline(ss, num, ',');
    num1 = std::stoi(num);

    std::getline(ss, num, ',');
    num2 = std::stoi(num);

    return num1 * num2;
}

std::string solution_part1(const std::vector<std::string> input) {
    std::string result = "Not Solved";

    std::regex op("mul\\([0-9]*,[0-9]*\\)");
    std::vector<std::string> operations;

    long acc = 0;

    for (int i = 0; i < input.size(); i += 1) {
        auto begin = std::sregex_iterator(input[i].begin(), input[i].end(), op);
        auto end = std::sregex_iterator();

        for (std::sregex_iterator j = begin; j != end; j++) {
            std::smatch match = *j;

            acc += evaluate(match.str());
        }
    }

    result = std::to_string(acc);
    return result;
}

std::string solution_part2(const std::vector<std::string> input) {
    std::string result = "Not Solved";

    std::regex op("(mul\\([0-9]*,[0-9]*\\))|(do\\(\\))|(don't\\(\\))");
    std::vector<std::string> operations;

    long acc = 0;
    bool active = true;

    for (int i = 0; i < input.size(); i += 1) {
        auto begin = std::sregex_iterator(input[i].begin(), input[i].end(), op);
        auto end = std::sregex_iterator();

        for (std::sregex_iterator j = begin; j != end; j++) {
            std::smatch match = *j;

            switch (match.str()[2]) {
                case ('n'):
                    active = false;
                    break;

                case ('('):
                    active = true;
                    break;

                case ('l'):
                    if (active) {
                        acc += evaluate(match.str());
                    }
                    break;

                default:
                    break;
            }
        }
    }

    result = std::to_string(acc);
    return result;
}
