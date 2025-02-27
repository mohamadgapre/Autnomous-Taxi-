from robot_hat import PWM
import time

LeftBrakeLED = PWM(8)
LeftTurnLED = PWM(9)
RightTurnLED = PWM(11)
RightBrakeLED = PWM(10)

LeftTurnLED.Prescaler = 100000000
RightTurnLED.Prescaler = 100000000
LeftTurnLED.period(1000)
RightTurnLED.period(1000)
RightBrakeLED.freq(1000)
LeftBrakeLED.freq(1000)

LeftTurnLED.pulse_width_percent(0)
RightTurnLED.pulse_width_percent(0)  
RightBrakeLED.pulse_width_percent(0)
LeftBrakeLED.pulse_width_percent(0)

def LeftLEDStart():
    LeftTurnLED.pulse_width(500)

def LeftLEDStop():
    LeftTurnLED.pulse_width(0)

def RightLEDStart():
    RightTurnLED.pulse_width(500)
        
def RightLEDStop():
    RightTurnLED.pulse_width(0)

def HazardLEDStart():
    LeftTurnLED.pulse_width(500)
    RightTurnLED.pulse_width(500)

def HazardLEDStop():
    RightTurnLED.pulse_width(0)
    LeftTurnLED.pulse_width(0)

def BrakingLEDStart():
    RightBrakeLED.pulse_width_percent(100)
    LeftBrakeLED.pulse_width_percent(100)


def BrakingLEDStop():
    RightBrakeLED.pulse_width_percent(0)
    LeftBrakeLED.pulse_width_percent(0)
