day ?= 1

default:
	g++ -c main.cpp; g++ -c day$(day).cpp; g++ main.o day$(day).o

new:
	cat day.txt > day$(day).cpp

test: default
	./a.out sample.txt

run: default
	./a.out input.txt

rmobj:
	rm *.o

clean: rmobj
	rm a.out
