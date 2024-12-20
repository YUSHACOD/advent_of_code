#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int partition(int arr[], int low, int high) {
  int pivot = arr[high];
  int i = (low - 1), tmp;

  for (int j = low; j <= high - 1; j++) {
    if (arr[j] < pivot) {
      i++;
      tmp = arr[i];
      arr[i] = arr[j];
      arr[j] = tmp;
    }
  }
  tmp = arr[i + 1];
  arr[i + 1] = arr[high];
  arr[high] = tmp;

  return (i + 1);
}

void sort(int h[], int low, int high) {
  if (low < high) {
    int pi = partition(h, low, high);

    sort(h, low, pi - 1);
    sort(h, pi + 1, high);
  }
}

int convert_to_calorie(char *buff, int length) {
  int temp = 0;
  for (int i = 0; buff[i] != 0; i++) {
    temp += (buff[i] - 48) * ((int)pow(10, length - 1));
    length--;
  }
  return temp;
}

int main(int argc, char *argv[]) {

  char ch, prev, buffer[20] = {0};
  int item_length, new_calorie_sum = 0, old_calorie_sum = 0, elve_count = 0,
                   *total_calorie_per_elve;

  FILE *fp = fopen("input.txt", "r");
  total_calorie_per_elve = (int *)calloc(255, sizeof(int));

  while ((ch = fgetc(fp)) != EOF) {

    if (ch == '\n') {
      if (ch == prev) {

        printf("Elvecount = %d\n", elve_count);
        total_calorie_per_elve[elve_count] = new_calorie_sum;
        elve_count++;
        new_calorie_sum = 0;
        continue;

      } else {

        new_calorie_sum += convert_to_calorie(buffer, item_length);
        for (int i = 0; i < 20; i++) {
          buffer[i] = 0;
        }
        item_length = 0;

      }
    } else {
      buffer[item_length] = ch;
      item_length++;
    }

    prev = ch;
  }

  int total = 0;
  printf("hello\n");
  total_calorie_per_elve[elve_count] = new_calorie_sum;

  sort(total_calorie_per_elve, 0, 254);

  for (int i = 254; i > 251; i--) {
    total += total_calorie_per_elve[i];
    printf("top 3 = %d\n", total_calorie_per_elve[i]);
  }

  printf("ElveCount = %d Total = %d\n", ++elve_count, total);
  fclose(fp);

  return 0;
}
