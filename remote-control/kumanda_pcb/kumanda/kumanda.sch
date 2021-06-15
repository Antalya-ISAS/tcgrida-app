EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Mechanical:MountingHole H1
U 1 1 60C27A3F
P 9400 1250
F 0 "H1" H 9500 1296 50  0000 L CNN
F 1 "MountingHole" H 9500 1205 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3" H 9400 1250 50  0001 C CNN
F 3 "~" H 9400 1250 50  0001 C CNN
	1    9400 1250
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H2
U 1 1 60C27B21
P 9400 1600
F 0 "H2" H 9500 1646 50  0000 L CNN
F 1 "MountingHole" H 9500 1555 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3" H 9400 1600 50  0001 C CNN
F 3 "~" H 9400 1600 50  0001 C CNN
	1    9400 1600
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H3
U 1 1 60C28E13
P 9450 1950
F 0 "H3" H 9550 1996 50  0000 L CNN
F 1 "MountingHole" H 9550 1905 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3" H 9450 1950 50  0001 C CNN
F 3 "~" H 9450 1950 50  0001 C CNN
	1    9450 1950
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H4
U 1 1 60C28E1D
P 9450 2250
F 0 "H4" H 9550 2296 50  0000 L CNN
F 1 "MountingHole" H 9550 2205 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3" H 9450 2250 50  0001 C CNN
F 3 "~" H 9450 2250 50  0001 C CNN
	1    9450 2250
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x03 VIB1
U 1 1 60C624BB
P 2900 5850
F 0 "VIB1" H 2980 5892 50  0000 L CNN
F 1 "Conn_01x03" H 2980 5801 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-03A_1x03_P2.54mm_Vertical" H 2900 5850 50  0001 C CNN
F 3 "~" H 2900 5850 50  0001 C CNN
	1    2900 5850
	-1   0    0    1   
$EndComp
$Comp
L Connector_Generic:Conn_01x03 POT1
U 1 1 60C62DF7
P 2900 3750
F 0 "POT1" H 2980 3792 50  0000 L CNN
F 1 "Conn_01x03" H 2980 3701 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-03A_1x03_P2.54mm_Vertical" H 2900 3750 50  0001 C CNN
F 3 "~" H 2900 3750 50  0001 C CNN
	1    2900 3750
	-1   0    0    1   
$EndComp
$Comp
L Connector_Generic:Conn_01x03 POT2
U 1 1 60C6321A
P 9550 3850
F 0 "POT2" H 9630 3892 50  0000 L CNN
F 1 "Conn_01x03" H 9630 3801 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-03A_1x03_P2.54mm_Vertical" H 9550 3850 50  0001 C CNN
F 3 "~" H 9550 3850 50  0001 C CNN
	1    9550 3850
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x03 DHT1
U 1 1 60C63350
P 2900 5150
F 0 "DHT1" H 2980 5192 50  0000 L CNN
F 1 "Conn_01x03" H 2980 5101 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-03A_1x03_P2.54mm_Vertical" H 2900 5150 50  0001 C CNN
F 3 "~" H 2900 5150 50  0001 C CNN
	1    2900 5150
	-1   0    0    1   
