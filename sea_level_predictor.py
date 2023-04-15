import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    plt.scatter(x, y)
    
    # Create first line of best fit
    years_extended = range(x.min(), 2051, 1)
    
    # get slope, intercept from linregress() to plot y' = intercept + slope*x
    slope, intercept, rvalue, pvalue, stderr = linregress(x, y)
    
    # make regression line
    line = [slope*xi + intercept for xi in years_extended]
    
    # plot linear regression line
    plt.plot(years_extended, line, color="red", linewidth=1
    
    # Create second line of best fit
    df2 = df[df['Year']>=2000]
    
    x2 = df2['Year']
    y2 = df2['CSIRO Adjusted Sea Level']

    years_extended2 = range(x2.min(), 2051, 1)
    
    # get slope, intercept from linregress() to plot y' = intercept + slope*x
    slope, intercept, rvalue, pvalue, stderr = linregress(x2, y2)
    
    # make regression line
    line2 = [slope*xi + intercept for xi in years_extended2]
    
    # plot linear regression line
    plt.plot(years_extended2, line2, color="orange", linewidth=1)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
