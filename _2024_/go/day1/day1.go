package day1

import (
	"advent_of_code/utils"
	"fmt"
	"log"
	"sort"
	"strconv"
	"strings"
)

func Solution1(inputFileName string) {
	input := utils.Input(inputFileName)

	var left []int
	var right []int

	for _, line := range input {
		numbers := strings.Split(line, "   ")

		num_left, err := strconv.Atoi(numbers[0])
		if err != nil {
			log.Fatal("conversion error left number")
		}

		left = append(left, num_left)

		num_right, err := strconv.Atoi(numbers[1])
		if err != nil {
			log.Print(numbers[1])
			log.Fatal("conversion error right number")
		}

		right = append(right, num_right)
	}

	sort.Ints(left)
	sort.Ints(right)
	
	if len(left) != len(right) {
		log.Fatal("lists are fucked left != right")
	}

	var ans int = 0
	for i := 0; i < len(left); i += 1 {
		ans += utils.AbsInt(left[i] - right[i])	
	}

	fmt.Println(ans)
}

func SimilarityScore(num int, list []int) int {
	var result int = 0

	for i := 0; i < len(list); i += 1 {
		if list[i] == num {
			result += 1;
		}
	}

	return num * result
}

func Solution2(inputFileName string) {
	input := utils.Input(inputFileName)

	var left []int
	var right []int

	for _, line := range input {
		numbers := strings.Split(line, "   ")

		num_left, err := strconv.Atoi(numbers[0])
		if err != nil {
			log.Fatal("conversion error left number")
		}

		left = append(left, num_left)

		num_right, err := strconv.Atoi(numbers[1])
		if err != nil {
			log.Print(numbers[1])
			log.Fatal("conversion error right number")
		}

		right = append(right, num_right)
	}
	
	var result int = 0
	for _, num := range left {
		result += SimilarityScore(num, right)
	}

	fmt.Println(result)
}
