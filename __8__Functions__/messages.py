# 8.9
# messages
messages = ['Hello Bro', 'Whats up ?', 'Good Evening Bhai', 'Welcome to India', 'Incredible India']
messages_copy = messages[:]

def show_messages(list):
    for message in list:
        print(message)
    pass


# 8.10
# sent messages


def send_messages(list):
    sent_messages = []
    while len(list) != 0:
        for message in list:
            # print(message)
            sent_messages.append(message)
            list.remove(message)
    print(list)
    print(sent_messages)
    pass


show_messages(messages)
send_messages(messages)

# 8.10
# archived messages
show_messages(messages_copy)
