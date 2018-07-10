
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
try:
    sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
except:
    pass
import cv2
#filename = './SampleVideo.mp4'
outputFile = 'sample_output.avi'
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(outputFile, fourcc, 30.0, (1920, 1080))
#frames = int(cap.get(cv2.CV_CAP_PROP_FRAME_COUNT))
#width  = int(cap.get(cv2.CV_CAP_PROP_FRAME_WIDTH))
#height = int(cap.get(cv2.CV_CAP_PROP_FRAME_HEIGHT))

fig, ax = plt.subplots(1,1)
plt.ion()
plt.show()
width = 1920
countDown = 5
fps = int(cap.get(cv2.CAP_PROP_FPS))
frames = countDown *fps
#Setup a dummy path
x = np.linspace(0,width,frames)
y = x/2. + 100*np.sin(2.*np.pi*x/1200)
start_time = time.time()
time_elapsed = 0
for i in range(frames):
    fig.clf()
    flag, frame = cap.read()

    plt.imshow(frame)
    plt.plot(x,y,'k-', lw=2)
    plt.plot(x[i],y[i],'or')
    plt.show()
    time_elapsed = time.time() - start_time
    print(time_elapsed)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        break
