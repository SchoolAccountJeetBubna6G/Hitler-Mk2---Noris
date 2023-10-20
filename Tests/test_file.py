text = input('YOU:: ')

control_words = {'pause':[' pause','stop'], 'resume':['start',' unpause']}
print(control_words['pause'])
for control_word in control_words:
    for word in control_words[control_word]:
        if word in text:
            print(control_word)