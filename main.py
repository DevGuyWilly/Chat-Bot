# Import modules
import openai
from tkinter import *

# creating GUI for the chatBot
window = Tk()
window.title('chatBot')
window.geometry('800x600')
window['background'] = 'white'

mystring = StringVar(window)


def send():
    # API KEY
    openai.api_key = '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'
    messages = [
        {"role": "system",
         #  behaviour of the system set to kind helpful assistance
         #  the assistance role is used to store prior responses as well
         "content": "You are a kind helpful assistant"},
    ]
    # model_engine = 'text-davinci-003'
    model_engine = 'gpt-3.5-turbo'

    # Insert text widget value into your message variable
    message = str(mystring.get())
    Usersend = "    User👨: " + message
    text.insert(END, "\n" + Usersend)

    if message:
        messages.append(
            {"role": "user", "content": message}
        )
        # taking our
        chat = openai.ChatCompletion.create(
            model=model_engine, messages=messages
        )
        # An object response from the AI specifying to 'message.content'
        reply = chat.choices[0].message.content
        BotSend = "    WillyDee's-ChatBot🤖: " + reply
        text.insert(END, "\n" + BotSend)
        #  the assistance role is used to store prior responses as well
        messages.append({"role": "assistant", "conent": reply})


def swap():
    label.pack_forget()
    button.pack_forget()
    labelTwo.pack(padx=10, pady=10)
    text.pack(padx=10, pady=20)
    entry.pack(padx=20, pady=20)
    sendButton.pack()


label = Label(window, text="Welcome to WillyDee's chat-Bot🤖",
              font=('Arial', 18), padx=20, pady=20, bg='black')

label.pack(expand=True)

button = Button(window, text="Start Conversation",
                padx=20, pady=20, bg='black', highlightthickness=0, command=lambda: swap())

button.pack(padx=20, pady=20)

#
labelTwo = Label(window, bg='black',
                 text='Ask Me Anything!😁', padx=20, pady=20, font=('Arial', 18))

text = Text(window, bg='black', width=700,
            highlightthickness=0)

entry = Entry(window, bg='black',
              font=('Arial', 18), width=50, highlightthickness=0, textvariable=mystring)

sendButton = Button(window, text='SEND', font=(
    'Arial', 16), bg='black', command=lambda: send(), highlightthickness=0, padx=20, pady=20)


window.mainloop()
