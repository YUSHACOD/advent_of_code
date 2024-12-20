#include <stdio.h>
#include <stdlib.h>

#define _sackCount_ 300

int ItemCompare(char *buffer, char ch, int size) {
  for (int k = 0; k <= size; k++) {
    if (buffer[k] == ch) {
      return 1;
    }
  }
  return 0;
}

int GetPriority(char ch) {
  if ((ch >= 'A') && (ch <= 'Z')) {
    return (ch - 'A' + 27);
  } else if ((ch >= 'a') && (ch <= 'z')) {
    return (ch - 'a' + 1);
  } else {
    exit(1);
  }
}

int main(int argc, char *argv[]) {
  FILE *fp;
  char ch, *firstCompartment;
  int sackCounter = 0, sacks[_sackCount_], itemCounter = 0, compartmentSize = 0,
      total = 0, flag = 0;
  // fp = fopen("testInput.txt", "r");
  fp = fopen("input.txt", "r");

  while ((ch = fgetc(fp)) != EOF) {
    if (ch == '\n') {
      compartmentSize = itemCounter / 2;
      firstCompartment = (char *)calloc(compartmentSize, sizeof(char));
      fseek(fp, -(itemCounter + 1), SEEK_CUR);

      for (int k = 0; (ch = fgetc(fp)) != '\n'; k++) {
        if (k < compartmentSize) {
          firstCompartment[k] = ch;
        } else {
          if (ItemCompare(firstCompartment, ch, compartmentSize) && flag == 0) {
            sacks[sackCounter++] = GetPriority(ch);
            flag = 1;
          }
        }
      }

      itemCounter = compartmentSize = flag = 0;
      free(firstCompartment);
    } else {
      itemCounter++;
    }
  }

  for (int i = 0; i < _sackCount_; i++) {
    total += sacks[i];
  }

  printf("Sack Counter = %d, total = %d\n", sackCounter, total);

  fclose(fp);
  return 0;
}
