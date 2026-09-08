"""License plate detection module using deep learning"""

import cv2
import numpy as np
from typing import List, Dict, Tuple, Optional
from src.config import DETECTION_MODEL_CONFIG, IMAGE_CONFIG
import logging

logger = logging.getLogger(__name__)


class LicensePlateDetector:
    """Detects license plates in images using YOLO"""

    def __init__(self, model_config: Optional[Dict] = None):
        """
        Initialize the license plate detector.

        Args:
            model_config: Configuration dictionary for the model
        """
        self.config = model_config or DETECTION_MODEL_CONFIG
        self.model = None
        self._load_model()

    def _load_model(self):
        """Load pre-trained YOLOv8 model"""
        try:
            from ultralytics import YOLO
            # Load YOLOv8 model
            logger.info(f"Loading {self.config['model_type']} model")
            # Uncomment when actual model is available
            # self.model = YOLO(f"yolov8{self.config['model_size']}.pt")
        except ImportError:
            logger.error("YOLOv8 not installed. Please install ultralytics.")

    def detect(self, image_path: str, return_image: bool = False) -> Union[List[Dict], Tuple[List[Dict], np.ndarray]]:
        """
        Detect license plates in an image.

        Args:
            image_path: Path to the input image
            return_image: Whether to return the annotated image

        Returns:
            List of detections with bbox, confidence, and optionally image
        """
        image = cv2.imread(image_path)
        if image is None:
            logger.error(f"Failed to read image: {image_path}")
            return [] if not return_image else ([], None)

        return self.detect_from_array(image, return_image)

    def detect_from_array(self, image: np.ndarray, return_image: bool = False) -> Union[List[Dict], Tuple[List[Dict], np.ndarray]]:
        """
        Detect license plates in an image array.

        Args:
            image: Input image as numpy array
            return_image: Whether to return the annotated image

        Returns:
            List of detections with bbox and confidence
        """
        if self.model is None:
            logger.error("Model not loaded")
            return [] if not return_image else ([], image.copy())

        # Run inference
        results = self.model(image, conf=self.config['confidence_threshold'])

        detections = []
        annotated_image = image.copy()

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                conf = box.conf[0].cpu().numpy()
                cls = int(box.cls[0])

                # Filter based on size constraints
                area = (x2 - x1) * (y2 - y1)
                if area < IMAGE_CONFIG['min_plate_area']:
                    continue

                detection = {
                    'bbox': [int(x1), int(y1), int(x2), int(y2)],
                    'confidence': float(conf),
                    'class': cls,
                }
                detections.append(detection)

                # Draw bounding box
                if return_image:
                    cv2.rectangle(annotated_image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(
                        annotated_image,
                        f"{conf:.2f}",
                        (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,
                        (0, 255, 0),
                        2,
                    )

        if return_image:
            return detections, annotated_image
        return detections

    def detect_batch(self, image_paths: List[str]) -> List[List[Dict]]:
        """
        Detect license plates in multiple images.

        Args:
            image_paths: List of paths to input images

        Returns:
            List of detection lists
        """
        results = []
        for image_path in image_paths:
            detections = self.detect(image_path)
            results.append(detections)
        return results
