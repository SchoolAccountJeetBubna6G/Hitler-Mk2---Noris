import json
#------------------------------------

import speech
from keyword_filter import keyword_in_text, assistant_name_in_text, __init__
import keyword_to_program
import threading
import clock
#!--------------------------------------------------------------------------------------------------------------------------

PATH_TO_MODEL = r'C:\Users\Jeet\Desktop\Projects\PythonProjects\SpeechRecognition\Hitler Mk2 - Noris\vosk-model-en-in-0.5'
ASSISTANT_NAME = ['hitler','littler','peddler','riddler', 'butler', 'nadler', 'headley', 'edler', "he'd learn", "atla"]     #The names that can be misinterprited by the model.
TEST_VALUE = 'hitler set a timer for 5 seconds'

speech.__init__(PATH_TO_MODEL, method='google')
__init__() #Initializes keyword filter

def main():
    #text = speech.generate_text_vosk()
    text = speech.generate_text_google()
    #text = TEST_VALUE
    if type(text) is str:
        text = text.lower()
        print(text, assistant_name_in_text(ASSISTANT_NAME, text))#Debug
        if assistant_name_in_text(ASSISTANT_NAME, text):
            keyword_data = keyword_in_text(text)
            print(keyword_data)
            if keyword_data['keyword_present']:
                #if keyword_data['keyword_value'] == 'clock.py': thread = threading.Thread(target=clock.timer, args=(5,)); thread.start()
                keyword_to_program.keyword_to_program_linker(keyword_value=keyword_data['keyword_value'], text=text)

reccursion_limit_for_testing = 100
while True:
    if reccursion_limit_for_testing > 1:
        main()
    reccursion_limit_for_testing -= 1

#main()






















"""

def create_timer(text):
    import clock

    def find_time_from_text(text):
        import conversion
        import keyword_filter

        value = keyword_filter.find_numericals_in_text(text)
        units = keyword_filter.find_units_in_text(text)

        time = value[0]


        print(f'Thread is running, and has executed. Value->{value} Unit->{units}')


        if 'minute' in units:
            time = conversion.conversion_minute_to_second(value[0])

        elif 'hour' in units:
            time = conversion.conversion_hour_to_second(value[0])

        return time
    
    time = find_time_from_text(text)

    timer_thread = threading.Thread(target=clock.timer, args=(5,))
    timer_thread.start()

    print('thread started')

"""