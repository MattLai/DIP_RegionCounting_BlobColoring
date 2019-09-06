1. Region Counting:
Write a program to binarize a gray-level image based on the assumption that the image has a bimodal histogram.  You are to implement the method to estimate the optimal threshold required to binarize the image. The threshold is to be computed using the average of the expectation of the two distributions. Your code should report both the binarized image and the optimal threshold value. Also assume that foreground objects are darker than background objects in the input gray-level image.

2. Blob Coloring
Write a program to perform blobcoloring. The input to your code should be a binary image (0's, and 255's) and the output should be a list of objects or regions in the image.

3. Ignore cells smaller than 15 pixels in area.
Ignore cells smaller than 15 pixels in area and generate a report of the remaining cells (Cell Number, Area, Location)

4. Image Compression(Run Length Encoding)
Write a code to compress a binary image using Run length Encoding.

--------------------------

How to Run your code?

  - Usage: ./dip_hw2_region_analysis.py -i image-name
       - image-name: name of the image
  - example: ./dip_hw2_region_analysis.py -i cells.png
  - Please make sure your code runs when you run the above command from prompt
  - Describe your method and findings in the report.md file
  - Any output images or files must be saved to "output/" folder

---------------------------

1. the code has to run using command
  
  ./dip_hw2_region_analysis.py -i image-name  
  
  (or)
  
  python dip_hw2_region_analysis.py -i image-name  
  
  
2. Any output file or image should be written to output/ folder