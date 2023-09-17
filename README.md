
# YouTube Metadata Generator

This script uses the OpenAI API to generate metadata for YouTube videos based on a provided video transcript. It outputs a title, a description, and hashtags.

## Features:

- Uses OpenAI's GPT model to generate YouTube metadata.
- Outputs the generated metadata in the console.
- Saves the metadata to an XLSX file for easy reference.

## How to Use:

1. Make sure you have the required libraries installed. They can be installed using the `requirements.txt` file.
2. Set up the `config.json` file with your OpenAI API key and desired configuration.
3. Create a virtual env `python -m venv venv`
4. Install requirements.txt `pip install -r requirements.txt`
5. Run the script using the command: `python main.py [input_folder] [output.xlsx] [language]`

## Note:

Ensure that the provided `config.json` is set up correctly. The OpenAI API key is mandatory.