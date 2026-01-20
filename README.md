# Handwriting Digit Recognition

A Python-based CNN system for recognizing handwritten digits using deep learning.

## Motivation

I build this project to learn about Neural Network specifically Convolutional Neural Network (CNN). 
Each person's handwriting is very different so we couldn't make a program to simply recognize the handwriting just by the pixel, so we need something that could learn. 
CNN is known for its advantages in "learning" from images so i choose to use it.
I train the CNN with MNIST Dataset and achieves an accuracy over 98% in its validation dataset.

## Project Sturcture

app/
model/
.gitignore
requirements.txt
README.md

## Installation

### Clone this repository:
git clone https://github.com/StanleyT14/Handwriting-Digit-Recognition
cd Handwriting-Digit-Recognition

### Create and install virtual environment:

### python -m venv hrr
hrr\Scripts\activate

pip install -r requirements.txt

### Run interface:
python app/app.py

## Usage

To run the program, make sure there is a trashcan image inside the same folder with the app.py. 
After you run the app.py, a canvas will show up and you can use your pointer to write a digit on the canvas.
To predict, press the "predict" button at the bottom left and a messagebox will show up with its prediction.
To clear the canvas, press the trashcan icon button.
To exit, press "q" on your keyboard (Do not press the "X" button or the canvas will stop working).

## Requirements 

Python 3.10
Tensorflow
Numpy
OpenCv
Matplotlib

## Limitation

Users can still press the fullscreen button and also the "X" button which would make the canvas stops working.
Model can not predict correctly an "ugly" handwriting and when the digit is on the edge of the canvas.

## License

This project is not licensed. All rights reserved.
