#import gopigo3 library
import easygopigo3 as easy

#instantiate a gopigo in memory
#var my_gopigo = physical robot
my_gopigo = easy.EasyGoPiGo3()

#drive 10cm
my_gopigo.drive_cm(10)

#some other commands
#these never tell the robot when to stop
my_gopigo.forward()
my_gopigo.backward()
my_gopigo.right()
my_gopigo.left()

my_gopigo.stop()


#this command uses inches and negative numbers to go backwards
my_gopigo.drive_inches(-10)

#use these to turn
my_gopigo.turn_degrees(90)
my_gopigo.turn_degress(-90)

my_gopigo.stop()