import google_search
import music_player
import clock
import volume_shifter
import weather_fetcher
import keyword_filter
import threading
import noris_speak as ns
"""
def find_time_from_text(text):
    import conversion
    value = keyword_filter.find_numericals_in_text(text)
    units = keyword_filter.find_units_in_text(text)
    time = value[0]
    print(f'Thread is running, and has executed. Value->{value} Unit->{units}')
    if 'minute' in units:
        time = conversion.conversion_minute_to_second(value[0])
    elif 'hour' in units:
        time = conversion.conversion_hour_to_second(value[0])
    return time
"""
def keyword_to_program_linker(keyword_value:str, text:str) -> None:
    match keyword_value:
        
        case 'weather_fetcher.py':
            weather_fetcher.fetch_weather()


        case 'volume_shifter.py':
            volume_shifter.volume_shift(text)

        
        case 'timer.py':
            #Create a thread
            #Start the thread
            print('timer detected!')
            time = keyword_filter.find_seconds_in_text(text)
            thread = threading.Thread(target=clock.create_timer, args=(time,)) #Setting to 5 for testing
            thread.start()


        case 'music_player.py':
            music_player.play_music(text)


        case 'google_search.py':
            pass

#keyword_to_program_linker('timer.py', 'set a timer for 5 seconds')

"""
        case 'timer.py':
            ####### TO FIX -------------------------
            time = find_time_from_text(text)

            timer_thread = threading.Thread(target=clock.timer, args=(time,))
            timer_thread.start()


            print('thread started')
"""