import cv2
import numpy as np
import matplotlib.pyplot as plt



def calculate_disease_severity(image_path):
    # Load the image
    img = cv2.imread(image_path)
    
    # Convert to grayscale for easier processing
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    plt.imshow(gray)
    plt.show()

  
    
    # Apply thresholding to segment the diseased areas
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    plt.imshow(thresh)
    plt.show()

    
    # Find contours of the diseased areas
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Calculate the total area of the diseased regions
    total_diseased_area = sum(cv2.contourArea(cnt) for cnt in contours)
    
    # Calculate the total area of the entire leaf
    total_leaf_area = img.shape[0] * img.shape[1]
    
    # Calculate disease severity as a percentage
    severity_percentage = (total_diseased_area / total_leaf_area) * 100
    
    return severity_percentage

if __name__ == "__main__":
# Example usage
    late_blight_severity = calculate_disease_severity(r"C:\Users\Pranesh\Downloads\Tomato\late_blight.jpeg")
    # late_blight_severity = calculate_disease_severity(r"C:\Users\tigco\Downloads\severe.jpeg")

    print(f"Early Blight Severity: {late_blight_severity}%")
    # print(f"Late Blight Severity: {late_blight_severity}%")

