#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(

KC_SYSTEM_SLEEP,
LALT(KC_LSFT),
KC_MEDIA_NEXT_TRACK,
KC_MY_COMPUTER,
KC_MEDIA_PREV_TRACK,
KC_WWW_SEARCH,
KC_CALCULATOR,
KC_MEDIA_PLAY_PAUSE,
KC_AUDIO_MUTE
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