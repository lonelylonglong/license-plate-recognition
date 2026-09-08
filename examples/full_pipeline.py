"""Example: Full end-to-end license plate recognition"""

import cv2
from src.pipeline import LicensePlateRecognizer


def main():
    """Run full recognition pipeline"""
    # Initialize recognizer
    recognizer = LicensePlateRecognizer()

    # Image path
    image_path = 'path/to/image.jpg'

    # Run full pipeline
    results, annotated_image = recognizer.recognize(image_path, return_visualization=True)

    # Print results
    print(f"\nFound {len(results)} license plate(s)\n")
    for i, result in enumerate(results):
        print(f"Plate {i + 1}:")
        print(f"  Text: {result['text']}")
        print(f"  OCR Confidence: {result['confidence']:.2f}")
        print(f"  Detection Confidence: {result['detection_confidence']:.2f}")
        print(f"  Bounding Box: {result['bbox']}")
        print()

    # Save annotated image
    cv2.imwrite('results.jpg', annotated_image)
    print("Annotated image saved as 'results.jpg'")


if __name__ == '__main__':
    main()
