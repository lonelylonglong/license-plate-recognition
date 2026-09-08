# Contributing to License Plate Recognition

Thank you for your interest in contributing to this project!

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion, please open an issue with:
- A clear, descriptive title
- A detailed description of the issue
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- Screenshots if applicable

### Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Add or update tests
5. Run tests locally: `pytest tests/ -v`
6. Commit with clear messages: `git commit -m 'Add feature: description'`
7. Push to your fork: `git push origin feature/your-feature`
8. Open a Pull Request

## Code Standards

- Follow PEP 8 style guidelines
- Write docstrings for all functions and classes
- Include type hints where possible
- Add unit tests for new features
- Keep functions focused and modular

## Testing

Before submitting a PR:
```bash
# Run tests
pytest tests/ -v

# Check code style
flake8 src/ tests/

# Format code
black src/ tests/
```

## Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/license-plate-recognition.git
cd license-plate-recognition

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install development dependencies
pip install -r requirements.txt
pip install -e .

# Run tests
pytest tests/
```

## Commit Message Guidelines

- Use clear, descriptive messages
- Start with a verb: "Add", "Fix", "Update", "Remove", etc.
- Reference issues when applicable: "Fixes #123"
- Keep first line under 50 characters
- Provide additional details in the body if needed

## Areas for Contribution

- Improve model architectures
- Add support for more license plate formats
- Optimize inference speed
- Enhance documentation
- Add more test coverage
- Improve error handling
- Add data augmentation techniques

## Questions?

Feel free to open an issue with the label "question" if you need clarification.

Thank you for contributing! 🙏