$EndComp
$Comp
L Connector_Generic:Conn_01x04 OLED_I2C1
U 1 1 60C67BF7
P 4750 5800
F 0 "OLED_I2C1" H 4830 5792 50  0000 L CNN
F 1 "Conn_01x04" H 4830 5701 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-04A_1x04_P2.54mm_Vertical" H 4750 5800 50  0001 C CNN
F 3 "~" H 4750 5800 50  0001 C CNN
	1    4750 5800
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x03 VIB2
U 1 1 60C77FDA
P 9550 5100
F 0 "VIB2" H 9630 5142 50  0000 L CNN
F 1 "Conn_01x03" H 9630 5051 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-03A_1x03_P2.54mm_Vertical" H 9550 5100 50  0001 C CNN
F 3 "~" H 9550 5100 50  0001 C CNN
	1    9550 5100
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x02 CAN_Bus2
U 1 1 60C7B460
P 7800 5700
F 0 "CAN_Bus2" H 7880 5692 50  0000 L CNN
F 1 "Conn_01x02" H 7880 5601 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-02A_1x02_P2.54mm_Vertical" H 7800 5700 50  0001 C CNN
F 3 "~" H 7800 5700 50  0001 C CNN
	1    7800 5700
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x07 CAN_Bus1
U 1 1 60C799FE
P 6300 5700
F 0 "CAN_Bus1" H 6380 5742 50  0000 L CNN
F 1 "Conn_01x07" H 6380 5651 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-07A_1x07_P2.54mm_Vertical" H 6300 5700 50  0001 C CNN
F 3 "~" H 6300 5700 50  0001 C CNN
	1    6300 5700
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x02 CAN_H_L1
U 1 1 60C7C262
P 7000 6150
F 0 "CAN_H_L1" H 7080 6142 50  0000 L CNN
F 1 "Conn_01x02" H 7080 6051 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-02A_1x02_P2.54mm_Vertical" H 7000 6150 50  0001 C CNN
F 3 "~" H 7000 6150 50  0001 C CNN
	1    7000 6150
	0    1    1    0   
$EndComp
$Comp
L Connector:RJ45 J3
U 1 1 60C7E37E
P 6200 2700
F 0 "J3" H 6257 3367 50  0000 C CNN
F 1 "RJ45" H 6257 3276 50  0000 C CNN
F 2 "Connector_RJ:RJ45_Ninigi_GE" V 6200 2725 50  0001 C CNN
F 3 "~" V 6200 2725 50  0001 C CNN
	1    6200 2700
	0    1    1    0   
$EndComp
$Comp
L Connector_Generic:Conn_01x05 Joy1
U 1 1 60C83B6D
P 2900 4350
F 0 "Joy1" H 2980 4392 50  0000 L CNN
F 1 "Conn_01x05" H 2980 4301 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-05A_1x05_P2.54mm_Vertical" H 2900 4350 50  0001 C CNN
F 3 "~" H 2900 4350 50  0001 C CNN
	1    2900 4350
	-1   0    0    1   
$EndComp
$Comp
L Connector_Generic:Conn_01x05 Joy2
U 1 1 60C842E4
P 9550 4450
F 0 "Joy2" H 9630 4492 50  0000 L CNN
F 1 "Conn_01x05" H 9630 4401 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-05A_1x05_P2.54mm_Vertical" H 9550 4450 50  0001 C CNN
F 3 "~" H 9550 4450 50  0001 C CNN
	1    9550 4450
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x03 Switch1
U 1 1 60C85709
P 2950 3050
F 0 "Switch1" H 3030 3092 50  0000 L CNN
F 1 "Conn_01x03" H 3030 3001 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-03A_1x03_P2.54mm_Vertical" H 2950 3050 50  0001 C CNN
F 3 "~" H 2950 3050 50  0001 C CNN
	1    2950 3050
	-1   0    0    1   
$EndComp
Wire Wire Line
	7000 5950 6900 5950
$Comp
L Connector:USB_A J1
U 1 1 60CA6300
P 7800 2850
F 0 "J1" V 7811 3180 50  0000 L CNN
F 1 "USB_A" V 7902 3180 50  0000 L CNN
F 2 "Connector_USB:USB_A_CONNFLY_DS1095-WNR0" H 7950 2800 50  0001 C CNN
F 3 " ~" H 7950 2800 50  0001 C CNN
	1    7800 2850
	0    1    1    0   
$EndComp
$Comp
L Connector_Generic:Conn_01x03 Switch2
U 1 1 60C85F12
P 9550 3450
F 0 "Switch2" H 9630 3492 50  0000 L CNN
F 1 "Conn_01x03" H 9630 3401 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-03A_1x03_P2.54mm_Vertical" H 9550 3450 50  0001 C CNN
F 3 "~" H 9550 3450 50  0001 C CNN
	1    9550 3450
	1    0    0    -1  
$EndComp
Wire Wire Line
	8600 3600 8600 3550
Wire Wire Line
	9050 3550 9050 3950
Wire Wire Line
	9050 3950 9350 3950
Wire Wire Line
	8600 3550 9050 3550
