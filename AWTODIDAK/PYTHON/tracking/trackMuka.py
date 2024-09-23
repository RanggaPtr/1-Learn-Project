import cv2
import numpy as np

# Muat model deteksi wajah dan mata
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Buka kamera
cap = cv2.VideoCapture(0)

# Tentukan codec dan buat objek VideoWriter untuk menyimpan video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    # Baca frame dari kamera
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Konversi frame ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Histogram equalization untuk meningkatkan kontras
    gray = cv2.equalizeHist(gray)
    
    # Deteksi wajah di frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Gambar kotak di sekitar wajah yang terdeteksi
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Region of interest (ROI) untuk mata
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        
        # Deteksi mata dalam wajah
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    
    # Konversi frame ke HSV untuk deteksi kulit
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Tentukan rentang warna kulit dalam HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    
    # Threshold HSV gambar untuk mendapatkan warna kulit saja
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    
    # Aplikasikan filter median untuk mengurangi noise
    mask = cv2.medianBlur(mask, 5)
    
    # Temukan kontur di dalam mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Lanjutkan jika ada kontur yang ditemukan
    if contours:
        # Kontur terbesar dianggap sebagai tangan
        max_contour = max(contours, key=cv2.contourArea)
        
        # Pastikan kontur terbesar cukup besar
        if cv2.contourArea(max_contour) > 1000:
            # Dapatkan hull dan defect dari kontur terbesar
            hull = cv2.convexHull(max_contour, returnPoints=False)
            defects = cv2.convexityDefects(max_contour, hull)
            
            if defects is not None:
                count_defects = 0
                
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(max_contour[s][0])
                    end = tuple(max_contour[e][0])
                    far = tuple(max_contour[f][0])
                    
                    # Hitung jarak antar titik untuk menentukan jumlah jari
                    a = np.linalg.norm(np.array(start) - np.array(end))
                    b = np.linalg.norm(np.array(start) - np.array(far))
                    c = np.linalg.norm(np.array(end) - np.array(far))
                    angle = np.arccos((b**2 + c**2 - a**2) / (2 * b * c)) * 180 / np.pi
                    
                    # Jika sudut antara defect kurang dari 90 derajat, hitung sebagai jari
                    if angle <= 90:
                        count_defects += 1
                        cv2.circle(frame, far, 5, (0, 0, 255), -1)
                        cv2.line(frame, start, end, (0, 255, 0), 2)
                        cv2.line(frame, start, far, (0, 255, 0), 2)
                        cv2.line(frame, end, far, (0, 255, 0), 2)
                
                # Tampilkan jumlah jari yang terdeteksi
                text = ""
                if count_defects == 0:
                    text = "1 Finger"
                elif count_defects == 1:
                    text = "2 Fingers"
                elif count_defects == 2:
                    text = "3 Fingers"
                elif count_defects == 3:
                    text = "4 Fingers"
                elif count_defects == 4:
                    text = "5 Fingers"
                cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    # Tampilkan frame
    cv2.imshow('Face, Eye and Gesture Tracker', frame)
    
    # Simpan frame ke video
    out.write(frame)
    
    # Tekan 'q' untuk keluar dari loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lepaskan kamera, writer dan tutup jendela
cap.release()
out.release()
cv2.destroyAllWindows()
