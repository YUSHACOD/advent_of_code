/*
 * A -> Rock    <- X : 1
 * B -> Paper   <- Y : 2
 * C -> Scizzor <- Z : 3
 * Loss : 0
 * Win  : 6
 * Drow : 3
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

#define WIN 6
#define DRAW 3
#define LOSS 0

#define Rock 1
#define Paper 2
#define Scizzor 3

#define _roundCount_ 2500

// Shit for first case start
/*int calculateRoundOutcome(int *roundBuff) {
  if (roundBuff[0] == roundBuff[1]) {
    return DRAW + roundBuff[1];
  } else if ((roundBuff[1] == Rock) && (roundBuff[0] == Scizzor)) {
    return WIN + Rock;
  } else if ((roundBuff[1] == Paper) && (roundBuff[0] == Rock)) {
    return WIN + Paper;
  } else if ((roundBuff[1] == Scizzor) && (roundBuff[0] == Paper)) {
    return WIN + Scizzor;
  } else {
    return LOSS + roundBuff[1];
  }
}*/
// Shit for first case end

// Shit for second case start
int inverse_of(int n, int state) {
  if (state == WIN) {
    if (n == Rock) {
      return Paper;
    } else if (n == Paper) {
      return Scizzor;
    } else {
      return Rock;
    }
  } else {
    if (n == Rock) {
      return Scizzor;
    } else if (n == Paper) {
      return Rock;
    } else {
      return Paper;
    }
  }
}

int calculate_round_outcome(int *roundBuff) {
  if (roundBuff[1] == Rock) {
    return LOSS + inverse_of(roundBuff[0], LOSS);
  } else if (roundBuff[1] == Paper) {
    return DRAW + roundBuff[0];
  } else {
    return WIN + inverse_of(roundBuff[0], WIN);
  }
}
// Shit for second case end

int main(int argc, char *argv[]) {
  char ch = 0;
  int round[2], move = 0, scorePerRound[_roundCount_], roundCount = 0;
  int total = 0;
  FILE *fp;
  fp = fopen("input.txt", "r");
  // fp = fopen("testIn.txt", "r");

  while ((ch = fgetc(fp)) != EOF) {
    if (ch == '\n') {
      scorePerRound[roundCount++] = calculate_round_outcome(round);
      for (int i = 0; i < 2; i++)
        round[i] = 0;
    } else if (ch == ' ') {
      continue;
    } else {
      switch (ch) {
      case ('A'):
        round[move] = Rock;
        move++;
        break;

      case ('B'):
        round[move] = Paper;
        move++;
        break;

      case ('C'):
        round[move] = Scizzor;
        move++;
        break;

      case ('X'):
        round[move] = Rock;
        move = 0;
        break;

      case ('Y'):
        round[move] = Paper;
        move = 0;
        break;

      case ('Z'):
        round[move] = Scizzor;
        move = 0;
        break;

      default:
        printf("Some error\n");
        exit(1);
        break;
      }
    }
  }

  for (int i = 0; i < _roundCount_; i++) {
    total += scorePerRound[i];
  }

  printf("The end of the program ,\n round count = %d, total = %d\n",
         roundCount, total);

  fclose(fp);
  return 0;
}
