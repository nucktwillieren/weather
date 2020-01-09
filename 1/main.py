from util import (
    data_field_generator,
    d2_field_generator,
    contour_plot
)
import numpy as np
xnum = 49 ; ynum = 25
fileName = 'output.bin'

with open(fileName, mode='rb') as file:
    a, b, c = 25, 49, 5
    h_data, u_data, v_data, t_data = (
        data_field_generator(file, a, b, c),
        data_field_generator(file, a, b, c),
        data_field_generator(file, a, b, c),
        data_field_generator(file, a, b, c),
    )
    
lons = np.linspace(90, 180, num = 49)
lats = np.linspace(15, 60, num = 25)
lons, lats = np.meshgrid(lons, lats)
latsarr = np.dstack((lats,lats,lats,lats,lats))

latsarrcos = np.cos(latsarr*np.pi/180)
omega=7.2921*10**(-5)
f = 2*omega*np.sin(latsarr*np.pi/180)
dy=6378000*1.875*3.14/180

tx_3, tx_1, ty_3, ty_1 = d2_field_generator(t_data)
ux_3, ux_1, uy_3, uy_1 = d2_field_generator(u_data)
vx_3, vx_1, vy_3, vy_1 = d2_field_generator(v_data)

hor_temp_advection = -u_data*((tx_3-tx_1)/(2*(dy*latsarrcos)))-v_data*((ty_3-ty_1)/(2*dy))
divergence = (ux_3-ux_1)/(2*(dy*latsarrcos))+((vy_3-vy_1)/(2*dy))
relative_vorticity = ((vx_3-vx_1)/(2*(dy*latsarrcos)) - (uy_3-uy_1)/(2*dy))
RV = relative_vorticity + f

rvx_3, rvx_1, rvy_3, rvy_1 = d2_field_generator(RV)

absolute_vorticity_advection = -u_data*((rvx_3-rvx_1)/(2*(dy*latsarrcos)))-v_data*((rvy_3-rvy_1)/(2*dy))

# 300hPa Horizontal temperature advection
contour_plot(lons,lats,hor_temp_advection[:,:,4],'300hPa Horizontal temperature advection','300HTA')

# 500hPa Horizontal temperature advection
contour_plot(lons,lats,hor_temp_advection[:,:,3],'500hPa Horizontal temperature advection','500HTA')

# 700hPa Horizontal temperature advection
contour_plot(lons,lats,hor_temp_advection[:,:,2],'700hPa Horizontal temperature advection','700HTA')

# 850hPa Horizontal temperature advection
contour_plot(lons,lats,hor_temp_advection[:,:,1],'850hPa Horizontal temperature advection','850HTA')

# 1000hPa Horizontal temperature advection
contour_plot(lons,lats,hor_temp_advection[:,:,0],'1000hPa Horizontal temperature advection','1000HTA')

# 300hPa divergence
contour_plot(lons,lats,divergence[:,:,4],'300hPa divergence','300Divergence')

# 500hPa divergence
contour_plot(lons,lats,divergence[:,:,3],'500hPa divergence','500Divergence')

# 700hPa divergence
contour_plot(lons,lats,divergence[:,:,2],'700hPa divergence','700Divergence')

# 850hPa divergence
contour_plot(lons,lats,divergence[:,:,1],'850hPa divergence','850Divergence')

# 1000hPa divergence
contour_plot(lons,lats,divergence[:,:,0],'1000hPa divergence','1000Divergence')

# 300hPa Relative vorticity
contour_plot(lons,lats,relative_vorticity[:,:,4],'300hPa Relative_vorticity','300_Relative_vorticity')

# 500hPa Relative vorticity
contour_plot(lons,lats,relative_vorticity[:,:,4],'500hPa Relative_vorticity','500_Relative_vorticity')

# 700hPa Relative vorticity
contour_plot(lons,lats,relative_vorticity[:,:,4],'700hPa Relative_vorticity','700_Relative_vorticity')

# 850hPa Relative vorticity
contour_plot(lons,lats,relative_vorticity[:,:,4],'850hPa Relative_vorticity','850_Relative_vorticity')

# 1000hPa Relative vorticity
contour_plot(lons,lats,relative_vorticity[:,:,4],'1000hPa Relative_vorticity','1000_Relative_vorticity')

# 300hPa absolute_vorticity_advection
contour_plot(lons,lats,absolute_vorticity_advection[:,:,4],'300hPa Absolute vorticity advection','300_Absolute_vorticity_advection')

# 500hPa absolute_vorticity_advection
contour_plot(lons,lats,absolute_vorticity_advection[:,:,4],'500hPa Absolute vorticity advection','500_Absolute_vorticity_advection')

# 700hPa absolute_vorticity_advection
contour_plot(lons,lats,absolute_vorticity_advection[:,:,4],'700hPa Absolute vorticity advection','700_Absolute_vorticity_advection')

# 850hPa absolute_vorticity_advection
contour_plot(lons,lats,absolute_vorticity_advection[:,:,4],'850hPa Absolute vorticity advection','850_Absolute_vorticity_advection')

# 1000hPa absolute_vorticity_advection
contour_plot(lons,lats,absolute_vorticity_advection[:,:,4],'1000hPa Absolute vorticity advection','1000_Absolute_vorticity_advection')