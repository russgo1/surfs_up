# Surfs Up Analysis

## Overview

### Purpose
The purpose of this analysis is to ensure suitable weather conditions for the viability of a surf and ice cream shop in Hawaii. Here, weather statistics from an SQLite database are gathered into two data frames which summarize temperature data gathered in the months of June and December, respectively. It is helpful to visualize these statistics side-by-side:

<p float="left">
  <img width="138" alt="June_summary" src="https://user-images.githubusercontent.com/114126935/205467293-0a06c8dc-94bb-413a-a012-1a1cbc00e533.png" />
  <img width="166" alt="December_summary" src="https://user-images.githubusercontent.com/114126935/205467296-7e895f0e-0e76-4e81-8806-33733f655a93.png" />
</p>

## Results

### Key differences
- June is warmer than December, as demonstrated by its higher mean, median (“50%”), min, and max temperatures. 

- June’s temperatures are more consistent than December’s temperatures, with a lower standard deviation (“std”) and interquartile range (IQR). The IQR is calculated by subtracting the “25%” statistic from the “75%” statistic. This puts June’s IQR at 4 and December’s at 5.  

- December temperatures span a wider range than June temperatures. December temperatures range from 56 to 83 degrees, a range of 27 degrees. June temperatures range 64 to 85 degrees, a smaller range of only 21 degrees. 

## Summary

### Results
June and December have very consistent temperatures, both with standard deviations between only 3 and 4 degrees. This means that most days in either month will be in the high 60’s to high 70’s. This type of consistent, predictable weather is good for business. 

On the other hand, the data for both months present outliers towards the lower and higher ends of the respective datasets. Using this data, we can define an outlier in two different ways, 

1. As being three standard deviations above or below the mean, or
2. As being 1.5(IQR) below the first quartile or above the third quartile. 

Both the min and max temperatures for the months of June and December are outliers, regardless of which method you chose. This suggests the presence of extreme weather. 

### Further research
Outliers may suggest extreme weather. Unusually cold and warm days should be examined to analyze the risk of potentially devastating weather. A query such as the following would let us know if extreme precipitation accompanied unusually warm days in December,
`session.query(Measurement.tobs, Measurement.prcp).filter(func.strftime("%m",Measurement.date) == "12")\
                .filter(Measurement.tobs < 80).all()`

Precipitation would be good to know about anyway. If it’s just too rainy, our shop may never become a popular destination. The following query will let us know how many June days saw an inch or more of rain and the temperature on those days,
`session.query(Measurement.tobs, Measurement.prcp).filter(func.strftime("%m",Measurement.date) == "06")\
                .filter(Measurement.prcp >= 1).all()`
