#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        KC_P7,   KC_P8,   KC_P9,
        KC_P4,   KC_P5,   KC_P6,
        KC_P1,   KC_P2,   KC_P3
    )
};

#ifdef OLED_ENABLE
bool oled_task_user(void) 
{
oled_set_cursor(0, 1);

oled_write("hello hackers!", false);
return false;
}
#endif