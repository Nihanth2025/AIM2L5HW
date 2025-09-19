import cv2
import numpy as np
def apply_color_filter(image_path, filter_type):
  '''Choose any one of the folloeing Applies a color filter to an image.'''
  filtered_image = image.copy()
  if filter_type == 'red_tint':
    filtered_image[:,:,1] = 0
    filtered_image[:,:,0] = 0
  elif filter_type == 'blue_tint':
    filtered_image[:,:,1] = 0
    filtered_image[:,:,2] = 0
  elif filter_type == 'green_tint':
    filtered_image[:,:,0] = 0
    filtered_image[:,:,2] = 0
  elif filter_type == "increased red":
    filtered_image[:,:,2] = cv2.add(filtered_image[:,:,2], 50)
  elif filter_type == "decreased blue":
    filtered_image[:,:,0] = cv2.subtract(filtered_image[:,:,0], 50)
  return filtered_image
image_path = 'example.jpg'
image=cv2.imread(image_path)
if image is None:
  print("Error: Could not load image.")
else:
  filter_type = 'original'
  print("Press the following keys to apply filters:")
  print("r - Red Tint")
  print("b - Blue Tint")
  print("g - Green Tint")
  print("i - Increased Red")
  print("d - Decreased Blue")
  print("q - Quit")
  while True:
    filtered_image =apply_color_filter(image,filter_type)
    cv2.imshow('Filtered Image',filtered_image)
    key = cv2.waitKey(0)
    if key == ord('r'):
      filter_type = 'red_tint'
    elif key == ord('b'):
      filter_type = 'blue_tint'
    elif key == ord('g'):
      filter_type = 'green_tint'
    elif key == ord('i'):
      filter_type = 'increased red'
    elif key == ord('d'):
      filter_type = 'decreased blue'
    elif key == ord('q'):
      print("Exiting...")
      break
    else:
      print("Invalid key pressed.")
cv2.destroyAllWindows() 