import openai
from openai import error
from colorama import Fore, Back, Style
from rich.markdown import Markdown
from rich.console import Console
import sys

def ask_openAI(message,api_key):
    openai.api_key = api_key

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = message,
            stream=True
            # messages=[
            #     {"role": "user", "content": message}
            # ]
        )

        print(Fore.YELLOW)
        for line in completion:
            chunk = line['choices'][0].get('delta', {}).get('content', '')
            if chunk:
                print(chunk, end="")
        print(Style.RESET_ALL)
        # answer = Fore.YELLOW + completion.choices[0].message["content"].strip() + Style.RESET_ALL
        # return ('success',answer)

    except error.AuthenticationError:
        error_message = Fore.YELLOW + "Incorrect API key provided. You can find your API key at https://platform.openai.com/account/api-keys.\n" \
                        "Change your API key by using command: /changekey <your new key>" + Style.RESET_ALL
        print(error_message)
        return ('key-err',error_message)
    # except Exception as err:
    #     error_message = Fore.YELLOW + "Server error, please try again later" + Style.RESET_ALL
    #     return ('server-err', error_message)