Connection ~ 9050 3550
Wire Wire Line
	9050 3550 9350 3550
Wire Wire Line
	9050 3950 9050 4250
Wire Wire Line
	9050 4250 9350 4250
Connection ~ 9050 3950
Wire Wire Line
	9050 4250 9050 5000
Wire Wire Line
	9050 5000 9350 5000
Connection ~ 9050 4250
Connection ~ 8600 3550
Wire Wire Line
	3300 3550 3300 2950
Wire Wire Line
	3300 2950 3150 2950
Connection ~ 6150 3550
Wire Wire Line
	3300 3550 3300 3650
Wire Wire Line
	3300 3650 3100 3650
Connection ~ 3300 3550
Wire Wire Line
	3300 3650 3300 4550
Wire Wire Line
	3300 4550 3100 4550
Connection ~ 3300 3650
Wire Wire Line
	3300 4550 3300 5250
Wire Wire Line
	3300 5250 3100 5250
Connection ~ 3300 4550
Wire Wire Line
	3300 5950 3100 5950
Connection ~ 3300 5250
Wire Wire Line
	3300 5700 4150 5700
Wire Wire Line
	3300 5250 3300 5700
Connection ~ 3300 5700
Wire Wire Line
	3300 5700 3300 5950
Wire Wire Line
	7400 3550 7400 2850
Wire Wire Line
	8600 3550 7400 3550
Wire Wire Line
	7400 3550 6150 3550
Connection ~ 7400 3550
Wire Wire Line
	4150 5700 4150 5500
Connection ~ 4150 5700
Wire Wire Line
	3900 3150 3400 3150
Wire Wire Line
	3400 3150 3400 3850
Wire Wire Line
	3400 3850 3100 3850
Connection ~ 3400 3150
Wire Wire Line
	3400 3150 3150 3150
Wire Wire Line
	3400 3850 3400 4450
Wire Wire Line
	3400 4450 3100 4450
Connection ~ 3400 3850
Wire Wire Line
	3400 4450 3400 5150
Wire Wire Line
	3400 5150 3100 5150
Connection ~ 3400 4450
Wire Wire Line
	3400 5150 3400 5750
Wire Wire Line
	3400 5750 3100 5750
Connection ~ 3400 5150
Wire Wire Line
	3400 5750 4100 5750
Connection ~ 3400 5750
Wire Wire Line
	4100 5750 4100 5400
Connection ~ 4100 5750
Wire Wire Line
	9250 3350 9250 3750
Wire Wire Line
	9250 3750 9350 3750
Connection ~ 9250 3350
Wire Wire Line
	9250 3350 9350 3350
Wire Wire Line
	9250 3750 9250 4350
Wire Wire Line
	9250 4350 9350 4350
Connection ~ 9250 3750
Wire Wire Line
	9250 4350 9250 5200
Wire Wire Line
	9250 5200 9350 5200
Connection ~ 9250 4350
$Comp
L Connector_Generic:Conn_01x04 J2
U 1 1 60D1844F
P 8800 5800
F 0 "J2" V 8672 5980 50  0000 L CNN
F 1 "Conn_01x04" V 8763 5980 50  0000 L CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-04A_1x04_P2.54mm_Vertical" H 8800 5800 50  0001 C CNN
F 3 "~" H 8800 5800 50  0001 C CNN
	1    8800 5800
	0    1    1    0   
$EndComp
Wire Wire Line
	8000 3150 8000 3350
Wire Wire Line
	8000 3350 9250 3350
Wire Wire Line
	9050 5000 8800 5000
Connection ~ 9050 5000
Wire Wire Line
	9250 5200 8900 5200
Wire Wire Line
	8900 5200 8900 5600
Connection ~ 9250 5200
Wire Wire Line
	8700 5200 8700 5600
Wire Wire Line
	8800 5000 8800 5450
