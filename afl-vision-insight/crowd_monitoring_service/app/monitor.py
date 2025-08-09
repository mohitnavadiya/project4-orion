# app/monitor.py

import random
from PIL import Image, ImageDraw
import os

class CrowdMonitor:
    def __init__(self):
        self.stages = ["Stage A", "Stage B", "Stage C"]
        self.max_allowed_resolution = (1920, 1080)  # HD resolution limit (width x height)

    def process_image(self, image_path: str, output_path: str):
        try:
            # Load image and validate format
            image = Image.open(image_path).convert("RGBA")

            # Check resolution to prevent memory issues
            if image.size[0] > self.max_allowed_resolution[0] or image.size[1] > self.max_allowed_resolution[1]:
                raise ValueError("Image resolution too high. Please use HD (1920x1080) or lower.")

            # Simulate heatmap overlay
            overlay = Image.new("RGBA", image.size, (255, 0, 0, 50))  # semi-transparent red
            result = Image.alpha_composite(image, overlay)
            result.save(output_path)

            # Simulate stage-wise crowd count
            crowd_data = {stage: random.randint(300, 800) for stage in self.stages}
            return {
                "status": "success",
                "message": "Crowd data generated successfully",
                "crowd_estimates": crowd_data
            }

        except ValueError as ve:
            return {
                "status": "error",
                "message": str(ve),
                "code": 413  # Payload Too Large (image resolution too high)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": "Failed to process image. Please check the format or content.",
                "code": 400
            }
