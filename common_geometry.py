

"""
A collection of callable objects whose return values
are X3D elements representing geometry

optional input arguments may be used to specify
an X3D Appearance node to apply to the geometry
"""

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
    An instance from x3d package representing an X3D node.
    
    """
    
    shape = x3d.Shape( geometry = x3d.Sphere(radius=radius) )
    if appearance is not None:
        shape.appearance = appearance
        
    retVal= x3d.Transform(
            translation=tuple(center),
            children=[shape]
    )
    return retVal
