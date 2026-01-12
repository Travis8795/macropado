# macropado
Macropado is a **8 key** macropad with a **rotary encoder** and an **OLED** screan and 8 SK6812 MINI Leds for **RGB** lights, it runs on **KMK** with python.

## CAD
Designed using **Fusion 360**.

The macropad is assembled by pressing heat-set inserts into the back of the top plate. Then, 16mm screws are inserted through the bottom of the base and the PCB, threading directly into the inserts to hold everything together.

<img width="992" height="665" alt="hackbad" src="https://github.com/user-attachments/assets/bd02f380-c402-4db4-9997-3d04c2e38eac" />

| front | back |
| :---: | :---: |
| <img width="1081" height="707" alt="base" src="https://github.com/user-attachments/assets/db0b47d0-61e0-4e7e-bfa3-89681e0f549b" /> | <img width="757" height="372" alt="base back" src="https://github.com/user-attachments/assets/66579155-b59f-4109-a108-542981b2c3f8" /> |
| <img width="1012" height="693" alt="plate" src="https://github.com/user-attachments/assets/bd134e1a-45c7-49de-85e7-f4e5e32f03ad" /> | <img width="711" height="685" alt="plate back" src="https://github.com/user-attachments/assets/23dc27ee-81e4-420c-b23a-4c11f8438dc8" /> |

## PCB
Designed using **KiCad**.

| Schematic | PCB |
| :---: | :---: |
| <img width="1127" height="774" alt="image" src="https://github.com/user-attachments/assets/862895ed-f3f9-43b6-a565-f52dac883ab2" /> | <img width="841" height="592" alt="PCB" src="https://github.com/user-attachments/assets/c60fe072-5dc6-4f44-912f-03be4dfbeae0" /> |

## Firmware overview
Macropado runs on **KMK firmware** using CircuitPython for easy, "on-the-fly" customization.

* **Rotary Encoder:** Adjusts system volume with a press-to-mute function.
* **8 Programmable Keys:** Currently configured as custom macros for productivity.
* **OLED Screen:** Features a custom **Bongocat** animation! :3
* **RGB Lighting:** 8 addressable SK6812 MINI LEDs for dynamic status effects.

All logic is written in Python using KMK modules and extensions.

## BOM:
Here is **everything** you need to make this macropad

- 1x XIAO RP2040
- 8x Cherry MX Switches
- 8x DSA Keycaps
- 4x M3x5x4 Heatset inserts
- 4x M3x16mm screws
- 9x 1N4148 DO-35 Diodes.
- 8x SK6812 MINI LEDs
- 1x 0.91" 128x32 OLED Display
- 1x EC11 Rotary Encoder
- 1x Case (3 printed parts)

---
A huge shout-out to Hack Club and the Blueprint team!

I’ve dreamed of making this macropad for a long time, but I failed my previous attempts. Blueprint was the awesome opportunity I needed. The community support was amazing and helped me through the tough parts!

This was my first time ever using Fusion 360 for CAD, KiCad for PCB design, and my first time 'shipping' a complete GitHub repo. I learned so much during this YSWS journey. Thank you for everything—I owe you guys a lot! I'm so proud of my Macropado. <3