$Comp
L Device:R R2
U 1 1 60D1689D
P 8250 5450
F 0 "R2" H 8320 5496 50  0000 L CNN
F 1 "R" H 8320 5405 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 8180 5450 50  0001 C CNN
F 3 "~" H 8250 5450 50  0001 C CNN
	1    8250 5450
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R1
U 1 1 60D14796
P 8650 5450
F 0 "R1" H 8720 5496 50  0000 L CNN
F 1 "R" H 8720 5405 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 8580 5450 50  0001 C CNN
F 3 "~" H 8650 5450 50  0001 C CNN
	1    8650 5450
	0    -1   -1   0   
$EndComp
Connection ~ 8800 5450
Wire Wire Line
	8800 5450 8800 5600
Wire Wire Line
	8400 5450 8500 5450
$Comp
L Device:R R3
U 1 1 60D21A05
P 7950 5300
F 0 "R3" H 8020 5346 50  0000 L CNN
F 1 "R" H 8020 5255 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 7880 5300 50  0001 C CNN
F 3 "~" H 7950 5300 50  0001 C CNN
	1    7950 5300
	1    0    0    -1  
$EndComp
Wire Wire Line
	8700 5200 5800 5200
Wire Wire Line
	5800 5200 5800 5000
Wire Wire Line
	7950 5150 8750 5150
Wire Wire Line
	8750 5150 8750 3450
Wire Wire Line
	8750 3450 5800 3450
Wire Wire Line
	5800 3450 5800 3600
Wire Wire Line
	8100 5450 7950 5450
Wire Wire Line
	7600 6000 10000 6000
Wire Wire Line
	10000 6000 10000 3200
Wire Wire Line
	7600 5800 7600 6000
Wire Wire Line
	3900 3150 3900 3350
Wire Wire Line
	8000 3350 3900 3350
Connection ~ 8000 3350
Connection ~ 3900 3350
Wire Wire Line
	3900 3350 3900 3600
Wire Wire Line
	6150 3200 6100 3200
Wire Wire Line
	6100 3200 6100 3100
Wire Wire Line
	6150 3200 6150 3550
Wire Wire Line
	6400 3200 6400 3100
Wire Wire Line
	6400 3200 10000 3200
Wire Wire Line
	6300 3100 6300 3250
Wire Wire Line
	6300 3250 6850 3250
Wire Wire Line
	6850 3250 6850 2500
Wire Wire Line
	6850 2500 8650 2500
Wire Wire Line
	8650 2500 8650 3100
Wire Wire Line
	8650 3100 10300 3100
Wire Wire Line
	10300 3100 10300 6150
Wire Wire Line
	10300 6150 7550 6150
Wire Wire Line
	7550 6150 7550 5700
Wire Wire Line
	7550 5700 7600 5700
Wire Wire Line
	7950 5450 7950 5600
Wire Wire Line
	7950 5600 8600 5600
Connection ~ 7950 5450
Wire Wire Line
	3100 4350 3500 4350
Wire Wire Line
	3500 3400 7700 3400
Wire Wire Line
	7700 3400 7700 3600
Wire Wire Line
	3100 4250 3550 4250
Wire Wire Line
	3550 4250 3550 5300
Wire Wire Line
	3550 5300 7700 5300
Wire Wire Line
	7700 5300 7700 5000
Wire Wire Line
	3100 4150 3600 4150
Wire Wire Line
	3600 4150 3600 3500
Wire Wire Line
	3600 3500 5100 3500
Wire Wire Line
	5100 3500 5100 3600
Wire Wire Line
	9350 4450 8950 4450
Wire Wire Line
	8950 4450 8950 3400
Wire Wire Line
	8950 3400 7800 3400
Wire Wire Line
	7800 3400 7800 3600
Wire Wire Line
	9350 4550 8900 4550
Wire Wire Line
	8900 4550 8900 5050
Wire Wire Line
	8900 5050 7800 5050
Wire Wire Line
	7800 5050 7800 5000
Wire Wire Line
	9350 4650 9350 4850
Wire Wire Line
	9350 4850 8600 4850
Wire Wire Line
	8600 4850 8600 5100
Wire Wire Line
	8600 5100 5100 5100
Wire Wire Line
	5100 5100 5100 5000
