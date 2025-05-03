import cv2
import numpy as np

def barcode(frame):
    # Define Mask (Kernel)
    kernel = np.array([[1, 0, -1],
                       [1, 0, -1],
                       [1, 0, -1]])

    # Apply 2D convolution for edge detection
    convolved = cv2.filter2D(frame, -1, kernel)

    # Define sharpening kernel
    sharp_kernel = np.array([[ 0, -1,  0],
                             [-1,  5, -1],
                             [ 0, -1,  0]])

    # Apply 2D convolution for sharpening
    sharpened = cv2.filter2D(convolved, -1, sharp_kernel)

    # Convert to grayscale
    gray = cv2.cvtColor(sharpened, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply adaptive thresholding for better contrast
    adaptive_thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY, 11, 2)

    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced_gray = clahe.apply(adaptive_thresh)

    qr_decoder = cv2.QRCodeDetector()
    value, pts, _ = qr_decoder.detectAndDecode(frame)

    if value:
        print(f"QR Code Detected: {value}")

        if pts is not None:
            pts = np.int32(pts).reshape(-1, 2)
            cv2.polylines(frame, [pts], True, (0, 255, 0), 3)

    barcode_decoder = cv2.barcode_BarcodeDetector()
    retval, decoded_info, points, straight_rects = barcode_decoder.detectAndDecodeMulti(frame)

    if retval:
        for info, point in zip(decoded_info, points):
            if info:
                print(f"Barcode Detected: {info}")

                points = np.int32(point).reshape(-1, 2)
                cv2.polylines(frame, [points], True, (0, 255, 0), 3)

    return frame

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

print("Press 'a' to quit the application.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read a frame.")
        break

    annotated_frame = barcode(frame)
    cv2.imshow("Barcode and QR Code Scanner", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cap.release()
cv2.destroyAllWindows()
