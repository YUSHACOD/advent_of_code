package stack

import (
	"log"
)

type Stack[T any] struct {
	mem  []T
	head int
}

func NewStack[T any](size int) *Stack[T] {
	return &Stack[T]{
		mem:  make([]T, size),
		head: -1,
	}
}

func (stack *Stack[T]) Pop() T {
	if stack.head < 0 {
		log.Fatal("Stack is empty")
	}

	top := stack.mem[stack.head]
	stack.mem = stack.mem[:stack.head-1]
	stack.head -= 1
	return top
}

func (stack Stack[T]) Push(elem T) {
	stack.mem = append(stack.mem, elem)
	stack.head += 1
}
