import matplotlib.pyplot as plt
import numpy as np

def calculate_gravity():
    # Constants
    G = 6.67430e-11  # Universal Gravitational Constant
    m1 = 5.972e24    # Mass of Earth in kg
    m2 = 1000        # Mass of a satellite in kg (Example)

    # Define a range of distances (from Earth's surface to deep space)
    # 6,371km (Earth radius) to 50,000km
    distances = np.linspace(6.371e6, 50e6, 100) 

    # The Math: F = G * (m1 * m2) / r^2
    forces = G * (m1 * m2) / (distances**2)

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(distances / 1000, forces, color='blue', linewidth=2)
    plt.title('Gravitational Force vs. Distance (Inverse Square Law)')
    plt.xlabel('Distance from Earth Center (km)')
    plt.ylabel('Force of Gravity (Newtons)')
    plt.grid(True, linestyle='--', alpha=0.7)
    
    print("Graph generated successfully. Showing the relationship between distance and force.")
    plt.show()

if __name__ == "__main__":
    calculate_gravity()
  
