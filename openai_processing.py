import json

import openai

from logger import log

# Load configurations from the provided config file
with open("config/config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)
    openai_json = config["openai"]
    hashtags_default_json = config["hashtags"]

openai.api_key = openai_json["api_key"]


def generate_video_metadata(transcript):
    """Generate Video title, description, and hashtags using the OpenAI API."""
    log.debug(f'generate_video_metadata({transcript})')
    prompt_text = f'{openai_json["prompt"]}{transcript}'
    response = openai.Completion.create(
        engine=openai_json["engine"],
        prompt=prompt_text,
        max_tokens=openai_json["max_tokens"]
    )
    output = response.choices[0].text.strip().split('\n')

    log.debug(f'output: {output}')

    title = next(line.replace("Title: ", "").strip()
                 for line in output if "Title:" in line)
    log.debug(f'title: {title}')

    description = next(line.replace("Description: ", "").strip()
                       for line in output if "Description:" in line)
    log.debug(f'description: {description}')

    hashtags = next(line.replace("Hashtags: ", "").strip()
                    for line in output if "Hashtags:" in line)

    for hashtag_default in hashtags_default_json:
        hashtags = f'{hashtags} {hashtag_default}'
    log.debug(f'hashtags: {hashtags}')

    return title, description, hashtags
