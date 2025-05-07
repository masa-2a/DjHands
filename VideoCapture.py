import cv2

def CaptureVideo():
    capture = cv2.VideoCapture(0)

    if not capture.isOpened():
        print("Error: Cannot open webcam")
        exit()

    while True:
        success, img = capture.read()
        if not success:
            print("Failed to read frame")
            break
        cv2.imshow('VideoCapture', img)
        yield img

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()
