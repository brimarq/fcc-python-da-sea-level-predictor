import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('./epa-sea-level.csv')

    # Create scatter plot
    yrs = df['Year']
    lvls = df['CSIRO Adjusted Sea Level']
    plt.scatter(yrs, lvls)
    plt.xlim(1850, 2075)

    # Create first line of best fit
    line1 = linregress(yrs, lvls)
    yrs_to2050 = yrs.append(pd.Series(range(yrs.max() + 1, 2051)))
    plt.plot(yrs_to2050, line1.intercept + line1.slope * yrs_to2050, color='aqua', label=f'{yrs.min()}-2050')

    # Create second line of best fit
    yrs_from2000 = df[yrs >= 2000]['Year']
    lvls_from2000 = df[yrs >= 2000]['CSIRO Adjusted Sea Level']

    line2 = linregress(yrs_from2000, lvls_from2000)
    yrs_from2000_to2050 = yrs_from2000.append(pd.Series(range(yrs_from2000.max() + 1, 2051)))
    plt.plot(yrs_from2000_to2050, line2.intercept + line2.slope * yrs_from2000_to2050, color='orange', label=f'{yrs_from2000.min()}-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend(title='Trends')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()