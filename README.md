# Real-Time Barcode and QR Code Scanner

This project is a Python-based application that uses your webcam to detect and decode various types of barcodes and QR codes in real-time. It leverages the power of the OpenCV library to identify codes from a live video stream, draws a bounding box around them, and prints the decoded information to the console.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Built With](#built-with)

## Features

-   **Real-Time Detection:** Scans for codes directly from a live webcam feed.
-   **Multi-Code Support:** Capable of detecting and decoding both standard 1D barcodes and 2D QR codes.
-   **Visual Feedback:** Automatically draws a green bounding box around any detected code in the video stream.
-   **Console Output:** Prints the decoded data (e.g., a URL from a QR code or a number from a barcode) directly to the terminal.
-   **Simple Interface:** A straightforward application that starts scanning immediately upon execution.

## How It Works

The script operates through the following steps:
1.  Initializes a video capture object to access the default webcam.
2.  Continuously reads frames from the video stream in a loop.
3.  For each frame, it utilizes OpenCV's built-in `QRCodeDetector` and `BarcodeDetector` to search for recognizable codes.
4.  If a code is successfully detected and decoded, the script:
    -   Prints the decoded information to the console.
    -   Draws a green polygon to highlight the location of the code on the frame.
5.  Displays the annotated video frame in a window titled "Barcode and QR Code Scanner".
6.  The application closes when the user presses the 'a' key.

## Prerequisites

Before you can run this script, you need to have Python and the following libraries installed on your system:

-   **Python 3.x**
-   **OpenCV for Python**
-   **NumPy**

## Installation

1.  **Clone the repository or download the `main.py` script.**

2.  **Install the required libraries using pip:**
    Open your terminal or command prompt and run the following command:
    ```sh
    pip install opencv-python numpy
    ```

## Usage

1.  Navigate to the directory where you saved the `main.py` file using your terminal.

2.  Run the script with the following command:
    ```sh
    python main.py
    ```

3.  A window will open showing your webcam's feed. Point the camera at a barcode or a QR code.

4.  Watch the terminal for the decoded information to be printed.

5.  To close the application, ensure the video window is active and press the **'a'** key on your keyboard.

## Built With

-   [OpenCV](https://opencv.org/) - The core library used for computer vision tasks, including barcode detection.
-   [NumPy](https://numpy.org/) - A fundamental package for numerical computation in Python, used by OpenCV.

