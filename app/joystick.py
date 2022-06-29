import pygame
from socket import timeout
import serial
import time 
from networktables import NetworkTables
import networktables
import pygame

NetworkTables.initialize()
table = NetworkTables.getTable("joystick")

sit = True
hizBoleni = 1
tolerans = 30

maxdeger = 1940
mindeger = 1060

xAxis = yAxis = x2Axis = y2Axis = 0.0
xAxisVal = yAxisVal = x2AxisVal = y2AxisVal = 0
condition1 = condition2 = condition3 = condition4 = 0

joystickMessage = ""

#serialcomm = serial.Serial('COM13', 115200) # Seri Haberleşme 
#serialcomm.timeout = 1

pygame.init() # Joystick 

while sit:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    for event in pygame.event.get():
        axes = joystick.get_numaxes() 
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.JOYBUTTONDOWN:
             print("Joystick button released.")
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.",pygame.JOYBUTTONUP,joystick.get_id())

    condition1 = joystick.get_button(11)
    if condition1 == 1:
            condition1 = 0
    elif condition1 == 0:
            condition1 = 1
    condition2 = joystick.get_button(12)
    condition3 = joystick.get_button(4)
    condition4 = joystick.get_button(2)

    xAxis = joystick.get_axis(0) + 1
    yAxis = joystick.get_axis(1) + 1
    x2Axis = joystick.get_axis(3) + 1
    y2Axis = joystick.get_axis(4) + 1
    
    xAxis = (512*xAxis)
    yAxis = (512*yAxis)
    x2Axis = (512*x2Axis)
    y2Axis = (512*y2Axis)

    xAxisVal = int(xAxis) +1000
    yAxisVal = 3000 - (int(yAxis) + 1000)
    x2AxisVal = 3000 - (int(x2Axis) + 1000)
    y2AxisVal = int(y2Axis) + 1000

    xAxisVal = 1500 + (xAxisVal - 1500) / hizBoleni
    yAxisVal = 1500 + (yAxisVal - 1500) / hizBoleni
    x2AxisVal = 1500 + (x2AxisVal - 1500) / hizBoleni
    y2AxisVal = 1500 + (y2AxisVal - 1500) / hizBoleni

    if (xAxisVal > maxdeger): xAxisVal = maxdeger
    if (yAxisVal > maxdeger): yAxisVal = maxdeger
    if (x2AxisVal > maxdeger): x2AxisVal = maxdeger
    if (y2AxisVal > maxdeger): y2AxisVal = maxdeger
    
    if (xAxisVal < mindeger): xAxisVal = mindeger
    if (yAxisVal < mindeger): yAxisVal = mindeger
    if (x2AxisVal < mindeger): x2AxisVal = mindeger
    if (y2AxisVal < mindeger): y2AxisVal = mindeger

    if (xAxisVal < 1500 + tolerans / hizBoleni and xAxisVal > 1500 - tolerans / hizBoleni): xAxisVal = 1500
    if (yAxisVal < 1500 + tolerans / hizBoleni and yAxisVal > 1500 - tolerans / hizBoleni): yAxisVal = 1500
    if (x2AxisVal < 1500 + tolerans / hizBoleni and x2AxisVal > 1500 - tolerans / hizBoleni): x2AxisVal = 1500
    if (y2AxisVal < 1500 + tolerans / hizBoleni and y2AxisVal > 1500 - tolerans / hizBoleni): y2AxisVal = 1500

    joystickMessage = str(int(xAxisVal))+str(int(yAxisVal))+str(int(x2AxisVal))+str(int(y2AxisVal))+str(condition1)+str(condition2)+str(condition3)+str(condition4)
    
    # serialcomm.write(i.encode())
    # print(serialcomm.readline().decode(encoding="ascii"))
    
    print(joystickMessage)
    table.putString("value",joystickMessage)
