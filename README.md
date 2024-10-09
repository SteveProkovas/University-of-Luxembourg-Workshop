# University of Luxembourg Workshop

This repository contains a simple Python implementation of a linear regression model that predicts exam scores based on study hours. The project is part of the *University of Luxembourg Workshop* (October 12th, 2024) and is published here for anyone interested in revisiting the material discussed during the workshop.

## Table of Contents
- [Overview](#overview)
- [Model Explanation](#model-explanation)
- [Code Overview](#code-overview)
- [Running the Code](#running-the-code)
- [Workshop Slides](#workshop-slides)
- [License](#license)

## Overview
This project demonstrates how to use a basic linear regression model to predict exam scores from the number of hours studied. The training data consists of three student records, with each entry representing the hours studied and the corresponding exam score.

This example was covered in the *University of Luxembourg Workshop*, and this repository provides an opportunity to revisit and understand the concepts of machine learning, specifically linear regression.

## Model Explanation
The model aims to learn a relationship between the number of hours studied (input) and the exam score (output). It adjusts its parameter \( w \) to minimize the error between predicted and actual scores using a simple gradient descent algorithm.

### Training Data
- **Student A**: Studied 1 hour, scored 50 points.
- **Student B**: Studied 3 hours, scored 65 points.
- **Student C**: Studied 5 hours, scored 80 points.

The model finds the best parameter \( w \) to make accurate predictions based on this data.

### Learning Process
- **Initial guess for \( w \)**: Starts at 10.0.
- **Learning rate**: 0.01
- **Stopping criterion**: Converges when the change in \( w \) is smaller than the tolerance of 1e-6.

The model iterates over the data, adjusts \( w \) to minimize the prediction error, and stops when convergence is reached.

## Code Overview
Here’s a simplified explanation of the code:
1. **Initialize Parameters**: Set an initial guess for \( w \) and define the learning rate, number of epochs, and tolerance for convergence.
2. **Training Loop**: For each epoch, the model:
    - Predicts exam scores.
    - Computes errors based on actual scores.
    - Updates \( w \) using gradient descent.
    - Checks for convergence.
3. **Final Output**: Prints the learned value of \( w \) and the final predictions.

```python
# Sample Code Snippet
data = [(1, 50), (3, 65), (5, 80)]  # Training data
w = 10.0  # Initial guess for parameter
learning_rate = 0.01  # Learning rate
# Model training logic...
```

## Running the Code
To run this project, clone the repository and execute the Python script.

```bash
git clone https://github.com/SteveProkovas/University-of-Luxembourg-Workshop.git
cd University-of-Luxembourg-Workshop
python predict_exam_scores.py
```

### Requirements
- Python 3.x
- No external libraries are required for this implementation.

## Workshop Slides
You can view the slides from the *University of Luxembourg Workshop* [here](https://docs.google.com/presentation/d/1Urk_tFU8MavFMdgnK7dFgr8Fufcu3NTzFLQyFileh08/edit#slide=id.g308e6baee55_0_59).

## License
This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
