#include <string.h>
#include "pico/stdlib.h"

#define RS_PIN 3
#define RW_PIN 4
#define E_PIN 5

#define BASE_DATA_PIN 8

#define PINS 0x0000ff38

const char hello[] = "Hello, world!";

void initDisplay();
void send();
void sendInstruction(uint8_t data);
void setData(uint8_t data);
void writeCharacter(char data);
void writeString(const char text[], int len);

int main() {
  gpio_init_mask(PINS);
  gpio_set_dir_out_masked(PINS);

  initDisplay();

  writeString(hello, strlen(hello));
}

void initDisplay() {
  sendInstruction(0b00111000);
  sendInstruction(0b00001110);
  sendInstruction(0b00000110);
}

void send() {
  gpio_put(E_PIN, true);
  sleep_ms(5);
  gpio_put(E_PIN, false);
}

void sendInstruction(uint8_t data) {
  gpio_put(E_PIN, false);
  gpio_put(RS_PIN, false);
  gpio_put(RW_PIN, false);

  setData(data);

  send();
}

void setData(uint8_t data) {
  for (int i = 0; i < 8; ++i, data >>= 1) {
    gpio_put(BASE_DATA_PIN + i, data & 1);
  }
}

void writeCharacter(char data) {
  gpio_put(E_PIN, false);
  gpio_put(RS_PIN, true);
  gpio_put(RW_PIN, false);

  setData((uint8_t) data);

  send();
}

void writeString(const char text[], int len) {
  for (int i = 0; i < len; ++i) {
    writeCharacter(text[i]);
  }
}
