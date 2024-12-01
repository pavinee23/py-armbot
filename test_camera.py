from picamera2 import Picamera2
import cv2
import numpy as np

def main():
    picam2 = Picamera2()
    picam2.configure(picam2.create_still_configuration())
    picam2.start_preview()
    picam2.start()

    while True:
        frame = picam2.capture_array()
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        cv2.imshow("Armbot Control A00001", frame_bgr)

        ArmbotA00001 = frame_bgr[:2580, :2280]
        hsv = cv2.cvtColor(ArmbotA00001, cv2.COLOR_BGR2HSV)

        lower_yellow = np.array([20, 100, 100])
        upper_yellow = np.array([30, 255, 255])
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        countor = 0
        for cn in contours:
            area = cv2.contourArea(cn)
            if area < 200000 or area > 5800000:
                continue

            (x, y), (w, h), angle = rect = cv2.minAreaRect(cn)
            box = cv2.boxPoints(rect)
            box = np.int0(box)

            cv2.circle(ArmbotA00001, (int(x), int(y)), 3, [0, 0, 255], -1)
            cv2.polylines(ArmbotA00001, [box], True, [0, 255, 0], 2)
            cv2.putText(ArmbotA00001, f"W {round(w*0.415, 1)} cm", (int(x - 30), int(y - 20)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(ArmbotA00001, f"H {round(h*0.415, 1)} cm", (int(x - 30), int(y + 10)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            countor += 1

        cv2.putText(ArmbotA00001, str(countor), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, [0, 0,255], 2, cv2.LINE_AA)
        cv2.imshow("Armbot Control A00001", ArmbotA00001)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    picam2.stop()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
