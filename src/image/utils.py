import cv2
import imutils


class Contour:
    def __init__(
        self,
        image,
        threshold_min_area=None,
        threshold_max_area=None
    ):

        self.image = image.copy()
        self.threshold_max_area = threshold_max_area  if threshold_max_area else self.image.shape[0]*self.image.shape[1]
        self.threshold_min_area = threshold_min_area  if threshold_min_area else self.image.shape[0]*self.image.shape[1]*0.10


    def findContours(
        self,
        mode=cv2.RETR_TREE,
        method=cv2.CHAIN_APPROX_SIMPLE
    ):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh, mode, method)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        # Contours are sorted by thier area
        self.contours = []

        for cout in cnts:
            perimeter = cv2.arcLength(cout, True)
            approx = cv2.approxPolyDP(cout, 0.035 * perimeter, True)
            x,y,w,h = cv2.boundingRect(approx)
            aspect_ratio = w / float(h)
            area = cv2.contourArea(cout)
            # if len(approx) == 4:
            self.contours.append([cout, area])

    def draw_contour(self, nos_contour=2):
        contours = sorted(
            self.contours, key = lambda tupl: tupl[1],
            reverse=True
        )
        image = self.image.copy()

        for i in range(nos_contour):
            cont = contours[i][0]
            peri = cv2.arcLength(cont,  True)
            approx = cv2.approxPolyDP(cont,  0.035 * peri, True)
            x,y,w,h = cv2.boundingRect(approx)
            area = cv2.contourArea(cont)
            if area > self.threshold_min_area:
                cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
                cv2.putText(
                    image,
                    str(cv2.contourArea(cont)),
                    org=(x,y),
                    fontFace = cv2.FONT_HERSHEY_DUPLEX,
                    fontScale = 1,
                    color = (0, 255, 0))
                print(cv2.contourArea(cont), (x,y,w,h))
        return image