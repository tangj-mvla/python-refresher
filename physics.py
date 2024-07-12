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
