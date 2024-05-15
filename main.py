import numpy as np
from skimage.color import rgb2gray
from skimage.feature import SIFT, match_descriptors,plot_matches
from skimage.transform import estimate_transform, warp
import matplotlib.pyplot as plt
import cv2
from skimage.feature import match_descriptors, plot_matches, ORB
from skimage.transform import AffineTransform
from detector import detector
import os

def load_images(original_path,rotated_path):

    original_g = cv2.imread(original_path,cv2.IMREAD_GRAYSCALE)
    distorted_g = cv2.imread(rotated_path,cv2.IMREAD_GRAYSCALE)
    return original_path,rotated_path,original_g,distorted_g

def detect_features(original,rotated):
    original_path,distorted_path,original,distorted = load_images(original,rotated)
    # name = distorted_path[-4:]
    
    #Detect Region
    org_region = detector(original_path)
    dist_region = detector(distorted_path)

    #Detect Features using ORB
    orb = ORB(n_keypoints=500,fast_threshold=0.05)
    orb.detect_and_extract(original)
    keypoints_original = orb.keypoints
    descriptors_original = orb.descriptors
    orb.detect_and_extract(distorted)
    keypoints_distorted = orb.keypoints
    descriptors_distorted = orb.descriptors
    # Match features
    matches = match_descriptors(descriptors_original, descriptors_distorted, cross_check=True)
    # Extract matched keypoints
    matched_original = keypoints_original[matches[:, 0]]
    matched_distorted = keypoints_distorted[matches[:, 1]]
    # Estimate similarity transform
    tform = AffineTransform()
    tform.estimate(matched_distorted,matched_original)
    # Apply transformation to get recovered scale and rotation
    scale_recovered = np.sqrt(np.linalg.det(tform.params[0:2, 0:2]))
    theta_recovered = np.degrees(np.arctan2(tform.params[0, 1], tform.params[0, 0]))
    print('ORB Method')
    # print('Recovered scale:', scale_recovered)
    print('Recovered theta:', theta_recovered)

    #Feature detection using SIFT
    original_gray = cv2.normalize(original, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')
    distorted_gray = cv2.normalize(distorted, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')
    # Create SIFT detector
    sift = cv2.SIFT_create()
    # Detect keypoints and descriptors
    keypoints_original_SIFT, descriptors_original_SIFT = sift.detectAndCompute(original_gray, None)
    keypoints_distorted_SIFT, descriptors_distorted_SIFT = sift.detectAndCompute(distorted_gray, None)
    # Create BFMatcher object
    bf = cv2.BFMatcher()
    # Match descriptors
    matches = bf.knnMatch(descriptors_original_SIFT, descriptors_distorted_SIFT, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # Extract matched keypoints
    matched_original_SIFT = np.float32([keypoints_original_SIFT[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    matched_distorted_SIFT = np.float32([keypoints_distorted_SIFT[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    # Estimate similarity transform
    tform, inlier_mask = cv2.estimateAffinePartial2D(matched_distorted_SIFT, matched_original_SIFT)

    # Apply transformation to get recovered scale and rotation
    scale_recovered_SIFT = np.sqrt(np.linalg.det(tform[0:2, 0:2]))
    theta_recovered_SIFT = -np.degrees(np.arctan2(tform[0, 1], tform[0, 0]))
    print('SIFT Method')
    # print('Recovered scale:', scale_recovered_SIFT)
    print('Recovered theta:', theta_recovered_SIFT)

    fig, axs = plt.subplots(1, 2, figsize=(15, 5))  

# Display images on the first two subplots
    axs[0].imshow(org_region)
    axs[0].set_title('Original')
    axs[0].axis('off') 

    axs[1].imshow(dist_region)
    axs[1].set_title('Rotated')
    axs[1].axis('off') 
    
    # fig, axes = plt.subplots(1, 2, figsize=(15, 5)) 
    # # Visualize matches on the third subplot
    # plot_matches(axes, original, distorted, keypoints_original, keypoints_distorted, matches)
    # axes.set_title('Matches')
    # axes.axis('off')  # Hide axes for cleaner display
    plt.text(25,50, "Angle Rotated in Degree by ORB "+str(round(theta_recovered,2)) + "\n Angle Rotated in Degree by SIFT Method "+str(round(theta_recovered_SIFT,2)), bbox=dict(fill=False, edgecolor='red', linewidth=2))
    # plt.suptitle('Matching points ORB, Theta: {}'.format(theta_recovered)) 
    fig.tight_layout()
    #Uncomment the below for saving the file
    # import datetime
    # ts = datetime.datetime.now().strftime("%Y%m%d-%H.%M.%S")
    # plt.savefig(f"/home/thanush/Mowito_Output/Temp3/figure-{ts}.png")
    plt.show()

    
# org = cv2.imread('/media/thanush/Misc1/Mowito/Test_images/org.jpg')
# dist = cv2.imread('/media/thanush/Misc1/Mowito/Test_images/dist.jpg')
org = input("Enter full path of the test image")
dist = input("Enter full path of the template image")

#Code to run a set of images
# mylist = os.listdir("/media/thanush/Misc1/Mowito/Test_images/")
# for i in range(4,15):
#     org = "/media/thanush/Misc1/Mowito/Template/screenshot_2024-05-02_17-22-50.jpg" #temp 3
#     dist = "/media/thanush/Misc1/Mowito/Test_images/"+mylist[i]
#     detect_features(org,dist)



