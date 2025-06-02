default:
	g++ main.cpp 

day ?= 0
new:
	cat day.txt > day$(day).cpp

test: default
	./a.out sample.txt

run: default
	./a.out input.txt

clean:
	rm a.out
