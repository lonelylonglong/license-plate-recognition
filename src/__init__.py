"""License Plate Recognition System"""

__version__ = '0.1.0'
__author__ = 'lonelylonglong'

from src.pipeline import LicensePlateRecognizer
from src.detector import LicensePlateDetector
from src.recognizer import CharacterRecognizer

__all__ = [
    'LicensePlateRecognizer',
    'LicensePlateDetector',
    'CharacterRecognizer',
]
