package day3

import (
	"advent_of_code/utils"
	"fmt"
	"strconv"
	"unicode"
)

func GetNum(line string, i int, state int) (int, int, int) {
	var result int = 0
	num, err := strconv.Atoi(line[i : i+1])
	if err != nil {
		return 0, i, 0
	} else {
		result = num
	}

	num, err = strconv.Atoi(line[i : i+2])
	if err != nil {
		return result, i, state + 1
	} else {
		result = num
	}

	num, err = strconv.Atoi(line[i : i+3])
	if err != nil {
		return result, i + 1, state + 1
	} else {
		result = num
	}

	return result, i + 2, state + 1
}

func SolveLine(line string) int {
	length := len(line)
	var result int = 0

	var state int = 0
	var num1 int = 0
	var num2 int = 0

	for i := 0; i < length; i += 1 {
		switch line[i] {

		case 'm':
			if state == 0 {
				state += 1
			} else {
				state = 0
			}

		case 'u':
			if state == 1 {
				state += 1
			} else {
				state = 0
			}

		case 'l':
			if state == 2 {
				state += 1
			} else {
				state = 0
			}

		case '(':
			if state == 3 {
				state += 1

			} else {
				state = 0
			}

		case ',':
			if state == 5 {
				state += 1

			} else {
				state = 0
			}

		case ')':
			if state == 7 {
				result += num1 * num2
				num1 = 0
				num2 = 0
			}
			state = 0

		default:
			if unicode.IsDigit(rune(line[i])) {
				if state == 4 {
					num1, i, state = GetNum(line, i, state)
				} else if state == 6 {
					num2, i, state = GetNum(line, i, state)
				} else {
					state = 0
				}
			} else {
				state = 0
			}
		}
	}

	return result
}

func Solution1(inputFileName string) {
	input := utils.Input(inputFileName)

	var result int = 0
	for _, line := range input {
		result += SolveLine(line)
	}

	fmt.Println(result)
}

func DCheck(line string, i int, enable int) (int, int) {
	if "do()" == line[i:i+4] {
		return 1, i + 3
	} else if "don't()" == line[i:i+7] {
		return 0, i + 6
	} else {
		return enable, i
	}
}

func SolveLine2(line string, enable int) (int, int) {
	length := len(line)
	var result int = 0

	var state int = 0
	var num1 int = 0
	var num2 int = 0

	for i := 0; i < length; i += 1 {
		switch line[i] {

		case 'm':
			if state == 0 {
				state += 1
			} else {
				state = 0
			}

		case 'u':
			if state == 1 {
				state += 1
			} else {
				state = 0
			}

		case 'l':
			if state == 2 {
				state += 1
			} else {
				state = 0
			}

		case '(':
			if state == 3 {
				state += 1

			} else {
				state = 0
			}

		case ',':
			if state == 5 {
				state += 1

			} else {
				state = 0
			}

		case ')':
			if state == 7 {
				if enable == 1 {
					result += num1 * num2
				}
				num1 = 0
				num2 = 0
			}
			state = 0

		case 'd':
			enable, i = DCheck(line, i, enable)
			state = 0
			fmt.Printf("d enable:%d, i:%d, state%d\n", enable, i, state)

		default:
			if unicode.IsDigit(rune(line[i])) {
				if state == 4 {
					num1, i, state = GetNum(line, i, state)
				} else if state == 6 {
					num2, i, state = GetNum(line, i, state)
				} else {
					state = 0
				}
			} else {
				state = 0
			}
		}
	}

	return result, enable
}

func Solution2(inputFileName string) {
	input := utils.Input(inputFileName)
	var enable int = 1
	var result int = 0

	for _, line := range input {
		var num int = 0
		num, enable = SolveLine2(line, enable)
		result += num
		fmt.Printf("enable %d, result %d, num %d\n", enable, result, num)
	}

	fmt.Println(result)
}
