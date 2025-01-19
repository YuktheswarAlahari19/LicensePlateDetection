# License Plate Detection Project

## Overview
This project helps detect and read license plates from images using:

    YOLO (You Only Look Once): For finding license plates in images
    OCR (Optical Character Recognition): For reading text from detected plates

Key Files Explained
Main File

    DetectionWorks.ipynb: Contains all the code that runs the project
        Loads images
        Detects license plates
        Reads plate numbers
        Shows results

Support Files (Created to Fix Issues)

    model_loader.py:
        Loads the YOLO model
        Sets up OCR reader
        Fixed issue: "No module named 'model_loader'"
    image_processor.py:
        Processes images to detect plates
        Draws boxes around plates
        Shows text on images
        Fixed issue: Multiple detection boxes problem
    file_ops.py:
        Handles reading/saving files
        Creates output folders
        Fixed issue: File organization problems
    dataset.yaml:
        Contains settings for training
        Defines data paths


## Files Structure
- DetectionWorks.ipynb: Main implementation notebook
- model_loader.py: YOLO model and OCR initialization
- image_processor.py: Image processing and plate detection
- file_ops.py: File handling operations
- dataset.yaml: Dataset configuration

## Setup Instructions
1. Create virtual environment: `python -m venv detect`
2. Activate environment: `detect\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run DetectionWorks.ipynb

## Requirements
- Python 3.11.8
- Required packages listed in requirements.txt
