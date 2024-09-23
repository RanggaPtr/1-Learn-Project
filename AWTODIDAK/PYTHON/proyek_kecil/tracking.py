import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

# mengakses kamera laptop
video = cv2.VideoCapture(0)

# membuat loop
while True:
    # mengambil frame dari kamera / unpack untuk dijadikan frame
    ret, frame = video.read()

    # menambahkan label kotak mengambil object dari frame yang sudah dikonversi sebelumnya
    bbbox, label, conf = cv.detect_common_objects(frame)

    # menambahkan label kotak yang sebelumnya sudah diambil dari frame
    output_image = draw_bbox(frame, bbbox, label, conf)

    # nama di aplikasinya
    cv2.imshow('Object Detection', output_image)

    # keluar dari loop ketika tombol q ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# membersihkan jendela
video.release()
cv2.destroyAllWindows()
