# =========================================
# Makers! Implement your own actions here.
# =========================================

from gpiozero import Servo
from time import sleep


class ServoMove(object):
    def __init__(self):
        self.servo=Servo(26)
        #self.value=value;
    def SetAngle(angle):
        duty=angle/18+2
        GPIO.output(self.servo,True)
        pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(self.servo,False)
        pwm.ChangeDutyCycle(0)

    def run(self, voice_command):
        if 'boy' in voice_command:
            for i in range (0,5):
                SetAngle(90)
                sleep(2)
                SetAngle(180)
                sleep(1)

 # =========================================
 # Makers! Add your own voice commands here.
 # =========================================

    actor.add_keyword('good', ServoMove())

    return actor


class MotorMove(object):
    def __init__(self):
        self.pwm = PWMOutputDevice(4)
    def run(self, voice_command):
        if 'bacon' in voice_command:
            self.pwm.on()
        elif 'work' in voice_command:
            self.pwm.off()

    actor.add_keyword('bacon',MotorMove())
    actor.add_keyword('work',MotorMove())

 # =========================================
 # Makers! Add your own voice commands here.
 # =========================================

    return actor;
