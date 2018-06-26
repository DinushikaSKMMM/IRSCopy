from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import tkinter as tk
from tkinter import filedialog
import csv
import os
import getUsersOfSign
import getCompanyOfSeal

def signatureFeature_TrainInput():
    root = tk.Tk()
    file_path = ['E:\Level4_Project\WritingFeatures5.csv']
    file_path1 = filedialog.askopenfilenames(parent=root, title='Choose a file')
    file_path = root.tk.splitlist(file_path1)
    # print (file_path)

    for imagePath in file_path:
        img = cv2.imread(imagePath)
        print(imagePath)

        if img is None:
            print("Enter Image")

        def midpoint(ptA, ptB):
            return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

        # construct the argument parse and parse the arguments
        ap = argparse.ArgumentParser()
        args = vars(ap.parse_args())
        # load the image, convert it to grayscale, and blur it slightly
        # ------------------------------------------------------------------------------------------image = cv2.imread(args["image"])
        image = cv2.imread(imagePath)

        #cv2.namedWindow("Input Image", cv2.WINDOW_NORMAL)
        #cv2.imshow("Input Image", image)
        #cv2.waitKey(0)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #cv2.namedWindow("Gray Image", cv2.WINDOW_NORMAL)
        #cv2.imshow("Gray Image", gray)
        #cv2.waitKey(0)

        gray = cv2.GaussianBlur(gray, (7, 7), 0)
        #cv2.namedWindow("GaussianBlur Image", cv2.WINDOW_NORMAL)
        #cv2.imshow("GaussianBlur Image", gray)
        #cv2.waitKey(0)
        ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        th2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                    cv2.THRESH_BINARY, 11, 2)
        #cv2.namedWindow("Adaptive Threshold Image", cv2.WINDOW_NORMAL)
        #cv2.imshow("Adaptive Threshold Image", th2)
        #cv2.waitKey(0)

        th3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                    cv2.THRESH_BINARY, 11, 2)
        #cv2.namedWindow("Adaptive Threshold GAUSSIAN Image", cv2.WINDOW_NORMAL)
        #cv2.imshow("Adaptive Threshold GAUSSIAN Image", th3)
        #cv2.waitKey(0)
        # perform edge detection, then perform a dilation + erosion to
        # close gaps in between object edges

        edged = cv2.Canny(gray, 50, 100)
        #cv2.namedWindow("Edge Detection Image", cv2.WINDOW_NORMAL)
        #cv2.imshow("Edge Detection Image", edged)
        #cv2.waitKey(0)

        edged = cv2.dilate(edged, None, iterations=1)
        #cv2.namedWindow("Dilate Image", cv2.WINDOW_NORMAL)
        #cv2.imshow("Dilate Image", edged)
        #cv2.waitKey(0)

        edged = cv2.erode(edged, None, iterations=1)
        #cv2.namedWindow("Erode Image", cv2.WINDOW_NORMAL)
        #cv2.imshow("Erode Image", edged)
        #cv2.waitKey(0)
        # find contours in the edge map
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        # sort the contours from left-to-right and initialize the
        # 'pixels per metric' calibration variable
        (cnts, _) = contours.sort_contours(cnts)
        pixelsPerMetric = None
        # loop over the contours individually
        # print(cnts)
        for c in cnts:
            # if the contour is not sufficiently large, ignore it
            if cv2.contourArea(c) < 1000:
                continue
            area = cv2.contourArea(c)
            Perimeter = cv2.arcLength(c, True)
            M = cv2.moments(c)
            centroid_x = int(M['m10'] / M['m00'])
            centroid_y = int(M['m01'] / M['m00'])
            x, y, w, h = cv2.boundingRect(c)
            aspect_ratio = float(w) / h
            # Extent is the ratio of contour area to bounding rectangle area.
            rect_area = w * h
            extent = float(area) / rect_area
            hull = cv2.convexHull(c)
            hull_area = cv2.contourArea(hull)
            solidity = float(area) / hull_area
            # Equivalent Diameter is the diameter of the circle whose area is same as the contour area.
            equi_diameter = np.sqrt(4 * area / np.pi)
            # the angle at which object is directed.
            (x, y), (MA, ma), angle = cv2.fitEllipse(c)
            mask = np.zeros(edged.shape, np.uint8)
            cv2.drawContours(mask, [c], 0, 255, -1)
            pixelpoints = np.transpose(np.nonzero(mask))
            approx = cv2.approxPolyDP(c, 0.1 * cv2.arcLength(c, True), True)
            features_array = []
            print("Contour Area:", area)
            f1 = round(area, 8)
            features_array.append(f1)

            f2 = round(Perimeter, 8)
            print("Contour Perimeter:", Perimeter)
            features_array.append(f2)

            f3 = round(centroid_x, 8)
            print("Cenrtoid x:", f3)

            f4 = round(centroid_y, 8)
            # features_array.append(centroid_x)
            print("Cenrtoid y:", f4)

            f5 = round(aspect_ratio, 8)
            # atures_array(centroid_y)
            print("Aspect Ratio(The ratio of width to height):", aspect_ratio)
            features_array.append(f5)

            f6 = round(extent, 8)
            print("Extent(The Ratio of contour area to bounding rectangle area):", extent)
            features_array.append(f6)

            f7 = round(hull_area, 8)
            print("Hull Area(The minimum set of points that define a polygon containing all the points):", hull_area)
            features_array.append(f7)

            f8 = round(solidity, 8)
            print("Solidity Area(The ratio of contour area to its convex hull area):", solidity)
            features_array.append(f8)

            f9 = round(equi_diameter, 8)
            print("Equivalent Diameter(The diameter of the circle whose area is same as the contour area):",
                  equi_diameter)
            features_array.append(f9)

            f10 = round(angle, 8)
            print("Orientation(The angle at which object is directed):", angle)
            features_array.append(f10)
            # print("Pixel Points(All the points which comprises that object):", pixelpoints)
            # print("approximation Epsilon:", approx)
            f11 = round(rect_area, 8)
            features_array.append(f11)

            orig = image.copy()
            for i in enumerate(c):
                rect = cv2.boundingRect(c)
                # box = cv2.minAreaRect(c)
                x, y, w, h = rect
                box = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cropped = image[y: y + h, x: x + w]
                # cv2.imshow("Show Boxes", cropped)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                #cv2.imwrite("x" + str(i) + ".jpg", cropped)
                break
                h, w = np.shape(area)
            # print image properties.
            getUsersOfSign.getSignOwner(imagePath)
            print("Width of contour area:", str(w))

            # = round(str(w), 8)
            f12 = round(w, 8)
            features_array.append(f12)
            #features_array.append(str(w))

            # f12 = round(str(h), 8)
            print("Height of contour area:", str(h))
            #features_array.append(str(h))
            f13 = round(h, 8)
            features_array.append(f13)

            print(features_array)
            #  with open(r'E:\Level4_Project\WritingFeatures.csv', mode='a+', encoding='UTF-8', errors='strict', buffering=1) as csvFile:
            with open(r'E:\Level4_Project\WritingFeatures5.csv', mode='a+', newline='') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(features_array)

            csvFile.close()

            print("Writing complete")  # compute the rotated bounding box of the contour
            box = cv2.minAreaRect(c)
            box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
            box = np.array(box, dtype="int")
            # order the points in the contour such that they appear
            # in top-left, top-right, bottom-right, and bottom-left
            # order, then draw the outline of the rotated bounding
            # box
            box = perspective.order_points(box)
            cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)
            # loop over the original points and draw them
            for (x, y) in box:
                cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)
            # unpack the ordered bounding box, then compute the midpoint
            # between the top-left and top-right coordinates, followed by
            # the midpoint between bottom-left and bottom-right coordinates
            (tl, tr, br, bl) = box
            (tltrX, tltrY) = midpoint(tl, tr)
            (blbrX, blbrY) = midpoint(bl, br)
            # compute the midpoint between the top-left and top-right points,
            # followed by the midpoint between the top-righ and bottom-right
            (tlblX, tlblY) = midpoint(tl, bl)
            (trbrX, trbrY) = midpoint(tr, br)
            (x1, y1) = tl
            (x2, y2) = tr
            (x3, y3) = br
            (x4, y4) = bl
            # draw the midpoints on the image
            cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
            cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
            cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
            cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
            # draw lines between the midpoints
            cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
                     (255, 0, 255), 2)
            cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
                     (255, 0, 255), 2)
            # compute the Euclidean distance between the midpoints
            dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
            dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
            # if the pixels per metric has not been initialized, then
            # compute it as the ratio of pixels to supplied metric
            # (in this case, inches)
            if pixelsPerMetric is None:
                pixelsPerMetric = dB
            # compute the size of the object
            dimA = dA / pixelsPerMetric
            dimB = dB / pixelsPerMetric
            # draw the object sizes on the image
            cv2.putText(orig, "{:.1f}in".format(dimA),
                        (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
                        0.65, (255, 255, 255), 2)
            cv2.putText(orig, "{:.1f}in".format(dimB),
                        (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
                        0.65, (255, 255, 255), 2)

            # show the output image
            #cv2.namedWindow("Object Detected Image", cv2.WINDOW_NORMAL)
            #cv2.imshow("Object Detected Image", orig)
            cv2.waitKey(0)
            #cv2.namedWindow("Segmented Image", cv2.WINDOW_NORMAL)
            #cv2.imshow("Segmented Image", cropped)
            #cv2.waitKey(0)
            cv2.destroyAllWindows()
            break

def sealFeature_TrainInput():
    root = tk.Tk()
    file_path = ['E:\Level4_Project\WritingFeatures5.csv']
    file_path1 = filedialog.askopenfilenames(parent=root, title='Choose a file')
    file_path = root.tk.splitlist(file_path1)
    # print (file_path)

    for imagePath in file_path:
        img = cv2.imread(imagePath)
        print(imagePath)

        if img is None:
            print("Enter Image")

        def midpoint(ptA, ptB):
            return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

        # construct the argument parse and parse the arguments
        ap = argparse.ArgumentParser()
        args = vars(ap.parse_args())
        # load the image, convert it to grayscale, and blur it slightly
        # ------------------------------------------------------------------------------------------image = cv2.imread(args["image"])
        image = cv2.imread(imagePath)

        # cv2.namedWindow("Input Image", cv2.WINDOW_NORMAL)
        # cv2.imshow("Input Image", image)
        # cv2.waitKey(0)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # cv2.namedWindow("Gray Image", cv2.WINDOW_NORMAL)
        # cv2.imshow("Gray Image", gray)
        # cv2.waitKey(0)

        gray = cv2.GaussianBlur(gray, (7, 7), 0)
        # cv2.namedWindow("GaussianBlur Image", cv2.WINDOW_NORMAL)
        # cv2.imshow("GaussianBlur Image", gray)
        # cv2.waitKey(0)
        ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        th2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                    cv2.THRESH_BINARY, 11, 2)
        # cv2.namedWindow("Adaptive Threshold Image", cv2.WINDOW_NORMAL)
        # cv2.imshow("Adaptive Threshold Image", th2)
        # cv2.waitKey(0)

        th3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                    cv2.THRESH_BINARY, 11, 2)
        # cv2.namedWindow("Adaptive Threshold GAUSSIAN Image", cv2.WINDOW_NORMAL)
        # cv2.imshow("Adaptive Threshold GAUSSIAN Image", th3)
        # cv2.waitKey(0)
        # perform edge detection, then perform a dilation + erosion to
        # close gaps in between object edges

        edged = cv2.Canny(gray, 50, 100)
        # cv2.namedWindow("Edge Detection Image", cv2.WINDOW_NORMAL)
        # cv2.imshow("Edge Detection Image", edged)
        # cv2.waitKey(0)

        edged = cv2.dilate(edged, None, iterations=1)
        # cv2.namedWindow("Dilate Image", cv2.WINDOW_NORMAL)
        # cv2.imshow("Dilate Image", edged)
        # cv2.waitKey(0)

        edged = cv2.erode(edged, None, iterations=1)
        # cv2.namedWindow("Erode Image", cv2.WINDOW_NORMAL)
        # cv2.imshow("Erode Image", edged)
        # cv2.waitKey(0)
        # find contours in the edge map
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        # sort the contours from left-to-right and initialize the
        # 'pixels per metric' calibration variable
        (cnts, _) = contours.sort_contours(cnts)
        pixelsPerMetric = None
        # loop over the contours individually
        # print(cnts)
        for c in cnts:
            # if the contour is not sufficiently large, ignore it
            if cv2.contourArea(c) < 1000:
                continue
            area = cv2.contourArea(c)
            Perimeter = cv2.arcLength(c, True)
            M = cv2.moments(c)
            centroid_x = int(M['m10'] / M['m00'])
            centroid_y = int(M['m01'] / M['m00'])
            x, y, w, h = cv2.boundingRect(c)
            aspect_ratio = float(w) / h
            # Extent is the ratio of contour area to bounding rectangle area.
            rect_area = w * h
            extent = float(area) / rect_area
            hull = cv2.convexHull(c)
            hull_area = cv2.contourArea(hull)
            solidity = float(area) / hull_area
            # Equivalent Diameter is the diameter of the circle whose area is same as the contour area.
            equi_diameter = np.sqrt(4 * area / np.pi)
            # the angle at which object is directed.
            (x, y), (MA, ma), angle = cv2.fitEllipse(c)
            mask = np.zeros(edged.shape, np.uint8)
            cv2.drawContours(mask, [c], 0, 255, -1)
            pixelpoints = np.transpose(np.nonzero(mask))
            approx = cv2.approxPolyDP(c, 0.1 * cv2.arcLength(c, True), True)
            features_array = []
            print("Contour Area:", area)
            f1 = round(area, 8)
            features_array.append(f1)

            f2 = round(Perimeter, 8)
            print("Contour Perimeter:", Perimeter)
            features_array.append(f2)

            f3 = round(centroid_x, 8)
            print("Cenrtoid x:", f3)

            f4 = round(centroid_y, 8)
            # features_array.append(centroid_x)
            print("Cenrtoid y:", f4)

            f5 = round(aspect_ratio, 8)
            # atures_array(centroid_y)
            print("Aspect Ratio(The ratio of width to height):", aspect_ratio)
            features_array.append(f5)

            f6 = round(extent, 8)
            print("Extent(The Ratio of contour area to bounding rectangle area):", extent)
            features_array.append(f6)

            f7 = round(hull_area, 8)
            print("Hull Area(The minimum set of points that define a polygon containing all the points):", hull_area)
            features_array.append(f7)

            f8 = round(solidity, 8)
            print("Solidity Area(The ratio of contour area to its convex hull area):", solidity)
            features_array.append(f8)

            f9 = round(equi_diameter, 8)
            print("Equivalent Diameter(The diameter of the circle whose area is same as the contour area):",
                  equi_diameter)
            features_array.append(f9)

            f10 = round(angle, 8)
            print("Orientation(The angle at which object is directed):", angle)
            features_array.append(f10)
            # print("Pixel Points(All the points which comprises that object):", pixelpoints)
            # print("approximation Epsilon:", approx)
            f11 = round(rect_area, 8)
            features_array.append(f11)

            orig = image.copy()
            for i in enumerate(c):
                rect = cv2.boundingRect(c)
                # box = cv2.minAreaRect(c)
                x, y, w, h = rect
                box = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cropped = image[y: y + h, x: x + w]
                # cv2.imshow("Show Boxes", cropped)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                # cv2.imwrite("x" + str(i) + ".jpg", cropped)
                break
                h, w = np.shape(area)
            # print image properties.
            getCompanyOfSeal.getComany(imagePath)
            #getUsersOfSign.getSignOwner(imagePath)
            print("Width of contour area:", str(w))

            # = round(str(w), 8)
            f12 = round(w, 8)
            features_array.append(f12)
            # features_array.append(str(w))

            # f12 = round(str(h), 8)
            print("Height of contour area:", str(h))
            # features_array.append(str(h))
            f13 = round(h, 8)
            features_array.append(f13)

            print(features_array)
            #  with open(r'E:\Level4_Project\WritingFeatures.csv', mode='a+', encoding='UTF-8', errors='strict', buffering=1) as csvFile:
            with open(r'E:\Level4_Project\WritingSealFeatures.csv', mode='a+', newline='') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(features_array)

            csvFile.close()

            print("Writing complete")  # compute the rotated bounding box of the contour
            box = cv2.minAreaRect(c)
            box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
            box = np.array(box, dtype="int")
            # order the points in the contour such that they appear
            # in top-left, top-right, bottom-right, and bottom-left
            # order, then draw the outline of the rotated bounding
            # box
            box = perspective.order_points(box)
            cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)
            # loop over the original points and draw them
            for (x, y) in box:
                cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)
            # unpack the ordered bounding box, then compute the midpoint
            # between the top-left and top-right coordinates, followed by
            # the midpoint between bottom-left and bottom-right coordinates
            (tl, tr, br, bl) = box
            (tltrX, tltrY) = midpoint(tl, tr)
            (blbrX, blbrY) = midpoint(bl, br)
            # compute the midpoint between the top-left and top-right points,
            # followed by the midpoint between the top-righ and bottom-right
            (tlblX, tlblY) = midpoint(tl, bl)
            (trbrX, trbrY) = midpoint(tr, br)
            (x1, y1) = tl
            (x2, y2) = tr
            (x3, y3) = br
            (x4, y4) = bl
            # draw the midpoints on the image
            cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
            cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
            cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
            cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
            # draw lines between the midpoints
            cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
                     (255, 0, 255), 2)
            cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
                     (255, 0, 255), 2)
            # compute the Euclidean distance between the midpoints
            dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
            dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
            # if the pixels per metric has not been initialized, then
            # compute it as the ratio of pixels to supplied metric
            # (in this case, inches)
            if pixelsPerMetric is None:
                pixelsPerMetric = dB
            # compute the size of the object
            dimA = dA / pixelsPerMetric
            dimB = dB / pixelsPerMetric
            # draw the object sizes on the image
            cv2.putText(orig, "{:.1f}in".format(dimA),
                        (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
                        0.65, (255, 255, 255), 2)
            cv2.putText(orig, "{:.1f}in".format(dimB),
                        (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
                        0.65, (255, 255, 255), 2)

            # show the output image
            # cv2.namedWindow("Object Detected Image", cv2.WINDOW_NORMAL)
            # cv2.imshow("Object Detected Image", orig)
            cv2.waitKey(0)
            # cv2.namedWindow("Segmented Image", cv2.WINDOW_NORMAL)
            # cv2.imshow("Segmented Image", cropped)
            # cv2.waitKey(0)
            cv2.destroyAllWindows()
            break






