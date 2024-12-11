package utils

import (
	"io"
	"log"
	"os"
	"strings"
)

func AbsInt(x int) int {
	if x < 0 {
		return -x
	}

	return x
}

func Sign(x int) int {
	if x > 0 {
		return 1
	} else {
		return -1
	}
}

func InRange(lower int, higher int, num int) bool {
	return num >= lower && num < higher
}

func Input(filename string) []string {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal("input file not found")
	}

	input, err := io.ReadAll(file)
	if err != nil {
		log.Fatal("file not readable")
	}

	input_string := string(input)

	input_string = strings.TrimSpace(input_string)
	lines := strings.Split(input_string, "\n")

	for index, line := range lines {
		line = strings.ReplaceAll(line, "\n", "")
		lines[index] = strings.TrimSpace(line)
	}

	return lines
}

func RemoveFromList[T any](list []T, index int) []T {
	length := len(list)

	if index <= 0 {
		return list[1:]
	} else if index >= length-1 {
		return list[:length-1]
	} else {
		return append(list[0:index], list[index+1:]...)
	}
}
