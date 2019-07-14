import numpy as np
from numpy import sin
from numpy import cos
from numpy import deg2rad as d2r


def compute_source(ra,dec,lst,lat=13.602997,lon=77.427981):
    '''
    A fuction which computes unit source vector

    Input:
    ------
    ra  - The Right ascension of the object in degrees.
    dec - The declination of the object in degrees.
    lst - The local sidereal time in degrees.
    lat - The latitude of the place of observation.
    lon - The longitude of the place of observation.

    Default for lat and lon is the  coordinates of GBD terrace

    Output:
    ------
    Touple of the form (x,y,z) in NEU coordinates.

    '''
    ha=lst-ra
    if(ha>360):
        ha=ha-360
    if(ha<0):
        ha=ha+360

    sin_dec= sin(d2r(dec))
    sin_lat= sin(d2r(lat))
    cos_dec= cos(d2r(dec))
    cos_lat= cos(d2r(lat))
    cos_ha = cos(d2r(ha))
    sin_ha = sin(d2r(ha))
    sin_alt= sin_dec*sin_lat+cos_dec*cos_lat*cos_ha
    alt = np.rad2deg(np.arcsin(sin_alt))
    cos_alt=cos(d2r(alt))
    cosA=(sin_dec-sin_alt*sin_lat)/(cos_alt*cos_lat)
    A=np.rad2deg(np.arccos(cosA))
    if(sin_ha>0):
        az=360-A
    else:
        az=A

    hor=[alt,az]
    x= cos(hor[0])*cos(hor[1])
    y= cos(hor[0])*sin(hor[1])
    z= sin(hor[0])
    return (x,y,z)

def compute_baseline(org,pnt):
    '''
    A fuction which computes baseline vector in the NEU coordinates

    Input:
    ------
    org - The number of the tile that is considered as the origin or reference
    pnt - The number of the tile that is considered as the origin or reference

    Output:
    ------
    Touple of the form (x,y,z) in NEU coordinates.

    '''
    # The vectors are the coordinates of tiles in the NE coordinates with reference to tile 1 (We assuming that they are in meters)
    b_df=[[0.0,0.0],[-69.9,44.7],[-39.4,66.6],[-39.4,66.6],[-39.4,66.6],[29.3,98.7],[-23.1,32.3],[-14.9,61.3],[-58.6,28.4]]
    l=[a_i - b_i for a_i, b_i in zip(b_df[pnt-1],b_df[org-1])]
    return (l[0],l[1],0)

print("\nScript Running...\n")

def compute_delay(lst,t_org,t_pnt,ra,dec):
    '''
    A fuction which computes the delay in seconds.

    Input:
    ------
    lst - The local sidereal time in degrees.    
    t_org - The number of the tile that is considered as the origin or reference
    t_pnt - The number of the tile that is considered as the origin or reference
    ra  - The Right ascension of the object in degrees.
    dec - The declination of the object in degrees.

    Output:
    ------
    The delay in seconds.

    '''
    bt = np.asarray(compute_baseline(t_org,t_pnt))
    st = np.asarray(compute_source(ra,dec,lst))
    c = 299792458
    return np.dot(bt,st)/c


ra_CasA  =300
dec_CasA =36.466667

print(compute_delay(100,1,2,ra_CasA,dec_CasA))
