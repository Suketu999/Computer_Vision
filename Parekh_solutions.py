import cv2

vid = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('HW00.avi',fourcc,30,(640,640))

while True:
    ret, frm = vid.read()
    output.write(frm)
    cv2.imshow('RT',frm)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
output.release()
cv2.destroyAllWindows()
