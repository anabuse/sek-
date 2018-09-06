#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

motorGarra = ev3.MediumMotor('outA'); assert motorGarra.connected
motorDir = ev3.LargeMotor('outC'); assert motorDir.connected
motorEsq = ev3.LargeMotor('outD'); assert motorEsq.connected

us = ev3.UltrasonicSensor('in4'); assert us.connected

vel = -100

while True:

    distancia = us.distance_centimeters

    print(str(distancia) + ' cm\n')

    motorDir.run_timed(time_sp=100, speed_sp=vel)
    motorEsq.run_timed(time_sp=100, speed_sp=vel)

    if distancia < 5:
        motorDir.stop()
        motorEsq.stop()

        motorGarra.run_to_rel_pos(position_sp=-360, speed_sp=100)
        motorGarra.wait_while('running')
        motorDir.run_timed(time_sp=4000, speed_sp=-vel)
        motorEsq.run_timed(time_sp=4000, speed_sp=-vel)
        motorEsq.wait_while('running')
        motorDir.wait_while('running')
        motorGarra.run_to_rel_pos(position_sp=360, speed_sp=100)
        motorGarra.wait_while('running')
        motorDir.run_timed(time_sp=4000, speed_sp=-vel)
        motorEsq.run_timed(time_sp=4000, speed_sp=-vel)






    
