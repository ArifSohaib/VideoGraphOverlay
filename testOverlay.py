
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
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
out = cv2.VideoWriter(outputFile, fourcc, 30.0, (640, 480))
#frames = int(cap.get(cv2.CV_CAP_PROP_FRAME_COUNT))
#width  = int(cap.get(cv2.CV_CAP_PROP_FRAME_WIDTH))
#height = int(cap.get(cv2.CV_CAP_PROP_FRAME_HEIGHT))

fig = plt.figure()
canvas = FigureCanvas(fig)
ax1 = fig.add_subplot(2,2,4)
ax2 = fig.add_subplot(2,2,3)
plt.ion()
plt.show()
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = int(cap.get(cv2.CAP_PROP_FPS))
print("Recording at width: {}, width: {}, fps: {}".format(width, height, fps))
countDown = 5

frames = countDown *fps
#Setup a dummy path
x = np.linspace(0,width,frames)
y = x/2. + 100*np.sin(2.*np.pi*x/1200)
start_time = time.time()
time_elapsed = 0
for i in range(frames):
    fig.clf()
    # flag, frame = cap.read()

    # plt.imshow(frame)
    ax1.plot(x,y,'k-', lw=2)
    ax2.plot(x[i],y[i],'or')
    canvas.draw()
    image = np.fromstring(canvas.tostring_rgb(), dtype='uint8')
    image = np.reshape(image, (480,640,3))
    out.write(image)
    time_elapsed = time.time() - start_time
    print(time_elapsed)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
