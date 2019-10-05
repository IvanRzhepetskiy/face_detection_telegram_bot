import imutils
import cv2
import io

#scans image for faces, if more than 1 face -> return 2, if == 1 return 1, if == 0 return 0
#return -1 if image does not exist


def find_faces(picture):
    faces_in_image_counter = 0
    confidence_given = 0.5
    proto_path = "module/caffee-deep-model/deploy.prototxt"
    model_path = "module/caffee-deep-model/res10_300x300_ssd_iter_140000.caffemodel"
    detector = cv2.dnn.readNetFromCaffe(proto_path, model_path)

    try:
        image = cv2.imread(picture)
    except Exception as e:
        print(e)
        return -1

    image = imutils.resize(image, width=600)
    image_blob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 1.0, (300, 300),
        (104.0, 177.0, 123.0), swapRB=False, crop=False)

    detector.setInput(image_blob)
    detections = detector.forward()

    for i in range(0, detections.shape[2]):

        confidence = detections[0, 0, i, 2]
        # print(confidence)

        if confidence > confidence_given:
            faces_in_image_counter += 1

    if faces_in_image_counter > 1:
        return 2
    elif faces_in_image_counter == 1:
        return 1
    elif faces_in_image_counter == 0:
        return 0


def search_face(face): #send face to findclone.ru, returns tuple (photo, number) 
    pass
