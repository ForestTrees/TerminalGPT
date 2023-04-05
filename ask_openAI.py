import openai
from openai import error
from colorama import Fore, Back, Style

message = []

def get_message(args):
    del args[0]
    input_message = ' '.join(args)

    return input_message

def ask_openAI(message,api_key):
    openai.api_key = api_key

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = message
            # messages=[
            #     {"role": "user", "content": message}
            # ]
        )

        answer = Fore.GREEN  + completion.choices[0].message["content"].strip() + Style.RESET_ALL

        return ('success',answer)

    except error.AuthenticationError:
        error_message = Fore.YELLOW + "Incorrect API key provided. You can find your API key at https://platform.openai.com/account/api-keys.\n" \
                        "Change your API key by using command: changekey <your new key>" + Style.RESET_ALL
        return ('key-err',error_message)
    except Exception as err:
        error_message = Fore.YELLOW + "Server error, please try again later" + Style.RESET_ALL
        return ('server-err', error_message)

def start_conversation(startMessage,api_key):
    global message

    input_message = startMessage
    while input_message != 'exit':
        message.append({"role": "user", "content": input_message})
        anwser = ask_openAI(message, api_key)

        if anwser[0] != 'success':
            message = message[:-1]
        else:
            message.append({"role": "assistant", "content": anwser[1]})

        print(anwser[1])
        # print(message)

        input_message = input("")