import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Constants
mixing_angle = np.radians(33)
mass_squared_difference = 7.5e-5
Length = 500  # Distance in KM

# Function to calculate the oscillation probability
def oscillation_probability(L, E, theta, delta_m):
    return np.sin(2 * theta)**2 * np.sin(1.27 * delta_m * (L / E))**2

# Adjusted Gaussian distribution parameters
mean_energy = 2.5  # Mean energy
sigma_energy = 0.5  # Standard deviation
energies = np.random.normal(mean_energy, sigma_energy, 1000)

# Calculate the probability for each energy
Prob = oscillation_probability(Length, energies, mixing_angle, mass_squared_difference)

# Total number of events
total_events = 500

# Poisson-distributed event counts based on the probability
counts = np.random.poisson(lam=Prob * total_events)

# Plot the histogram
plt.figure()
hist, bins, _ = plt.hist(energies, bins=50, weights=counts, label='Energy', alpha=0.7, density=True)

# Bin centers
bin_centers = 0.5 * (bins[1:] + bins[:-1])

# Gaussian function
def gaussian(x, amp, mean, sigma):
    return amp * np.exp(-0.5 * ((x - mean) / sigma)**2)

# Fit Gaussian using curve_fit
popt, _ = curve_fit(gaussian, bin_centers, hist)

# Plot the fitted Gaussian
plt.plot(bin_centers, gaussian(bin_centers, *popt), 'r-', label='Fitted Gaussian')

# Labels and title
plt.xlabel('Energy (GeV)')
plt.ylabel('Normalized Event Counts')
plt.title('Energy Spectrum with Fitted Gaussian')
plt.legend()
plt.show()

