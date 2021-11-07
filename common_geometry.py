

"""
A collection of callable objects whose return values
are X3D elements representing geometry

optional input arguments may be used to specify
an X3D Appearance node to apply to the geometry
"""
import numpy as np
import math
from x3d import x3d

def Sphere( center, radius, appearance=None):
    """returns a sphere with specified radius and center
    
    Args:
    center: a (3,) sequence of (x,y,z) coordinates of sphere center
    radius: a numeric radius
    
    appearance: (optional) Must be an x3d.Appearance instance
        If not supplied, no Appearance node will appear in the x3d Shape
        instances, and X3D specified defaults will be applied by browsers
       
    Returns:
    An x3d.Transform node containing a single x3d.Shape node
    
    """
    
    shape = x3d.Shape( geometry = x3d.Sphere(radius=radius) )
    if appearance is not None:
        shape.appearance = appearance
        
    retVal= x3d.Transform(
            translation=tuple(center),
            children=[shape]
    )
    return retVal


def TiltedPlane(length,width,beta, appearance=None):
    """ returns a rectangle of specified length and width, centered on cone axis, making angle beta with horizontal
    
    Args:
    length : length of rectanle in x axis
    width  : width of rectangle in z axis
    beta   : angle the plane makes with horizontal (x-z plane)
    appearance: (optional) Must be an x3d.Appearance instance
        If not supplied, no Appearance node will appear in the x3d Shape
        instances, and X3D specified defaults will be applied by browsers 
        
    Returns:
    An x3d.Shape node   
    """
    
    
    corners = np.array([
        ( 0.5, 0, 0.5),
        (-0.5, 0, 0.5),
        (-0.5, 0,-0.5),
        ( 0.5, 0,-0.5)
    ]) * np.array((length,1.0,width))
    
    M = np.array([
        ( math.cos(beta),  math.sin(beta) , 0),
        ( -math.sin(beta),  math.cos(beta) , 0),
        ( 0             ,  0              , 1)
    ])
    
    coordinates = np.inner(corners, M)
    coordinates = [ tuple(pt) for pt in coordinates ]
    
    ifs = x3d.IndexedFaceSet()
    ifs.coord = x3d.Coordinate( point= list(coordinates))
    ifs.coordIndex = [0,1,2,3,-1]
    ifs.solid = False
    
    shape = x3d.Shape(geometry = ifs)
    if appearance is not None:
        shape.appearance = appearance
    return x3d.Transform( children=[shape])   
