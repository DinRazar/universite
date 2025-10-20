
import math
from .utils import deg_to_rad, rad_to_deg

def cartesian_to_spherical(x, y, z, to_degrees=True):
    """
    Преобразует декартовы координаты в сферические
    
    Args:
        x, y, z: декартовы координаты
        to_degrees: если True, возвращает углы в градусах
    
    Returns:
        tuple: (r, theta, phi)
    """
    r = math.sqrt(x**2 + y**2 + z**2)
    
    theta = math.atan2(y, x)
    
    if r == 0:
        phi = 0
    else:
        phi = math.acos(z / r)
    
    if to_degrees:
        theta = rad_to_deg(theta)
        phi = rad_to_deg(phi)
    
    return r, theta, phi

def spherical_to_cartesian(r, theta, phi, from_degrees=True):
    """
    Преобразует сферические координаты в декартовы
    
    Args:
        r: радиус
        theta: азимутальный угол
        phi: полярный угол
        from_degrees: если True, углы заданы в градусах
    
    Returns:
        tuple: (x, y, z)
    """
    if from_degrees:
        theta = deg_to_rad(theta)
        phi = deg_to_rad(phi)
    
    x = r * math.sin(phi) * math.cos(theta)
    y = r * math.sin(phi) * math.sin(theta)
    z = r * math.cos(phi)
    
    return x, y, z
