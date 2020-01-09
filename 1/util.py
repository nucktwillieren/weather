from mpl_toolkits.basemap import Basemap, shiftgrid
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import struct
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def data_field_generator(file_stream, a, b, c):
    payload = np.zeros((a,b,c))
    for k in range(c):
        for i in range(a):
            for j in range(b):
                value = file_stream.read(4)
                float_value = struct.unpack("f", value)[0]
                payload[i][j][k] = float_value

    return payload

def d2_field_generator(data_array):
    x_3 = np.append(data_array[:,1:2,:]*2,data_array[:,2:49,:],axis = 1)
    x_3 = np.append(x_3,data_array[:,48:49,:]*2,axis = 1)
    x_1 = np.append(data_array[:,0:1,:]*2,data_array[:,0:47,:],axis = 1)
    x_1 = np.append(x_1,data_array[:,47:48,:]*2,axis = 1)
    y_3 = np.append(data_array[1:2,:,:]*2,data_array[2:25,:,:],axis = 0)
    y_3 = np.append(y_3,data_array[24:25,:,:]*2,axis = 0)
    y_1 = np.append(data_array[0:1,:,:]*2,data_array[0:23,:,:],axis = 0)
    y_1 = np.append(y_1,data_array[23:24,:,:]*2,axis = 0)

    return x_3, x_1, y_3, y_1

def get_hor_temp_advection():
    pass

def contour_plot(x,y,value,title,filename):
    fig = plt.figure(figsize=(16,10))
    canvas = FigureCanvas(fig)
    m = Basemap(projection='cyl',llcrnrlat=15,urcrnrlat=60,llcrnrlon=90,urcrnrlon=180)
    # make a filled contour plot.
    CS1 = m.contour(x,y,value,linewidths=0.5,colors='k',levels=10)
    CS2 = m.contourf(x,y,value,CS1.levels,cmap=plt.cm.jet,extend='both')
    m.colorbar(CS2,pad='10%') # draw colorbar
    # draw coastlines and political boundaries.
    m.drawcoastlines()
    m.drawmapboundary()
    # draw parallels and meridians.
    parallels = np.arange(0.,80,5.)
    m.drawparallels(parallels,labels=[1,0,0,0])
    meridians = np.arange(10.,360.,10.)
    m.drawmeridians(meridians,labels=[0,0,0,1])
    plt.title(title, y=1.075)
    canvas.print_figure(filename,dpi=300)