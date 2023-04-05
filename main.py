import sys
import keyConfig
import ask_openAI
from colorama import Fore, Back, Style


api_key = keyConfig.get_key()


if len(sys.argv) > 1:
    arg1 = sys.argv[1]
    if arg1 == 'changekey':
        if len(sys.argv) == 3:
            keyConfig.change_key(sys.argv[2])
        else:
            print("command error: changekey <your new key>")
    else:
        input_message = ask_openAI.get_message(sys.argv)
        ask_openAI.start_conversation(input_message,api_key)

else:
    print(Fore.YELLOW + 'Welcome to use terminalGPT, please enter help to see how to use it'+ Style.RESET_ALL)
    input_message = input("Enter you question：")

#print()


