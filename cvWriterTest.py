
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import time
import sys

import cv2


def fig2data(fig):
    """
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    # draw the renderer
    fig.canvas.draw()

    # Get the RGBA buffer from the figure
    w, h = fig.canvas.get_width_height()
    buf = np.fromstring(fig.canvas.tostring_argb(), dtype=np.uint8)
    buf.shape = (w, h, 4)

    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = np.roll(buf, 3, axis=2)
    return buf

outputFile = 'sample_output.avi'
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(outputFile, fourcc, 30.0, (640, 480))
#frames = int(cap.get(cv2.CV_CAP_PROP_FRAME_COUNT))
#width  = int(cap.get(cv2.CV_CAP_PROP_FRAME_WIDTH))
#height = int(cap.get(cv2.CV_CAP_PROP_FRAME_HEIGHT))

fig = Figure()
fig.set_rasterized(True)
canvas = FigureCanvas(fig)
ax1 = fig.add_subplot(2,2,4)
ax2 = fig.add_subplot(2,2,3)
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
    flag, frame = cap.read()

    ax1.plot(x,y,'k-', lw=2)
    ax2.plot(x[i],y[i],'or')
    fig.tight_layout()
    image = fig2data(fig)
    image = cv2.resize(image,(640,480))
    image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)
    cv2.imshow('graph',image)
    out.write(image)
    time_elapsed = time.time() - start_time
    print(time_elapsed)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
