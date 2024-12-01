package utils

import (
	"io"
	"log"
	"os"
	"strings"
)

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
