import cv2
from Pendeteksi_Video import df

#function to calculate minimum distance from all colors and get the most matching color
def get_color_name(r,g,b):
    minimum = 1000
    for i in range(len(df)):
        d = abs(r - int(df.loc[i,'R'])) + abs(g - int(df.loc[i,'G'])) + abs(b - int(df.loc[i,'B']))
        if d <= minimum:
            minimum = d
            cname = df.loc[i, 'color_name']
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

