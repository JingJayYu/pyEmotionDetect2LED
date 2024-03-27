import cv2
import threading
from deepface import DeepFace
import serial2ino

font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10, 500)
fontScale = 1
fontColor = (0, 255, 0)
thickness = 1
lineType = 2
cap = cv2.VideoCapture(0)

# use list to communicate in diffrent threads
emotionList = ["init"]
_serial = threading.Thread(target=serial2ino.run, args=(emotionList,))
_serial.start()


def emotion_detect():
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Can't receive frame. Exiting ...")
                break

            try:
                analyze_result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

                #draw rect on faces and calculate each face's area
                face_area = []
                for i in range(len(analyze_result)):
                    x,y,w,h = analyze_result[i]['region']['x'],analyze_result[i]['region']['y'],analyze_result[i]['region']['w'],analyze_result[i]['region']['h']
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
                    face_area.append((x+w)*(y+h))

                #select the biggest face area to output result
                emotion_text = analyze_result[face_area.index(max(face_area))]['dominant_emotion']

                # Define the font and get the width and height of the frame.
                font = cv2.FONT_HERSHEY_SIMPLEX
                frame_height, frame_width = frame.shape[:2]

                # Calculate text width & height to draw the text in the top right corner.
                text_size = cv2.getTextSize(emotion_text, font, 1, 2)[0]
                text_x = frame_width - text_size[0] - 10  # 10 pixels from the right edge.
                text_y = text_size[1] + 10  # 10 pixels from the top.

                # Put the emotion text on the frame.
                cv2.putText(frame, emotion_text, (text_x, text_y), font, 1, (255, 255, 255), 2)
                
                cv2.imshow('Webcam Feed', frame)
                
                emotionList[0] = emotion_text
                print(emotion_text)
            except Exception as e:
                print("Error in emotion detection:", e)

            keypress = cv2.waitKey(30)
            if (keypress == ord('q') or keypress == 27) :
                break
            
    finally:
        cap.release()
        cv2.destroyAllWindows()
    
if (__name__ == "__main__"):
    emotion_detect()