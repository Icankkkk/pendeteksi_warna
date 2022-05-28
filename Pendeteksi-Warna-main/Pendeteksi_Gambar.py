#memasukan Library

import cv2
import pandas as pd

# --------------------------------------------------------------------------

#memasukan alamat data
csv_path = 'Data/colors.csv'

#declaring global variables
r = g = b = xpos = ypos = 0

# reading csv file
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv(csv_path, names=index, header=None)

def Playgambar(file):
    
    # reading image
    img = cv2.imread(file['gambar1'])
    img = cv2.resize(img, (900,600))

    #function to calculate minimum distance from all colors and get the most matching color
    def get_color_name(r,g,b):
            minimum = 1000
            for i in range(len(df)):
                    d = abs(r - int(df.loc[i,'R'])) + abs(g - int(df.loc[i,'G'])) + abs(b - int(df.loc[i,'B']))
                    if d <= minimum:
                            minimum = d
                            cname = df.loc[i, 'color_name'] + "Hex" + df.loc[i, "hex"]
            return cname

    #function to get x,y coordinates of mouse double click
    def identify_color(event, x, y, flags, params):
            global b, g, r, xpos, ypos
            if event == cv2.EVENT_LBUTTONDBLCLK:
                    xpos = x
                    ypos = y
                    b,g,r = img[y,x]
                    b = int(b)
                    g = int(g)
                    r = int(r)


    # creating window
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', identify_color)
    while True:
        cv2.imshow('image', img)
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (600,60), (b,g,r), -1)

        #Creating text string to display( Color name and RGB values )
        text = get_color_name(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
            
        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
                

        if cv2.waitKey(1) & 0xFF ==ord("q"):
            cv2.destroyAllWindows()
            break


