# TerminalGPT
TerminalGPT is a project that allows you to use chatgpt in the terminal

## How to use

> Please make sure that `python3` has been installed and added to the system environment variables before you use this project.

1. Clone the repo and enter the directory

   ```bash
   git clone https://github.com/ForestTrees/terminalGPT.git
   ```

2. Install the necessary third-party packages:

   ```bash
   pip install openai
   pip install colorama
   ```

3. Create a file named `config.ini` and write the following information:

   ```ini
   [Section1]
   key = <Your openAI key>
   language = en
   ```

   You can find your API key at https://platform.openai.com/account/api-keys.

   `language` Currently supports English (en)

4. Run the project with `python`

   ```bash
   python main.py
   ```

## Shortcut to run (Windows)

1. Add the folder path of this project to the system environment variable Path

2. Modify `showme.bat` to your own path

   ```bat
   @echo off
   python.exe <Your Path>\main.py
   ```

3. Enter directly in the terminal: `showme` to run. 

   You can also modify `showme.bat` to any name (do not change the `.bat` suffix), and then enter this name in the terminal to run the program

## License

This project is licensed under the [MIT License](https://github.com/ForestTrees/terminalGPT/blob/main/LICENSE).
