import cv2

img = cv2.imread("C:/Users/michael/Downloads/PRO-104-Reference-Code-main/PRO-104-Reference-Code-main/c104/solar-system.jpg")

#rocket = img[120:360,400:500]

#img[0:240, 500:600] = rocket

cv2.putText(img,
          "Sun", 
          (50,100), 
          cv2.FONT_HERSHEY_COMPLEX, 
          1, 
          (200,255,255)
          )
cv2.putText(img,
          "Mercury", 
          (110,290), 
          cv2.FONT_HERSHEY_COMPLEX, 
          0.5, 
          (255,255,255)
          )
cv2.putText(img,
          "Venus", 
          (190,290), 
          cv2.FONT_HERSHEY_COMPLEX, 
          0.5, 
          (255,0,255)
          )
cv2.putText(img,
          "Earth", 
          (275,290), 
          cv2.FONT_HERSHEY_COMPLEX, 
          0.5, 
          (0,255,255)
          )
cv2.putText(img,
          "Mars", 
          (400,290), 
          cv2.FONT_HERSHEY_COMPLEX, 
          0.5, 
          (255,255,0)
          )
cv2.putText(img,
          "Jupiter", 
          (600,400), 
          cv2.FONT_HERSHEY_COMPLEX, 
          0.5, 
          (255,0,0)
          )
cv2.putText(img,
          "Saturn", 
          (800,350), 
          cv2.FONT_HERSHEY_COMPLEX, 
          0.5, 
          (0,0,255)
          )
cv2.putText(img,
          "Uranus", 
          (950,350), 
          cv2.FONT_HERSHEY_COMPLEX, 
          0.5, 
          (0,255,0)
          )
cv2.putText(img,
          "Neptune", 
          (1100,350), 
          cv2.FONT_HERSHEY_COMPLEX, 
          0.5, 
          (200,200,200)
          )





cv2.imshow("output",img)
cv2.imwrite("Solar_systemwithname.jpg",img)

cv2.waitKey(0)
