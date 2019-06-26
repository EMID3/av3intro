import cv2

img = cv2.imread("mdfoto.jpeg", cv2.IMREAD_COLOR)

stylization = cv2.stylization(img)

cv2.imshow('mdfoto2', stylization)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("mdfoto_result.png", stylization)
