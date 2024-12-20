package day2

import (
	"advent_of_code/utils"
	"fmt"
	"log"
	"strconv"
	"strings"
)

func Safe(list []int) bool {
	length := len(list)

	sign := utils.Sign(list[0] - list[1])
	for i := 0; i < (length - 1); i += 1 {
		diff := list[i] - list[i+1]

		if sign == utils.Sign(diff) {
			diff = utils.AbsInt(diff)
			if !(diff >= 1 && diff <= 3) {
				return false
			}
		} else {
			return false
		}
	}

	return true
}

func Solution1(inputFileName string) {
	input := utils.Input(inputFileName)

	var safe int = 0

	for _, line := range input {
		var levels []int
		list := strings.Split(line, " ")

		for _, num := range list {
			level, err := strconv.Atoi(num)
			if err != nil {
				log.Fatal("error converting number")
			}
			levels = append(levels, level)
		}

		if Safe(levels) {
			safe += 1
		}
	}

	fmt.Println(safe)
}

func Safe2(list []int) bool {
	length := len(list)

	sign := utils.Sign(list[0] - list[1])
	for i := 0; i < length-1; i += 1 {
		diff := list[i] - list[i+1]

		if sign == utils.Sign(diff) {
			diff = utils.AbsInt(diff)
			if !(diff >= 1 && diff <= 3) {
				list3safety := false
				if i > 0 {
					list3 := []int{}
					list3 = utils.RemoveFromList(append(list3, list...), i - 1)
					list3safety = Safe(list3)
				}
				list1 := []int{}
				list1 = utils.RemoveFromList(append(list1, list...), i)
				list2 := []int{}
				list2 = utils.RemoveFromList(append(list2, list...), i+1)
				return Safe(list1) || Safe(list2) || list3safety
			}
		} else {
			list3safety := false
			if i > 0 {
				list3 := []int{}
				list3 = utils.RemoveFromList(append(list3, list...), i - 1)
				list3safety = Safe(list3)
			}
			list1 := []int{}
			list1 = utils.RemoveFromList(append(list1, list...), i)
			list2 := []int{}
			list2 = utils.RemoveFromList(append(list2, list...), i+1)
			return Safe(list1) || Safe(list2) || list3safety
		}
	}

	return true
}

func Solution2(inputFileName string) {
	input := utils.Input(inputFileName)

	var safe int = 0

	for _, line := range input {
		var levels []int
		list := strings.Split(line, " ")

		for _, num := range list {
			level, err := strconv.Atoi(num)
			if err != nil {
				log.Fatal("error converting number")
			}
			levels = append(levels, level)
		}

		safety := Safe2(levels)
		// fmt.Println(levels)
		// fmt.Println(safety)
		if safety {
			safe += 1
		}
	}

	fmt.Println(safe)
}
