# Mathematics-Physics-Simulations
A collection of Python scripts exploring computational physics and mathematical modeling.

### 🌌 Project 1: GraviPlot (Inverse Square Law Simulation)

This script models the gravitational pull between Earth and a satellite as a function of distance.

**The Underlying Physics:**
The simulation is based on Newton's Law of Universal Gravitation:
$$F = G \frac{m_1 m_2}{r^2}$$

**Technical Implementation:**
- **Vectorized Computation:** Uses `NumPy` to calculate forces across 100 data points simultaneously.
- **Data Visualization:** Uses `Matplotlib` to demonstrate the exponential decay of force as the satellite moves into deep space.
- **Real-world Constants:** Uses Earth's mass ($5.972 \times 10^{24}$ kg) and the Gravitational Constant ($6.67430 \times 10^{-11}$).
- 
