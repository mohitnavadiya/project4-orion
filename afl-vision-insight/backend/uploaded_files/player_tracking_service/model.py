from typing import List, Dict

def run_dummy_inference(file_path: str) -> Dict:
    return {
        "status": "success",
        "message": f"Dummy inference on file {file_path}",
        "video_info": {
            "video_path": file_path,
            "frame_rate": "30",
            "resolution": "1280x720"
        },
        "tracking_results": [
            {
                "player_id": "player_1",
                "bbox": [100, 150, 50, 100],
                "center": [125, 200],
                "confidence": 0.95,
                "width": 50,
                "height": 100
            },
            {
                "player_id": "player_2",
                "bbox": [200, 180, 60, 120],
                "center": [230, 240],
                "confidence": 0.90,
                "width": 60,
                "height": 120
            }
        ]
    }
