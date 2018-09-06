#!/usr/bin/env python3
import ev3dev.ev3 as ev3

motorEsq = ev3.LargeMotor('outC'); assert motorEsq.connected
motorDir = ev3.LargeMotor('outB'); assert motorDir.connected
## motorGarra = ev3.MediumMotor('outA'); assert motorGarra.connected

## Sensores de cor
corEsq = ev3.ColorSensor('in1'); assert corEsq.connected
corEsq.mode = 'COL-COLOR'

corDir = ev3.ColorSensor('in4'); assert corDir.connected
corDir.mode = 'COL-COLOR'

corCheck = ev3.ColorSensor('in2'); assert corCheck.connected
corCheck.mode = 'COL-COLOR'

while True:

  print("Estou aqui!", valorCorCheck())
