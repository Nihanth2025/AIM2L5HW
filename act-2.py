import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_color_filter(image, filter_type):
    '''Applies a color filter to an image.'''
    filtered_image = image.copy()
    if filter_type == 'red_tint':
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == 'blue_tint':
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == 'green_tint':
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == 'increased_red':
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == 'decreased_blue':
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)
    elif filter_type == 'decreased_red':
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 2], 50)
    elif filter_type == 'increased_green':
        try:
            green_intensity = int(input("Enter the green intensity to increase: "))
            filtered_image[:, :, 1] = cv2.add(filtered_image[:, :, 1], green_intensity)
        except ValueError:
            print("Invalid input. Using default intensity of 50.")
            filtered_image[:, :, 1] = cv2.add(filtered_image[:, :, 1], 50)
    elif filter_type == 'original':
        pass  
    return filtered_image

def display_image(title, image):
    """Displays an image using matplotlib."""
    plt.figure(figsize=(10, 10))
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def interactive_edge_detection(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read image.")
        return
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Grayscale Image", gray_image)

    while True:
        print("\nChoose an edge detection method:")
        print("1. Sobel Edge Detection")
        print("2. Canny Edge Detection")
        print("3. Laplacian Edge Detection")
        print("4. Gaussian Blur")
        print("5. Median Filtering")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
            sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)
            combined = cv2.bitwise_or(sobel_x.astype(np.uint8), sobel_y.astype(np.uint8))
            display_image("Sobel Edge Detection", combined)
        elif choice == "2":
            try:
                low = int(input("Low threshold: "))
                high = int(input("High threshold: "))
                edges = cv2.Canny(gray_image, low, high)
                display_image("Canny Edge Detection", edges)
            except ValueError:
                print("Invalid threshold values.")
        elif choice == "3":
            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            display_image("Laplacian Edge Detection", laplacian.astype(np.uint8))
        elif choice == "4":
            try:
                ksize = int(input("Kernel size (odd number): "))
                blurred = cv2.GaussianBlur(gray_image, (ksize, ksize), 0)
                display_image("Gaussian Blur", blurred)
            except ValueError:
                print("Invalid kernel size.")
        elif choice == "5":
            try:
                ksize = int(input("Kernel size (odd number): "))
                median = cv2.medianBlur(gray_image, ksize)
                display_image("Median Filtered Image", median)
            except ValueError:
                print("Invalid kernel size.")
        elif choice == "6":
            print("Exiting edge detection...")
            break
        else:
            print("Invalid choice. Try again.")

def color_filter_mode(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image.")
        return

    filter_type = 'original'
    print("\nPress keys to apply filters:")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - Increased Red")
    print("f - Increased Green")
    print("x - Decreased Blue")
    print("y - Decreased Red")
    print("o - Original Image")
    print("q - Quit")

    while True:
        filtered_image = apply_color_filter(image, filter_type)
        cv2.imshow('Filtered Image', filtered_image)
        key = cv2.waitKey(0)

        if key == ord('r'):
            filter_type = 'red_tint'
        elif key == ord('b'):
            filter_type = 'blue_tint'
        elif key == ord('g'):
            filter_type = 'green_tint'
        elif key == ord('i'):
            filter_type = 'increased_red'
        elif key == ord('f'):
            filter_type = 'increased_green'
        elif key == ord('x'):
            filter_type = 'decreased_blue'
        elif key == ord('y'):
            filter_type = 'decreased_red'
        elif key == ord('o'):
            filter_type = 'original'
        elif key == ord('q'):
            print("Exiting color filter mode...")
            break
        else:
            print("Invalid key pressed.")

    cv2.destroyAllWindows()


print("Choose one of the following modes:")
print("1 - Apply Color Filter to Image")
print("2 - Edge Detection Filters")
mode = input("Enter your choice: ")

image_path = 'example.jpg' 

if mode == "1":
    color_filter_mode(image_path)
elif mode == "2":
    interactive_edge_detection(image_path)
else:
    print("Invalid choice.")