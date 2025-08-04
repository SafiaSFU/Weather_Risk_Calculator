'''
DEVELOPER(S): Safia U.
COLLABORATOR(S): ----
'''

##########################################
# FUNCTIONS:
##########################################
#<replace this line with function definitions, each needs a description>

def main():

#Define the fuction to convert -if necessary- the input from Celsius to Fahrenheit (Metric to Imperial):
    def convert_temp_string(temp_string):
        temp_string = temp_string.strip().upper() #To delete the whitespaces and convert to uppercase
        if temp_string.endswith('C'):
    #convertion formula C to F. Float to change from string to a number [:-1] remove last character C ot F
            return (((float(temp_string[:-1])) * 9/5) + 32)
        if temp_string.endswith('F'):
            return (float(temp_string[:-1])) #return the string digit as a number 
        else:
            print("Invalid temperature format. Please enter '10C' or '10f' format")
            return None
        

    #Define the fuction to convert -if necessary- the input from Km to miles (Metric to Imperial):
    def convert_speed_string(speed_string):
        speed_string = speed_string.strip().lower()
        if speed_string.endswith('kmh'):
            return ((float(speed_string[:-3])) / 1.609) #the three last characters "kmh"
        if speed_string.endswith('mph'):
            return (float(speed_string[:-3])) #return the string digit as a number
        else:
            return None

    #Define the function to calculate wind chill temperature (Imperial system):
    def get_wind_chill(temp_f, wind_speed_mph):
        wind_chill =  35.74 + (0.6215 * temp_f) - 35.75 * (wind_speed_mph**0.16) + 0.4275 * temp_f * (wind_speed_mph**0.16)
        if temp_f > 50 or wind_speed_mph <= 3:
            return None #because wind chill doesn't apply in these conditions
        else:
            return wind_chill

    #Define the function to calculate index heat temperature (Imperial system):
    def get_heat_index(temp_f, humidity):
        heat_index = (-42.379 
        + 2.04901523 * temp_f 
        + 10.14333127 * humidity 
        - 0.22475541 * temp_f * humidity 
        - 6.83783 * 10**-3 * temp_f**2 
        - 5.481717 * 10**-2 * humidity**2 
        + 1.22874 * 10**-3 * temp_f**2 * humidity 
        + 8.5282 * 10**-4 * temp_f * humidity**2 
        - 1.99 * 10**-6 * temp_f**2 * humidity**2)
        if temp_f < 80 or humidity < 40: # # Heat index doesn't apply in these conditions
            return None
        else:
            return heat_index

    while True:
        temp_f = None
        while temp_f is None:
            input_temp= input("Enter temperature (e.g: '10F' or '10C'): ")
            temp_f = convert_temp_string(input_temp)

        wind_speed_mph = None
        while wind_speed_mph is None:
            input_windspeed = input("Enter wind speed (e.g: '10mph' or '10kmh'): ")
            wind_speed_mph = convert_speed_string(input_windspeed)
        
        humidity = None
        while humidity is None:
            humidity_input = input("Enter humidity (in percentage) number only: ")
            if humidity_input.isdigit():
                humidity = float(humidity_input)
            else:
                print("Invalid input. Please enter a digit only.")

                """I have tried to don't loop for temperature, speed wind and humidity by using continue BUT if you input one of the three parameters 
                in a wrong way, the loop starts from the beginning every time, I mean it asks for temperature again then speed wind then humidity...
                The first code that I have used was:"""
        #input_temp= input("Enter temperature (e.g: '10F' or '10C'): ")
        #temp_f = convert_temp_string(input_temp)
        #if temp_f is None:
            #continue

        #input_windspeed = input("Enter wind speed (e.g: '10mph' or '10kmh'): ")
        #wind_speed_mph = convert_speed_string(input_windspeed)
        #if wind_speed_mph is None: #Invalid input, try again
            #continue

        #humidity = input("Enter humidity (in percentage) number only!!: ")
        #if not humidity.isdigit():
            #print('Invalid input. Please enter a digit only.')
            #continue
        #humidity = float(humidity)

        wind_chill = get_wind_chill(temp_f, wind_speed_mph)
        heat_index = get_heat_index(temp_f, humidity)
        
        #select the relevant index based on the inputs:
        if wind_chill is not None: #When wind chill applies
            print("#"*15, "WATCH OUT! RISK!", "#"*15)
            print(f"Temp= {temp_f:.0f}°F, Wind chill = {wind_chill:.0f}°F")
            print(f'''Cold stress, feels like {wind_chill:.0f}°F. Stay covered and warm.
Minimize your exposure to the outdoors if possible!''')
            print("#"*50)
        elif heat_index is not None: #When heat index apply
            print("#"*15, "WATCH OUT! RISK!", "#"*15)
            print(f"Temp= {temp_f:.0f}°F, heat_index = {heat_index:.0f}°F")
            print(f'''Heat risk!! Hot and humid, feels like {heat_index:.0f}°F. Stay hydrated.
Minimize your exposure to the outdoors if possible!''')
            print("#"*50)

        elif temp_f < 30 : #when is extremely cold but wind chill doesn't apply bc of low wind speed
            print("#"*15, "WATCH OUT! RISK!", "#"*15)
            print(f"Temp= {temp_f:.0f}°F, Wind speed= {wind_speed_mph:.0f}mph, Humidity={humidity:.0f}%")
            print("Freezing! Beware of frostbite and hypothermia.")
            print("#"*50)

        elif temp_f >= 80 and humidity < 40: #when is hot but heat index doesn't apply bc of low humidity
            print("#"*15, "WATCH OUT! RISK!", "#"*15)
            print(f"Temp= {temp_f:.0f}°F, Wind speed= {wind_speed_mph:.0f}mph, Humidity={humidity:.0f}%")
            print("Very hot and dry! Risk of dehydration. Please stay hydrated!")
            print("#"*50)
        
        else:
            print("#"*20, "RESULT", "#"*20)
            print(f"Temp= {temp_f:.0f}°F, Wind speed= {wind_speed_mph:.0f}mph, Humidity={humidity:.0f}%")
            print("Comfortable weather. No risk, enjoy your time! ")
            print("#"*50)

        again = input("\nDo you want to try again? (yes/no): ").strip().lower()
        if again != 'yes':
            break

##########################################
# MAIN PROGRAM:
##########################################
#<replace this line with your main program>
main()
