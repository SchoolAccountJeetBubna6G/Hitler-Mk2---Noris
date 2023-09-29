def theKeyWordFilterBug(sentence):
    import json
    with open('keywords.json') as file:
        global keywords
        keywords = json.load(file)
        print(keywords['keywords'])
    
    for item in keywords['keywords'][0]:
        if item in sentence:
            print('True, works ig')

def theKeywordReturnBug():
    import json
    with open('keywords.json') as file:
        global keywords
        keywords = json.load(file)
        #print(keywords['keywords'])
    
    item_counter = 0
    for item in keywords['keywords'][0]:
        print(keywords['keywords'][0][item])
        item_counter += 1

def theThreadingTimerClockBug():
    import threading
    import time
    import test_file


    thread = threading.Thread(target=test_file.timer, args=(5,))
    thread.start()

    control_variable = 0
    while control_variable <= 100:
        print(control_variable)
        control_variable += 1
        time.sleep(1)
    
theThreadingTimerClockBug()