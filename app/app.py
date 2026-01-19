import tkinter.messagebox
import cv2
import numpy as np
from tensorflow import keras    

canvas = np.zeros((331, 280, 3), dtype=np.uint8)
drawing = False
trashcan = cv2.imread("app/trashcan.png")
trashcan = cv2.resize(trashcan,(50,50))
clear = False
model = keras.models.load_model("model/CNN_model.keras")
def draw(event, x, y, flags, param):
    global drawing, last_x, last_y, clear, img28
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        last_x, last_y = x, y
        if x >= 230 and y >= 281:
            clear = True
        elif x <= 90 and y >= 281:
            prediction = model.predict(img28.astype("float32").reshape(1,28,28,1))
            result = np.where(prediction[0] == max(prediction[0]))[0][0]
            print(f"Prediction : {result}")
            tkinter.messagebox.showinfo(title="Result",message=f"Prediction : {result}")

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing and not y > 270:
            cv2.line(canvas, (last_x, last_y), (x, y), (255,255,255), 15)
            last_x, last_y = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        
cv2.namedWindow("Digit Recognition")
cv2.setMouseCallback("Digit Recognition", draw)

while True:
    if clear == True:
        canvas[0:280,0:280] = 0
        clear = False
    cv2.rectangle(canvas, (0,281),(90,330),(255,255,255))
    cv2.imshow("Digit Recognition", canvas)
    predict_txt = cv2.putText(canvas,"Predict",(0,310),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
    cv2.imshow("Digit Recognition",predict_txt) 
    canvas[281:331,230:280] = trashcan 
    cv2.line(canvas,(0,281),(280,281),(255,255,255),1)
    gray = cv2.cvtColor(canvas[0:280,0:280],cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    img140 = cv2.resize(blur,(140,140),interpolation=cv2.INTER_AREA)
    img28 = cv2.resize(img140,(28,28),interpolation=cv2.INTER_AREA)
    if cv2.waitKey(1) == ord("q"): 
        break
cv2.destroyAllWindows()