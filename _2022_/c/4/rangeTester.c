#include <stdio.h>
#include <stdlib.h>

int RangeTester(int **buffer) {
  printf("hi");
  if (((buffer[0][0]) <= (buffer[1][0])) &&
      ((buffer[0][1]) >= (buffer[1][1]))) {
    return 1;
  } else if (((buffer[0][0]) >= (buffer[1][0])) &&
             ((buffer[0][1]) <= (buffer[1][1]))) {
    return 1;
  } else {
    return 0;
  }
}

int main(int argc, char *argv[]) {
  int **buffer;
  buffer = (int **)calloc(2, sizeof(int *));
  buffer[0] = (int *)calloc(2, sizeof(int));
  buffer[1] = (int *)calloc(2, sizeof(int));
  printf("helo");
  scanf("%d", &buffer[0][0]);
  printf("helo");
  scanf("%d", &buffer[0][1]);
  printf("helo");
  scanf("%d", &buffer[1][0]);
  printf("helo");
  scanf("%d", &buffer[1][1]);
  printf("helo");
  printf("helo");
  printf("return : %d", RangeTester(buffer));
  return 0;
}
