import math

def calculate_buoyancy(V, density_fluid):
    '''
    calculates buoyancy force

    V: Volume of object in cubic meters
    density_fluid: density of fluid in kg/m^3
    '''
    if (V <= 0): return "Volume Error"
    if (density_fluid <= 0): return "Density Error"
    return density_fluid * V * 9.81

def will_it_float(V, mass):
    '''
    determines whether an object will float or sink in water

    V: the volume of the object in cubic meters
    mass: the mass of the object in kilograms
    '''
    if (V <= 0): return "Volume Error"
    if (mass <= 0): return "Mass Error"
    return mass/V < 1000

def calculate_pressure(depth):
    '''
    calculates the pressure at a given depth in water

    depth: the depth in meters
    '''
    if (depth < 0): return "Depth Error"
    return depth * 9.81 * 1000

def calculate_acceleration(F, m):
    '''
    calculates the acceleration of an object given the force applied to it and its mass

    F: the force applied to the object in Newtons
    m: the mass of the object in kilograms
    '''
    if (m <= 0): return "Mass Error"
    return F/m

def calculate_angular_acceleration(tau, I):
    '''
    calculates the angular acceleration of an object given the torque applied to it and its moment of inertia

    tau: the torque applied to the object in Newton-meters
    I: the moment of inertia of the object in kg * m^2
    '''
    if (I <= 0): return "Inertia Error"
    return tau/I

def calculate_torque(F_magnitude, F_direction, r):
    '''
    calculates the torque applied to an object given the force applied to it
    and the distance from the axis of rotation to the point where the force is applied

    F_magnitude: the magnitude of force applied to the object in Newtons
    F_direction: the direction of the force applied to the object in degrees
    r: the distance from the axis of rotation to the point where the force is applied in meters
    '''
    return r * F_magnitude * math.sin(math.radians(F_direction))

def calculate_moment_of_inertia(m ,r):
    '''
    calculates the moment of inertia of an object given its mass
    and the distance from the axis of rotation to the center of mass of the object

    m: the mass of the object in kilograms
    r: the distance from the axis of rotation to the center of mass of the object in meters
    '''
    return m * r * r

def calculate_auv_acceleration(F_magnitude, F_angle, mass = 100, volume = 0.1, thruster_distance = 0.5):
    '''
    calculates the acceleration of the AUV in the 2D plane

    F_magnitude: the magnitude of force applied by the thruster in Newtons
    F_angle: the angle of the force applied by the thruster in radians
    mass: the mass of the AUV in kilograms. The default value is 100 kg
    volume: the volume of the AUV in cubic meters. The default value is 0.1 m^3
    thruster_distance: the distance from the center of mass of the AUV to the thruster in meters. The default value is 0.5 m
    '''
    force = F_magnitude * math.cos(math.radians(F_angle))
    return calculate_acceleration(force, mass)

def calculate_auv_angular_acceleration(F_magnitude, F_angle, inertia = 1, thruster_distance = 0.5):
    '''
    calculates the angular acceleration of the AUV

    F_magnitude: the magnitude of force applied by the thruster in Newtons
    F_angle: the angle of the force applied by the thruster in radians
    inertia: the moment of inertia of the AUV in kg * m^3. Default is 1 kg * m^3
    thruster_distance: the distance from the center of mass of the AUV to the thruster in meters. The default value is 0.5 m
    '''
    tau = calculate_torque(F_magnitude, F_angle, thruster_distance)
    return calculate_angular_acceleration(tau, inertia)

def calculate_auv2_acceleration(T, alpha, theta, mass = 100):
    '''
    calculates the acceleration of the AUV in the 2D plane

    T: an np.ndarray of the magnitudes of the forces applied by the thrusters in Newtons
    alpha: the angle of the thrusters in radians
    theta: the angle of the AUV in radians
    mass: the mass of the AUV in kilograms. The default value is 100 kg
    '''
    a1 = calculate_acceleration(T[0],alpha,mass)
    a2 = calculate_acceleration(T[1],alpha,mass)
    a3 = calculate_acceleration(T[2],alpha,mass)
    a4 = calculate_acceleration(T[3],alpha,mass)
    return a1 + a2 - a3 - a4

def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia = 100):
    '''
    calculates the angular acceleration of the AUV

    T: an np.ndarray of the magnitudes of the forces applied by the thrusters in Newtons
    alpha: the angle of the thrusters in radians
    L: the distance from the center of mass of the AUV to the thrusters in meters
    l: the distance from the center of mass of the AUV to the thrusters in meters
    inertia: the moment of inertia of the AUV in kg * m^3. The default value is 100 kg * m^3
    '''
    distance = np.sqrt(L**2, l**2)
    t1 = distance * T[0] * np.sin(alpha)
    t2 = distance * T[1] * np.sin(alpha)
    t3 = distance * T[2] * np.sin(alpha)
    t4 = distance * T[3] * np.sin(alpha)
    return (t1 + t3 - t2 -t4)/inertia
    
def simulate_auv2_motion(T, alpha, L, l, mass = 100, inertia = 100, dt = 0.1, t_final = 10, x0 = 0, y0 = 0, theta0 = 0):
    '''
    simulates the motion of the AUV in the 2D plane

    T: an np.ndarray of the magnitudes of the forces applied by the thrusters in Newtons
    alpha: the angle of the thrusters in radians
    L: the distance from the center of mass of the AUV to the thrusters in meters
    l: the distance from the center of mass of the AUV to the thrusters in meters
    mass: the mass of the AUV in kilograms. The default value is 100 kg
    inertia: the moment of inertia of the AUV in kg * m^2. The default value is 100 kg * m^2
    dt: the time step of the simulation in seconds. The default value is 0.1 s
    t_final: the final time of the simulation in seconds. The default value is 10 s
    x0: the initial x-position of the AUV in meters. The default value is 0 m
    y0: the initial y-position of the AUV in meters. The default value is 0 m
    theta0: the initial angle of the AUV in radians. The default value is 0 rad
    '''
    alpha = math.pi/180 * alpha
    t = np.arange(0,t_final+dt,dt)
    moment_arm = np.sqrt(l**2+L**2)
    net_torque = moment_arm*np.sin(alpha)*(T[0]+T[2]-T[1]-T[3])
    theta = t**2 + 1/2 * net_torque/inertia + theta0
    print (theta)

    horizontal = np.sin(math.pi/2-alpha+theta)*(T[0] + T[1] - T[2] - T[3])/mass
    vertical = np.cos(math.pi/2-alpha+theta)*(T[0] + T[1] - T[2] - T[3])/mass
    a = np.sqrt(horizontal**2 + vertical**2)

    hv = np.array([sum(horizontal[:1])]) * dt for i in range(len(horizontal))
    vv = np.array([sum(vertical[:1])]) * dt for i in rnage(len(vertical))
    v = np.sqrt(hv**2 + vv**2)

    x = x0 + np.array([sum(hv[:1])]) * dt for i in range(len(hv))
    y = y0 + np.array([sum(vv[:1])]) * dt for i in rnage(len(vv))
