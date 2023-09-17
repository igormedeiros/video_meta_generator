import os
import sys

from tqdm import tqdm

from video_processing import process_videos

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(
            "Usage: python main.py [input_folder] [output.xlsx] [language]")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_file = sys.argv[2]
    language = sys.argv[3]

    if not os.path.exists(input_folder):
        print(f"Input folder {input_folder} does not exist.")
        sys.exit(1)

    video_files = [f for f in os.listdir(input_folder) if f.endswith(".mp4")]

    if not video_files:
        print(f"No video files found in {input_folder}.")
        sys.exit(1)

    progress_bar = tqdm(total=len(video_files))

    for video_file in video_files:
        process_videos(input_folder, output_file,
                       video_file, language, progress_bar)

    progress_bar.close()
    print(f"Data saved to {output_file}")