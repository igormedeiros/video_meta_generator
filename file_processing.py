import os
import re
import shutil

from logger import log

def format_valid_file_name(text: object) -> object:
    # Remove caracteres especiais e espaços
    text = re.sub(r'[^\w\s]', '', text)
    # Substitui espaços por underscores
    text = text.replace(' ', '_')
    # Converte para minúsculas
    text = text.lower()
    return text


def save_video_copy(video_path, title):
    log.debug(f'save_video_copy({video_path}, {title})')
    """Saves a copy of the video with the determined title in the 'videos_processed' folder."""
    processed_folder = 'videos_processed'

    if os.path.exists(processed_folder):
        shutil.rmtree(processed_folder)
        os.makedirs(processed_folder)
    else:
        os.makedirs(processed_folder)

    cleaned_title = format_valid_file_name(title)
    new_video_filename = f"{cleaned_title}.mp4"
    new_video_path = os.path.join(processed_folder, new_video_filename)

    try:
        shutil.copy2(video_path, new_video_path)
    except OSError as e:
        print(f"Error copying file: {e}")
    return new_video_path