$Comp
L MEGA_PRO_EMBED_CH340G___ATMEGA2560-git:MEGA_PRO_EMBED_CH340G___ATMEGA2560 U1
U 1 1 60C9CA00
P 6200 4300
F 0 "U1" V 6246 6830 50  0000 L CNN
F 1 "MEGA_PRO_EMBED_CH340G___ATMEGA2560" V 6155 6830 50  0000 L CNN
F 2 "MODULE_MEGA_PRO_EMBED_CH340G_git:_ATMEGA2560" H 6200 4300 50  0001 L BNN
F 3 "" H 6200 4300 50  0001 L BNN
F 4 "12/May/2017" H 6200 4300 50  0001 L BNN "PARTREV"
F 5 "" H 6200 4300 50  0001 L BNN "MAXIMUM_PACKAGE_HIEGHT"
F 6 "Manufacturer Recommendations" H 6200 4300 50  0001 L BNN "STANDARD"
F 7 "Robotdyn" H 6200 4300 50  0001 L BNN "MANUFACTURER"
	1    6200 4300
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4550 5750 4550 5800
Wire Wire Line
	4550 5900 4450 5900
Wire Wire Line
	4450 5150 6000 5150
Wire Wire Line
	6000 5150 6000 5000
Wire Wire Line
	6150 3550 3300 3550
Wire Wire Line
	4550 6000 3650 6000
Wire Wire Line
	3650 6000 3650 3000
Wire Wire Line
	3650 3000 5600 3000
Wire Wire Line
	5600 3000 5600 3500
Wire Wire Line
	5600 3500 6000 3500
Wire Wire Line
	6000 3500 6000 3600
Wire Wire Line
	4150 5700 4550 5700
Wire Wire Line
	4450 5900 4450 5150
Wire Wire Line
	4100 5750 4550 5750
Text Label 4550 6000 2    50   ~ 0
SDA
Text Label 4550 5900 2    50   ~ 0
SCL
Text Label 4550 5800 2    50   ~ 0
VCC
Text Label 4550 5700 2    50   ~ 0
GND
Text Label 3150 2950 0    50   ~ 0
GND
Text Label 3100 3650 0    50   ~ 0
GND
Text Label 3100 4550 0    50   ~ 0
GND
Text Label 3100 5250 0    50   ~ 0
GND
Text Label 3100 5950 0    50   ~ 0
GND
Text Label 7600 5700 2    50   ~ 0
CAN_H
Text Label 7600 5800 2    50   ~ 0
CAN_L
Text Label 9350 3550 2    50   ~ 0
GND
Text Label 9350 3950 2    50   ~ 0
GND
Text Label 9350 4250 2    50   ~ 0
GND
Text Label 9350 5000 2    50   ~ 0
GND
Text Label 8800 5600 1    39   ~ 0
GND
Text Label 8900 5600 1    39   ~ 0
VCC
Text Label 9350 5200 2    50   ~ 0
VCC
Text Label 9350 4350 2    50   ~ 0
VCC
Text Label 9350 3750 2    50   ~ 0
VCC
Text Label 9350 3350 2    50   ~ 0
VCC
Text Label 8000 3150 3    50   ~ 0
VCC
Text Label 7400 2850 2    50   ~ 0
GND
Text Label 6100 3100 3    50   ~ 0
GND
Text Label 3150 3150 0    50   ~ 0
VCC
Text Label 3100 3850 0    50   ~ 0
VCC
Text Label 3100 4450 0    50   ~ 0
VCC
Text Label 3100 5150 0    50   ~ 0
VCC
Text Label 3100 5750 0    50   ~ 0
VCC
Text Label 8600 5600 1    39   ~ 0
RX
Text Label 8700 5600 1    39   ~ 0
TX
Wire Wire Line
	2650 3250 5400 3250
Wire Wire Line
	5400 3250 5400 3600
Wire Wire Line
	2650 6150 5650 6150
Wire Wire Line
	5650 6150 5650 5800
Wire Wire Line
	5650 5800 6100 5800
Wire Wire Line
	2650 3250 2650 6150
Wire Wire Line
	4150 5500 5550 5500
Wire Wire Line
	5550 5500 5550 5900
Wire Wire Line
	5550 5900 6100 5900
Wire Wire Line
	4100 5400 5950 5400
Wire Wire Line
	5950 5400 5950 6000
