#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define _GroupCount_ 100

char getSameChar(char **buffer, int *size) {
  char ch = 0;
  for (int i = 0; i < size[0]; i++) {
    for (int j = 0; j < size[1]; j++) {
      if (buffer[1][j] == buffer[0][i]) {
        ch = buffer[0][i];
        for (int k = 0; k < size[2]; k++) {
          if (ch == buffer[2][k]) {
            return ch;
          }
        }
      }
    }
  }
  return ch;
}

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
  char ch, *Sacks[3];
  int groupCounter = 0, groups[_GroupCount_], itemCounter = 0,
      total = 0, sackSizes[3], sackCounter = 0;
  // fp = fopen("testInput.txt", "r");
  fp = fopen("input.txt", "r");

  while ((ch = fgetc(fp)) != EOF) {
    if (ch == '\n') {
      sackSizes[sackCounter] = itemCounter;
      Sacks[sackCounter] = (char *)calloc(sackSizes[sackCounter], sizeof(char));
	  fseek(fp, -(sackSizes[sackCounter] + 1), SEEK_CUR);

      for (int i = 0; (ch = fgetc(fp)) != '\n'; i++) {
        Sacks[sackCounter][i] = ch;
      }

      sackCounter++;

      if (sackCounter == 3) {
		  groups[groupCounter++] = GetPriority(getSameChar(Sacks, sackSizes));

		  sackCounter = 0;
		  for (int i = 0; i < 3; i++) {
		 	free(Sacks[i]); 
		  }
      }

	  itemCounter = 0;
    } else {
      itemCounter++;
    }
  }

  for (int i = 0; i < _GroupCount_; i++) {
    total += groups[i];
  }

  printf("Sack Counter = %d, total = %d\n", sackCounter, total);

  fclose(fp);
  return 0;
}
