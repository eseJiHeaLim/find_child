import cv2

videoCapture = cv2.VideoCapture(0)

_, frameNDArray = videoCapture.read()

videoHeight, videoWidth = frameNDArray.shape[:2]

fourcc = cv2.VideoWriter_fourcc(*"DIVX")

videoWriter = cv2.VideoWriter("result.avi", fourcc, 25.0, (videoWidth, videoHeight))

while (videoCapture.isOpened()):

    _, frameNDArray = videoCapture.read()

    videoWriter.write(frameNDArray)

    cv2.imshow("video", frameNDArray)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

videoCapture.release()

videoWriter.release()

cv2.destroyAllWindows()
