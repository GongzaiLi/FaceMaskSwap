import cv2
PREDICTOR_PATH = "models/shape_predictor_68_face_landmarks.dat"
CASCADE_PATH="models/haarcascade_frontalface_default.xml"
OPENCV_OBJECT_TRACKERS = {
    "kcf": cv2.legacy.TrackerKCF_create,
    "boosting": cv2.legacy.TrackerBoosting_create,
    "mil": cv2.legacy.TrackerMIL_create,
    "tld": cv2.legacy.TrackerTLD_create,
    "medianflow": cv2.legacy.TrackerMedianFlow_create,
    "mosse": cv2.legacy.TrackerMOSSE_create
    
}