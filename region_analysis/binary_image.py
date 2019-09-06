import numpy as np

class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""
        hist = [0]*256
        height, width = image.shape[0], image.shape[1]

        for i in range(height):
            for j in range(width):
                x = image[i, j]
                hist[x] += 1

        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""

        median = len(hist)/2
        right_T = 0
        left_T = 0
        max_index = 0
        min_index = 0
        for index, times in enumerate(hist):
            if index > median:
                if times > right_T:
                    right_T = times
                    max_index = index
            if index <= median:
                if times > left_T:
                    left_T = times
                    min_index = index
        T = int((max_index + min_index)/2)
        threshold = 75
        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        # Algorithm
        # if image(height, width) > thres:
        #     bin_img(height, width) = 0
        # else:
        #     bin_img(height, width) = maxValue

        bin_img = image.copy()
        hist = self.compute_histogram(image)
        thres = self.find_optimal_threshold(hist)
        height, width = image.shape[0], image.shape[1]

        for i in range(height):
            for j in range(width):
                if (bin_img[i, j] > thres):
                    bin_img[i, j] = 0
                else:
                    bin_img[i, j] = 255


        return bin_img


