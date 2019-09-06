import numpy as np
class rle:

    def encode_image(self, binary_image):
        """
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """

        pixelValue = []
        height, width = binary_image.shape[0], binary_image.shape[1]
        for i in range(height):
            for j in range(width):
                pixelValue.append(binary_image[i, j])


        count = 1
        previous = ''
        rle_code = []

        for i in pixelValue:
            if i == previous:
                count += 1
            else:
                rle_code.append((count, previous))
                count = 1
                previous = i
        entry = (count, previous)
        rle_code.append(entry)

        del rle_code[0]


        return rle_code #replace zeros with rle_code
        # return np.zeros(100)


    def decode_image(self, rle_code, height , width):
        """
        Get original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """
        reconstructedImage = np.zeros([height, width], dtype=np.uint8)

        recover = []
        rle_code = np.array(rle_code)
        for times, pixels in rle_code:
            recover += times*[pixels]

        for rowIndex in range(height):
            for colIndex in range(width):
                reconstructedImage[rowIndex, colIndex] = recover[rowIndex*width+colIndex]

        return reconstructedImage #replace zeros with image reconstructed from rle_Code
        # return np.zeros((100, 100), dtype=np.uint8)




        




