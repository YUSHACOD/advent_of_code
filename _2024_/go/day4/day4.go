package day4

import (
	"advent_of_code/utils"
	"fmt"
)

var north = [][]int{
	{0, -1},
	{0, -2},
	{0, -3},
}

var north_east = [][]int{
	{1, -1},
	{2, -2},
	{3, -3},
}

var east = [][]int{
	{1, 0},
	{2, 0},
	{3, 0},
}

var south_east = [][]int{
	{1, 1},
	{2, 2},
	{3, 3},
}

var south = [][]int{
	{0, 1},
	{0, 2},
	{0, 3},
}

var south_west = [][]int{
	{-1, 1},
	{-2, 2},
	{-3, 3},
}

var west = [][]int{
	{-1, 0},
	{-2, 0},
	{-3, 0},
}

var north_west = [][]int{
	{-1, -1},
	{-2, -2},
	{-3, -3},
}

var directions = [][][]int{
	north,
	north_east,
	east,
	south_east,
	south,
	south_west,
	west,
	north_west,
}

var xmas_chars = []byte{
	'M',
	'A',
	'S',
}

func Xmas(input []string, y int, x int, limit int) int {
	found_xmas := 0

	for _, direction := range directions {
		if FindMas(input, y, x, direction, limit) {
			found_xmas += 1
		}
	}

	return found_xmas
}

func FindMas(input []string, y int, x int, direction [][]int, limit int) bool {
	for i, coord := range direction {
		x_new := x + coord[0]
		y_new := y + coord[1]

		if utils.InRange(0, limit, x_new) && utils.InRange(0, limit, y_new) {
			if xmas_chars[i] != input[y_new][x_new] {
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

	x_limit := len(input[0])
	y_limit := len(input)

	xmas_count := 0

	for y := 0; y < y_limit; y += 1 {
		for x := 0; x < x_limit; x += 1 {
			if input[y][x] == 'X' {
				xmas_count += Xmas(input, y, x, y_limit)
			}
		}
	}

	fmt.Println(xmas_count)
}

var diag1 = [][]int{
	{-1, -1},
	{1, 1},
}

var diag2 = [][]int{
	{1, -1},
	{-1, 1},
}

var diags = [][][]int{
	diag1,
	diag2,
}

func CheckDiag(input []string, y int, x int, limit int, diag [][]int) bool {
	x0 := x + diag[0][0]
	y0 := y + diag[0][1]
	x1 := x + diag[1][0]
	y1 := y + diag[1][1]

	in_range0 := utils.InRange(0, limit, x0) && utils.InRange(0, limit, y0)
	in_range1 := utils.InRange(0, limit, x1) && utils.InRange(0, limit, y1)

	if in_range0 && in_range1 {

		condition0 := input[y0][x0] == 'M' && input[y1][x1] == 'S'
		condition1 := input[y1][x1] == 'M' && input[y0][x0] == 'S'

		return condition0 || condition1
	} else {
		return false
	}
}

func IsXMas(input []string, y int, x int, limit int) bool {
	result := true 

	for _, diag := range diags {
		result = result && CheckDiag(input, y, x, limit, diag)
	}

	return result
}

func Solution2(inputFileName string) {
	input := utils.Input(inputFileName)

	x_limit := len(input[0])
	y_limit := len(input)

	x_mas_count := 0

	for y := 0; y < y_limit; y += 1 {
		for x := 0; x < x_limit; x += 1 {
			if input[y][x] == 'A' {
				if IsXMas(input, y, x, y_limit) {
					x_mas_count += 1
				}
			}
		}
	}

	fmt.Println(x_mas_count)
}
