# 10.1

# importing
import time

py_learn = open('learning_python.txt')
with py_learn as py_txt:
    learnings = py_txt.readlines()
    learned = []
    learned_string = ""
    for learn in learnings:
        learned.append(learn.rstrip())
        learned_string += " "+learn.strip()
    print(learned)
    print(learned_string)
print('Things learned till now :-')
for learn in learned:
    time.sleep(0.8)
    print(learn)

# 10.2
learned_string = learned_string.replace('types', "")
print(learned_string)
learned_string = learned_string.replace('Python', "C")
print(learned_string)