Wire Wire Line
	5950 6000 6100 6000
Text Label 6100 6000 2    50   ~ 0
VCC
Text Label 6100 5900 2    50   ~ 0
GND
Text Label 6100 5700 2    50   ~ 0
SO
Text Label 6100 5600 2    50   ~ 0
SI
Text Label 6100 5400 2    50   ~ 0
INT
Text Label 6100 5500 2    50   ~ 0
SCK
Wire Wire Line
	4600 5000 4600 5350
Wire Wire Line
	4600 5350 5850 5350
Wire Wire Line
	5850 5350 5850 5500
Wire Wire Line
	5850 5500 6100 5500
Wire Wire Line
	6100 5700 5600 5700
Wire Wire Line
	5600 5700 5600 5200
Wire Wire Line
	5600 5200 4500 5200
Wire Wire Line
	4500 5200 4500 5000
Wire Wire Line
	6100 5600 4400 5600
Wire Wire Line
	4400 5600 4400 5000
Text Label 9350 4450 2    50   ~ 0
X
Text Label 9350 4550 2    50   ~ 0
Y
Text Label 9350 4650 2    50   ~ 0
SW
Text Label 3100 4350 0    50   ~ 0
X
Text Label 3100 4250 0    50   ~ 0
Y
Text Label 3100 4150 0    50   ~ 0
SW
Text Label 6300 3100 3    50   ~ 0
CAN_H
Text Label 6400 3100 3    50   ~ 0
CAN_L
Wire Wire Line
	3500 4350 3500 3400
Wire Wire Line
	3100 5850 3500 5850
Wire Wire Line
	3500 5850 3500 6200
Wire Wire Line
	3500 6200 2500 6200
Wire Wire Line
	2500 6200 2500 2800
Wire Wire Line
	2500 2800 5300 2800
Wire Wire Line
	5300 2800 5300 3600
Wire Wire Line
	9350 5100 9100 5100
Wire Wire Line
	9100 5100 9100 6350
Wire Wire Line
	9100 6350 5400 6350
Wire Wire Line
	5400 6350 5400 5000
Wire Wire Line
	3100 3750 3750 3750
Wire Wire Line
	3750 3750 3750 2250
Wire Wire Line
	3750 2250 7150 2250
Wire Wire Line
	7150 2250 7150 3500
Wire Wire Line
	7150 3500 7900 3500
Wire Wire Line
	7900 3500 7900 3600
Text Label 3100 3750 0    50   ~ 0
A4
Text Label 3150 4350 0    50   ~ 0
A0
Text Label 3150 4250 0    50   ~ 0
A1
Text Label 9300 4450 2    50   ~ 0
A2
Text Label 9300 4550 2    50   ~ 0
A3
Text Label 3100 5850 0    50   ~ 0
D6
Wire Wire Line
	3100 5050 5700 5050
Wire Wire Line
	5700 5050 5700 5000
Text Label 3100 5050 0    50   ~ 0
D15
Text Label 9350 5100 2    50   ~ 0
D9
Text Label 6100 5800 2    50   ~ 0
D8
Wire Wire Line
	3150 3050 5850 3050
Wire Wire Line
	5850 3050 5850 3600
Wire Wire Line
	5850 3600 5900 3600
Text Label 3150 3050 0    50   ~ 0
D18
Text Label 9350 3450 2    50   ~ 0
D19
Wire Wire Line
	9350 3450 9150 3450
Wire Wire Line
	9150 3450 9150 2950
Wire Wire Line
	9150 2950 10400 2950
Wire Wire Line
	10400 2950 10400 6200
Wire Wire Line
	10400 6200 7200 6200
Wire Wire Line
	7200 6200 7200 5050
Wire Wire Line
	7200 5050 5900 5050
Wire Wire Line
	5900 5050 5900 5000
Wire Wire Line
	9350 3850 9000 3850
Wire Wire Line
	9000 3850 9000 3500
Wire Wire Line
	9000 3500 8000 3500
Wire Wire Line
	8000 3500 8000 3600
Text Label 9350 3850 2    50   ~ 0
A6
$EndSCHEMATC
