"""Image processing utilities"""

import cv2
import numpy as np
from typing import Tuple


def crop_region(image: np.ndarray, bbox: Tuple[int, int, int, int]) -> np.ndarray:
    """
    Crop a region from an image.

    Args:
        image: Input image
        bbox: Bounding box as (x1, y1, x2, y2)

    Returns:
        Cropped image region
    """
    x1, y1, x2, y2 = bbox
    x1 = max(0, x1)
    y1 = max(0, y1)
    x2 = min(image.shape[1], x2)
    y2 = min(image.shape[0], y2)
    return image[y1:y2, x1:x2]


def resize_image(image: np.ndarray, max_size: int) -> np.ndarray:
    """
    Resize image to max size while maintaining aspect ratio.

    Args:
        image: Input image
        max_size: Maximum dimension size

    Returns:
        Resized image
    """
    h, w = image.shape[:2]
    if max(h, w) <= max_size:
        return image

    scale = max_size / max(h, w)
    new_h = int(h * scale)
    new_w = int(w * scale)
    return cv2.resize(image, (new_w, new_h))


def enhance_contrast(image: np.ndarray, alpha: float = 1.5, beta: float = 30) -> np.ndarray:
    """
    Enhance image contrast.

    Args:
        image: Input image
        alpha: Contrast control
        beta: Brightness control

    Returns:
        Enhanced image
    """
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)


def denoise_image(image: np.ndarray) -> np.ndarray:
    """
    Denoise image using bilateral filter.

    Args:
        image: Input image

    Returns:
        Denoised image
    """
    return cv2.bilateralFilter(image, 9, 75, 75)
