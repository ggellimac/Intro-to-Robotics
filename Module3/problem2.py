from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''

import csv
import easygopigo3 as easy
my_gopigo = easy.EasyGoPiGo3()

import time     # import the time library for the sleep function
import gopigo3 # import the GoPiGo3 drivers

gpg = easy.EasyGoPiGo3()
GPG = gopigo3.GoPiGo3() # Create an instance of the GoPiGo3 class. GPG will be the GoPiGo3 object.

my_distance_sensor = gpg.init_distance_sensor()

distance = 25

distance_list = []
encoder_list_left = []
encoder_list_right = []

try:
    GPG.offset_motor_encoder(GPG.MOTOR_LEFT, GPG.get_motor_encoder(GPG.MOTOR_LEFT))
    GPG.offset_motor_encoder(GPG.MOTOR_RIGHT, GPG.get_motor_encoder(GPG.MOTOR_RIGHT))
    #while nothing is within 25 cm, go in a square
    while my_distance_sensor.read() > distance:
            print("Distance Sensor Reading: {} cm ".format(my_distance_sensor.read()))
            distance_list.append(my_distance_sensor.read())
            print("Encoder L: %6d  R: %6d" % (GPG.get_motor_encoder(GPG.MOTOR_LEFT),                                        GPG.get_motor_encoder(GPG.MOTOR_RIGHT)))
            encoder_list_left.append(GPG.get_motor_encoder(GPG.MOTOR_LEFT))
            encoder_list_right.append(GPG.get_motor_encoder(GPG.MOTOR_RIGHT))

            my_gopigo.drive_inches(19.685)

            print("Distance Sensor Reading: {} cm ".format(my_distance_sensor.read()))
            distance_list.append(my_distance_sensor.read())
            print("Encoder L: %6d  R: %6d" % (GPG.get_motor_encoder(GPG.MOTOR_LEFT),                                        GPG.get_motor_encoder(GPG.MOTOR_RIGHT)))
            encoder_list_left.append(GPG.get_motor_encoder(GPG.MOTOR_LEFT))
            encoder_list_right.append(GPG.get_motor_encoder(GPG.MOTOR_RIGHT))

            my_gopigo.turn_degrees(90)

            print("Distance Sensor Reading: {} cm ".format(my_distance_sensor.read()))
            distance_list.append(my_distance_sensor.read())
            print("Encoder L: %6d  R: %6d" % (GPG.get_motor_encoder(GPG.MOTOR_LEFT),                                        GPG.get_motor_encoder(GPG.MOTOR_RIGHT)))
            encoder_list_left.append(GPG.get_motor_encoder(GPG.MOTOR_LEFT))
            encoder_list_right.append(GPG.get_motor_encoder(GPG.MOTOR_RIGHT))

    #if something is within 25 cm, go around
            if my_distance_sensor.read() < distance:
                my_gopigo.turn_degrees(90)
                    print("Distance Sensor Reading: {} cm ".format(my_distance_sensor.read()))
                    distance_list.append(my_distance_sensor.read())
                    print("Encoder L: %6d  R: %6d" % (GPG.get_motor_encoder(GPG.MOTOR_LEFT),                                        GPG.get_motor_encoder(GPG.MOTOR_RIGHT)))
                    encoder_list_left.append(GPG.get_motor_encoder(GPG.MOTOR_LEFT))
                    encoder_list_right.append(GPG.get_motor_encoder(GPG.MOTOR_RIGHT))
                         
                    my_gopigo.drive_inches(19.685)

                    print("Distance Sensor Reading: {} cm ".format(my_distance_sensor.read()))
                    distance_list.append(my_distance_sensor.read())
                    print("Encoder L: %6d  R: %6d" % (GPG.get_motor_encoder(GPG.MOTOR_LEFT),                                        GPG.get_motor_encoder(GPG.MOTOR_RIGHT)))
                    encoder_list_left.append(GPG.get_motor_encoder(GPG.MOTOR_LEFT))
                    encoder_list_right.append(GPG.get_motor_encoder(GPG.MOTOR_RIGHT))

                    my_gopigo.turn_degrees(-90)

                    print("Distance Sensor Reading: {} cm ".format(my_distance_sensor.read()))
                    distance_list.append(my_distance_sensor.read())
                    print("Encoder L: %6d  R: %6d" % (GPG.get_motor_encoder(GPG.MOTOR_LEFT),                                        GPG.get_motor_encoder(GPG.MOTOR_RIGHT)))
                    encoder_list_left.append(GPG.get_motor_encoder(GPG.MOTOR_LEFT))
                    encoder_list_right.append(GPG.get_motor_encoder(GPG.MOTOR_RIGHT))
                    
  

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    GPG.reset_all()        # Unconfigure the sensors, disable the motors, and restore the LED to the control of the GoPiGo3 firmware.

with open("problem2_pathtrace.csv", "w") as out_file:
    fieldnames = ['index_row', 'Distance Sensor', 'LWheel Encoder Val', 'RWHeel Encoder Val']
    csv_writer = csv.DictWriter(out_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    for i in range(len(distance_list)):
        out_string = ""
        out_string += str(i) + "\t"
        out_string += str(distance_list[i])
        out_string += "," + str(encoder_list_left[i])
        out_string += "," + str(encoder_list_right[i])
        out_file.write(out_string)
        print (out_string)
        

