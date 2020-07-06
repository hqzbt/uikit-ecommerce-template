import cv2
files = ""

s=210
m=481
l=1200
import os 
root_dir ="./"
fl=[os.path.join(root_dir,x) for x in os.listdir(root_dir) if ".jpg" in x]
def process(img):
    w,h= img.shape[:2]
    ratio = w/float(h)

    ws,hs=  s, int(ratio*s)
    wm,hm=  m, int(ratio*m)
    wl,hl=  l, int(ratio*l)

    img_s=cv2.resize(img,(ws,hs))
    img_l=cv2.resize(img,(wl,hl))
    img_m=cv2.resize(img,(wm,hm))

    return [img_s,img_m,img_l]





print (fl)
os.makedirs("../xxx",  exist_ok=True)
for i, f in enumerate(fl) :
    img = cv2.imread(f)
    
    g1,g2,g3 = process(img)
    cv2.imwrite(f"../xxx/{i}-small.jpg", g1)
    cv2.imwrite(f"../xxx/{i}-medium.jpg", g2)
    cv2.imwrite(f"../xxx/{i}-large.jpg", g3)
