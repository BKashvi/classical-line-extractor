CLASSICAL LANE LINE EXTRACTOR

1. Loading the Image

The program loads a road image from the images folder.

2. Converting to HSV

The image is converted from BGR to HSV color space to make color-based lane detection easier.

3. Detecting White and Yellow Lanes

Color masks are created to identify white and yellow lane markings.

4. Combining the Masks

The two masks are combined to create one image containing the selected lane-marking regions.

5. Gaussian Blur

Gaussian blur reduces small details and noise before edge detection.

6. Canny Edge Detection

Canny identifies edges that may correspond to lane markings.

7. Region of Interest (ROI)

A selected region of the image is used to focus processing on the road area.

8. Detecting Lane Lines

The Probabilistic Hough Line Transform detects line segments from the processed edges.

CHALLENGES FACED

Understanding how the different processing stages work together was an important part of the project. Image paths and parameter selection also required attention. The output depends on lighting, road conditions, image quality, and the selected color thresholds.

AREAS OF IMPROVMENT

1.Test the pipeline on more road images.

2.Improve detection under different lighting conditions.

3.Group detected segments into more consistent lane lines.

4.Explore curved-lane detection.

5.Measure the time taken to process images.