import markdown

import keyConfig
import ask_openAI
from colorama import Fore, Back, Style
from rich.markdown import Markdown
from rich.console import Console

print(Fore.YELLOW + 'Welcome to use terminalGPT, please enter help to see how to use it'+ Style.RESET_ALL)

api_key = keyConfig.get_key()
message = []
commands = ['changekey','help']
input_message = input("")

while input_message != 'exit':

    if input_message.startswith('/changekey'):
        args = input_message.split()
        if len(args) != 2:
            print("Incorrect command :/changekey <Your new key>")
        else:
            keyConfig.change_key(args[1])
            api_key = args[1]
    elif input_message == '/help':
        print("help message")
    else:
        message.append({"role": "user", "content": input_message})
        anwser = ask_openAI.ask_openAI(message, api_key)
        anwser_status = anwser[0]
        anwser_text = anwser[1]

        if anwser_status != 'success':
            message = message[:-1]
            print(anwser_text)
        else:
            message.append({"role": "assistant", "content": anwser[1]})
            console = Console()
            anwser_text = Markdown(anwser_text)

            console.print(anwser_text)

    input_message = input("")



