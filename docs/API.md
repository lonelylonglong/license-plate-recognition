# API Documentation

## Core Classes

### LicensePlateRecognizer

End-to-end license plate recognition system.

#### Methods

```python
recognize(image_path: str, return_visualization: bool = False) -> List[Dict]
```

Recognize license plates in an image.

**Parameters:**
- `image_path` (str): Path to the input image
- `return_visualization` (bool): Whether to return annotated image

**Returns:**
- List of dictionaries with keys:
  - `text`: Recognized license plate text
  - `confidence`: OCR confidence score (0-1)
  - `bbox`: Bounding box [x1, y1, x2, y2]
  - `detection_confidence`: Detection confidence score (0-1)

**Example:**
```python
from src.pipeline import LicensePlateRecognizer

recognizer = LicensePlateRecognizer()
results = recognizer.recognize('image.jpg')
for plate in results:
    print(f"Text: {plate['text']}, Confidence: {plate['confidence']}")
```

---

### LicensePlateDetector

Detects license plates in images.

#### Methods

```python
detect(image_path: str, return_image: bool = False) -> List[Dict]
```

Detect license plates in an image.

**Parameters:**
- `image_path` (str): Path to the input image
- `return_image` (bool): Whether to return annotated image

**Returns:**
- List of detections with keys:
  - `bbox`: [x1, y1, x2, y2]
  - `confidence`: Detection confidence score
  - `class`: Object class

---

### CharacterRecognizer

Recognizes characters in license plates.

#### Methods

```python
recognize(plate_image: np.ndarray) -> Tuple[str, float]
```

Recognize text in a license plate image.

**Parameters:**
- `plate_image` (np.ndarray): Cropped plate image

**Returns:**
- Tuple of (recognized_text, confidence_score)

---

## Configuration

See `src/config.py` for configuration options.

### Detection Configuration
```python
DETECTION_MODEL_CONFIG = {
    'model_type': 'yolov8',
    'model_size': 'medium',
    'confidence_threshold': 0.5,
    'iou_threshold': 0.45,
}
```

### Recognition Configuration
```python
RECOGNITION_MODEL_CONFIG = {
    'model_type': 'crnn',
    'input_height': 32,
    'input_width': 100,
    'confidence_threshold': 0.5,
}
```
