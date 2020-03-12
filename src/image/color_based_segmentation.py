import os
import colorsys
import cv2, numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans



# image_path = "../../test/proposal_cce_pepper_small.png"
image_path = "../../test/nemo0_crop.jpg"
image_path = "../../test/yeezes_single_crop.jpeg"
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsv_img = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)


def visualize_colors(cluster, centroids):
    # Get the number of different clusters, create histogram, and normalize
    ret_colors = []
    labels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
    (hist, _) = np.histogram(cluster.labels_, bins = labels)
    hist = hist.astype("float")
    hist /= hist.sum()

    # Create frequency rect and iterate through each cluster's color and percentage
    rect = np.zeros((50, 300, 3), dtype=np.uint8)
    colors = sorted([(percent, color) for (percent, color) in zip(hist, centroids)])
    start = 0
    for (percent, color) in colors:
        ret_colors.append([color, percent])
        print(color, "{:0.2f}%".format(percent * 100))
        end = start + (percent * 300)
        cv2.rectangle(rect, (int(start), 0), (int(end), 50), \
                      color.astype("uint8").tolist(), -1)
        start = end
    # return rect, sorted(colors, key=lambda x: x[-1])
    return rect, sorted(ret_colors, key=lambda x: x[-1])

reshape = image.reshape((image.shape[0] * image.shape[1], 3))

# Find and display most dominant colors
cluster = KMeans(n_clusters=5).fit(reshape)
visualize, colors = visualize_colors(cluster, cluster.cluster_centers_)
plt.imshow(visualize)

# hsv_colors = [cv2.cvtColor(np.uint8([[color[0]]]), cv2.COLOR_BGR2HSV) for color in colors]
hsv_colors = [cv2.cvtColor(np.uint8([[color[0]]]), cv2.COLOR_RGB2HSV).flatten() for color in colors]
# hsv_colors = [colorsys.rgb_to_hsv(*color[0]) for color in colors]
print(hsv_colors)
print(colors)

mask = cv2.inRange(
    hsv_img,
    list(hsv_colors[-1]),
    list(hsv_colors[-3])
    )
plt.imshow(mask)

light_orange = (1, 190, 200)
dark_orange = hsv_colors[-1]
dark_orange = (18, 255, 255)
mask = cv2.inRange(
    hsv_img,
    tuple(light_orange),
    tuple(dark_orange))
plt.imshow(mask)


np.asarray(dark_orange) - np.asarray(light_orange)
np.asarray(hsv_colors[-3]) - np.asarray(hsv_colors[-1])
