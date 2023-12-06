pt_1 = 357424.851

pt_2 = 357821.8043

pt_3 = 572152.965

pt_4 = 570493.6584

#import the math module
import math
#calculate the square root of decimal numbers
print("The square root of (((pt_1 - pt_2)**2)+((pt_3 - pt_4)**2)) is",math.sqrt(((pt_1 - pt_2)**2)+((pt_3 - pt_4)**2))/1000)
print("The square root of (((pt_1 - pt_2)**2)+((pt_3 - pt_4)**2)) is",math.sqrt(((pt_1 - pt_2)**2)+((pt_3 - pt_4)**2))/100*(0.4))
print("The square root of (((pt_1 - pt_2)**2)+((pt_3 - pt_4)**2)) is",math.sqrt(((pt_1 - pt_2)**2)+((pt_3 - pt_4)**2))/100*(0.4)*(4))
DISTANCE = ("The square root of (((pt_1 - pt_2)**2)+((pt_3 - pt_4)**2)) is",math.sqrt(((pt_1 - pt_2)**2)+((pt_3 - pt_4)**2))/1000)
MIN_OF_DRIVE = ("The square root of (((pt_1 - pt_2)**2)+((pt_3 - pt_4)**2)) is",math.sqrt(((pt_1 - pt_2)**2)+((pt_3 - pt_4)**2))/100*(0.4))
MIN_OF_TREK = ("The square root of (((pt_1 - pt_2)**2)+((pt_3 - pt_4)**2)) is",math.sqrt(((pt_1 - pt_2)**2)+((pt_3 - pt_4)**2))/100*(0.4)*(4))
TIME_ANALYSIS = (DISTANCE, MIN_OF_DRIVE, MIN_OF_TREK)
print(TIME_ANALYSIS)
DISTANCE_FROM = ("The square root of (((pt_1 - pt_2)**2)+((pt_3 - pt_4)**2)) is",math.sqrt(((pt_1 - pt_2)**2)+((pt_3 - pt_4)**2))/1000*2)
MIN_OF_DRIVE_FROM = ("The square root of (((pt_1 - pt_2)**2)+((pt_3 - pt_4)**2)) is",math.sqrt(((pt_1 - pt_2)**2)+((pt_3 - pt_4)**2))/100*(0.4)*2)
MIN_OF_TREK_FROM = ("The square root of (((pt_1 - pt_2)**2)+((pt_3 - pt_4)**2)) is",math.sqrt(((pt_1 - pt_2)**2)+((pt_3 - pt_4)**2))/100*(0.4)*(4)*2)
TO_AND_FRO = (DISTANCE_FROM, MIN_OF_DRIVE_FROM, MIN_OF_TREK_FROM)
print(TO_AND_FRO)
