import os
import cv2
import numpy as np
from vidaug import augmentors as va
from moviepy.editor import ImageSequenceClip

# Define augmentations
augmentations = {
    "darken": va.Multiply(0.5),          # Darkening effect
    "lighten": va.Multiply(1.5),         # Lightening effect
}

def load_video_frames(video_path):
    """Load frames from a video file."""
    cap = cv2.VideoCapture(video_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    cap.release()
    return frames

def save_video(frames, output_path, fps):
    """Save frames as a video file."""
    clip = ImageSequenceClip(frames, fps=fps)
    clip.write_videofile(output_path, codec="libx264", audio=False)

def augment_and_save_videos(input_folder):
    # Create output folder if it doesn't exist
    output_folder = os.path.join(input_folder, "output")
    os.makedirs(output_folder, exist_ok=True)

    # Get all video files in the input folder
    video_files = [f for f in os.listdir(input_folder) if f.endswith(('.mp4', '.avi', '.mov'))]
    
    for video_file in video_files:
        # Load base video
        video_path = os.path.join(input_folder, video_file)
        base_frames = load_video_frames(video_path)

        # Get video fps
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        cap.release()

        # Save original video as base copy with '_base' suffix
        base_output_path = os.path.join(output_folder, f"{os.path.splitext(video_file)[0]}_base.mp4")
        save_video(base_frames, base_output_path, fps)

        # Apply each augmentation and save as a new video file
        for aug_name, augmenter in augmentations.items():
            # Apply the augmentation
            augmented_frames = augmenter(base_frames)
            # Set the output path with augmentation-specific suffix
            output_path = os.path.join(output_folder, f"{os.path.splitext(video_file)[0]}_{aug_name}.mp4")
            # Save the augmented video
            save_video(augmented_frames, output_path, fps)

# Specify the folder containing videos
input_folder = "./videos"
augment_and_save_videos(input_folder)