import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read the data from the CSV file
    df = pd.read_csv('epa-sea-level.csv')

    # Create a scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Actual Data')

    # Get the slope, intercept, r_value, p_value, and std_err of the line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create a line of best fit using the entire dataset
    line_fit = [slope * year + intercept for year in range(1880, 2051)]
    plt.plot(range(1880, 2051), line_fit, label='Line of Best Fit (1880-2050)')

    # Create a line of best fit using data from 2000 onward
    recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    line_fit_recent = [slope_recent * year + intercept_recent for year in range(2000, 2051)]
    plt.plot(range(2000, 2051), line_fit_recent, label='Line of Best Fit (2000-2050)')

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Add legend
    plt.legend()

    # Save and return the plot
    plt.savefig('sea_level_plot.png')
    plt.show()

# Run the function to generate the plot
draw_plot()