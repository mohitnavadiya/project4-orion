# app/tracker.py

import random
import time

class PlayerTracker:
    def __init__(self):
        pass

    def process_video(self, video_path: str):
        time.sleep(1)  # Simulate processing delay

        video_info = {
            "duration": 10.5,
            "fps": 30,
            "total_frames": 315,
            "resolution": [1920, 1080]
        }

        tracking_results = []
        for frame_number in range(1, 6):  # Simulate 5 frames
            players = []
            for pid in range(1, random.randint(2, 4)):
                x1 = random.randint(100, 500)
                y1 = random.randint(100, 500)
                width = 100
                height = 333
                x2 = x1 + width
                y2 = y1 + height
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2
                players.append({
                    "player_id": pid,
                    "bbox": {
                        "x1": x1,
                        "y1": y1,
                        "x2": x2,
                        "y2": y2
                    },
                    "center": {
                        "x": center_x,
                        "y": center_y
                    },
                    "confidence": round(random.uniform(0.85, 0.95), 2),
                    "width": width,
                    "height": height
                })

            tracking_results.append({
                "frame_number": frame_number,
                "timestamp": round(frame_number * (1 / 30), 3),
                "players": players
            })

        return {
            "video_info": video_info,
            "tracking_results": tracking_results
        }