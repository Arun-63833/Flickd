import cv2
import os
from pathlib import Path

def extract_images(video_path=r"D:\Flickd\videos", output_path=r"D:\Flickd\extracted_image"):
    os.makedirs(output_path, exist_ok=True)

    for video_file in os.listdir(video_path):
        if video_file.endswith(".mp4"):
            video_file_path = os.path.join(video_path, video_file)
            video_name = Path(video_file).stem

            cap = cv2.VideoCapture(video_file_path)
            fps = cap.get(cv2.CAP_PROP_FPS)
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            duration = frame_count / fps

            # Dynamically adjust frame interval based on duration
            frame_interval = 5  # default
            if duration > 120:
                frame_interval = 8  # for videos longer than 2 minutes

            frame_number = 0
            saved_frame_count = 0

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                current_time = frame_number / fps

                if int(current_time) % frame_interval == 0:
                    filename = f"{video_name}_frame_{frame_number:04d}.jpg"
                    filepath = os.path.join(output_path, filename)
                    cv2.imwrite(filepath, frame)
                    saved_frame_count += 1

                frame_number += 1

            cap.release()
            print(f"Extracted {saved_frame_count} frames from {video_file} (duration: {duration:.1f}s, interval: {frame_interval}s)")

    print("All frames extracted and saved.")

extract_images()
