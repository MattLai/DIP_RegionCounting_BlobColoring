import cv2
import numpy as np

class cell_counting():
    FIND_COLOR = 255

    UNCHECK = 0
    CHECKED = 1

    image = []
    marked_pixels = []
    pixel_group_arr = []
    pixel_group = []

    height = 0
    width = 0

    regions = dict()
    k = 1

    def grow(self, y, x):

        self.marked_pixels[y, x] = self.CHECKED
        self.pixel_group.append((y, x))

        if (x > 0):
            if (self.image[y, x - 1] == self.FIND_COLOR and self.marked_pixels[y, x - 1] == self.UNCHECK):
                self.grow(y, x - 1)
        if (y > 0):
            if (self.image[y - 1, x] == self.FIND_COLOR and self.marked_pixels[y - 1, x] == self.UNCHECK):
                self.grow(y - 1, x)
        if (x < self.width - 1):
            if (self.image[y, x + 1] == self.FIND_COLOR and self.marked_pixels[y, x + 1] == self.UNCHECK):
                self.grow(y, x + 1)
        if (y < self.height - 1):
            if (self.image[y + 1, x] == self.FIND_COLOR and self.marked_pixels[y + 1, x] == self.UNCHECK):
                self.grow(y + 1, x)

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""
        # 0 = black, 1 or 255 = white
        # regions = dict()

        self.image = image
        height, width = image.shape[0], image.shape[1]

        self.height = height
        self.width = width

        self.marked_pixels = np.zeros((height, width), dtype=np.uint32)

        for y in range(height):
            for x in range(width):
                if (image[y, x] == self.FIND_COLOR and self.marked_pixels[y, x] == self.UNCHECK):
                    self.grow(y, x)
                    # self.pixel_group_arr.append(self.pixel_group)
                    self.regions[self.k] = self.pixel_group
                    self.k += 1
                    self.pixel_group = []
                else:
                    self.marked_pixels[y, x] = self.CHECKED
                    
        return self.regions


    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""

        l1 = []
        l2 = []
        area = []
        for regionNumber in self.regions:
            eachCell = self.regions[regionNumber]
            length = len(eachCell)
            area.append(length)
            for coordinate in eachCell:
                l1.append(coordinate[0])
                l2.append(coordinate[1])
            center_x = int(sum(l1)/length)
            center_y = int(sum(l2)/length)
            l1 = []
            l2 = []
            print("Region number: {0}, Area: {1}, Center/Centroid: {2} ".format(regionNumber, (length), (center_x, center_y)))

        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return area

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        height, width = image.shape[0], image.shape[1]
        final_image = np.zeros((height, width, 3), dtype=np.uint8)

        regionNumberOfPixelBiggerThan15 = []
        regionNumberOfPixelSmallerThan15 = []
        pixelMoreThan15 = []
        pixelLessThan15 = []

        font = cv2.FONT_HERSHEY_SIMPLEX

        for region in self.regions:
            lst = (self.regions[region])
            if len(lst) < 15:
                pixelLessThan15.append(region)
            else:
                pixelMoreThan15.append(region)

        for region_number in pixelLessThan15:
            regionNumberOfPixelSmallerThan15.append(self.regions[region_number])
        for regionNumber in pixelMoreThan15:
            regionNumberOfPixelBiggerThan15.append(self.regions[regionNumber])


        for bigNumber in regionNumberOfPixelBiggerThan15:
            for bigCoordinate in bigNumber:
                final_image[bigCoordinate] = (255, 255, 255)

        l1 = []
        l2 = []
        area = []
        number = []
        for regionNumber in pixelMoreThan15:
            eachCell = self.regions[regionNumber]
            number.append(self.regions[regionNumber])
            length = len(eachCell)
            area.append(length)
            for coordinate in eachCell:
                l1.append(coordinate[0])
                l2.append(coordinate[1])
            center_x = int(sum(l1) / length)
            center_y = int(sum(l2) / length)
            l1 = []
            l2 = []
            final_image[center_x, center_y] = (0, 0, 255)
            cv2.putText(final_image, "%s,%s" % (regionNumber, length), (center_y, center_x), font, 0.25, (0, 0, 255), 1)


        return final_image

