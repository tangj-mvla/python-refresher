import math

def calculate_buoyancy(V, density_fluid):
    return density_fluid * V * 9.81

def will_it_float(V, mass):
    return (mass/V <= 1000)

def calculate_pressure(depth):
    return depth * 9.81 * 1000

def calculate_acceleration(F, m):
    return F/m

def calculate_angular_acceleration(tau, I):
    return tau/I

def calculate_torque(F_magnitude, F_direction, r):
    return r * F_magnitude * math.sin(math.radians(F_direction))

def calculate_moment_of_inertia(m ,r):
    return m * r * r

def calculate_auv_acceleration(F_magnitude, F_angle, mass = 100, volume = 0.1, thruster_distance = 0.5):
    force = F_magnitude * math.cos(math.radians(F_angle))
    return calculate_acceleration(force, mass)

def calculate_auv_angular_acceleration(F_magnitude, F_angle, inertia = 1, thruster_distance = 0.5):
    tau = calculate_torque(F_magnitude, F_angle, thruster_distance)
    return calculate_angular_acceleration(tau, inertia)

def calculate_auv2_acceleration(T, alpha, theta, mass = 100):
    a1 = calculate_acceleration(T[0],alpha,mass)
    a2 = calculate_acceleration(T[1],alpha,mass)
    a3 = calculate_acceleration(T[2],alpha,mass)
    a4 = calculate_acceleration(T[3],alpha,mass)
    return a1 + a2 - a3 - a4

def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia = 100):
    distance = np.sqrt(L**2, l**2)
    t1 = distance * T[0] * np.sin(alpha)
    t2 = distance * T[1] * np.sin(alpha)
    t3 = distance * T[2] * np.sin(alpha)
    t4 = distance * T[3] * np.sin(alpha)
    return (t1 + t3 - t2 -t4)/inertia
    
def simulate_auv2_motion(T, alpha, L, l, mass = 100, inertia = 100, dt = 0.1, t_final = 10, x0 = 0, y0 = 0, theta0 = 0):
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
    