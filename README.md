# Object Detection Using Haar Cascade Classifier
Viola Jones algorithm is named after two computer vision researchers who proposed the method in 2001, Paul Viola and Michael Jones in their paper, “Rapid Object Detection using a Boosted Cascade of Simple Features”. This framework can be trained to detect almost any object, but this primarily solves the problem of face detection in real-time. 

* [About](#About)
* [Requirements](#Requirements)
*  [Example Usage](#usage)


<a id="About"></a>
## About

### The Viola Jones algorithm has four main steps
1. Selecting Haar-like features
2. Creating an integral image
3. Running AdaBoost training
4. Creating classifier cascades

### There are 3 types of Haar-like features that Viola and Jones identified in their research:
1. Edge features
2. Line-features
3. Four-sided features

Edge features and Line features are useful for detecting edges and lines respectively. The four-sided features are used for finding diagonal features.The value of the feature is calculated as a single number: the sum of pixel values in the black area minus the sum of pixel values in the white area. Since our faces are of complex shapes with darker and brighter spots, a Haar-like feature gives you a large number when the areas in the black and white rectangles are very different. Using this value, we get a lot of information out of the image.

### Integral Image
An Integral image is used as a quick and efficient way to calculate the sum of pixel values in an image or rectangular part of an image.
Using these integral images, we save a lot of time calculating the summation of all the pixels in a rectangle as we only have to perform calculations on four edges of the rectangle.

### AdaBoost
For a window of 24x24 pixels, there can be about 160,000 possible features,but only a few of these features are important to identify a face.Hence AdaBoost algorithm is used to train the classifier with only the best features.

### Cascade Classifier
the AdaBoost will finally select the best features around say 2500, but it is still a time-consuming process to calculate these features for each region. We have a 24×24 window which we slide over the input image, and we need to find if any of those regions contain the face. The job of the cascade is to quickly discard non-faces, and avoid wasting precious time and computations. Thus, achieving the speed necessary for real-time face detection.

<a id="Requirements"></a>

## Requirements
<ul>
  <li>Python 3.x</li>
  <li>OpenCV 2.x</li>
</ul

