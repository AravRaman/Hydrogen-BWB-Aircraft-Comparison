#name = 'Carol'
#age = 3000
#if name == 'Alice':
    #print('Hi, Alice.')
#elif age < 12:
    #print('You are not Alice, kiddo.')
#else:
    #print('You are neither Alice nor a little kid.')

#today_is_opposite_day = False

# Set say_it_is_opposite_day base don today_is_opposite_day:
#if today_is_opposite_day == True:
    #say_it_is_opposite_day = True
#else:
   #say_it_is_opposite_day = False

# If it is opposite day, toggle say_it_is_opposite_day:
#if today_is_opposite_day == True:
    #say_it_is_opposite_day = not say_it_is_opposite_day
# Say what day it is:
#if say_it_is_opposite_day == True:
   # print('Today is Opposite Day.')
#else:
    #print('Today is not Opposite Day.')

print('Enter TB or GB for the advertised unit:')
unit = input('>')

#Calc amount advertised capacity lies.
if unit == 'TB' or unit == 'tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
    discrepancy = 1000000000 / 1073741824

print('Enter the advertised capacity:')
advertised_capacity = input('>')
advertised_capacity = float(advertised_capacity)

# Calc real capacity, round to nearest hundredth, and convert it to a string
real_capacity = str(round(advertised_capacity * discrepancy, 2))

print('The actual capacity is ' + real_capacity + ' ' + unit)
    