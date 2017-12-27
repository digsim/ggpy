from ggplot import *

print(powerconsumption.head())
print(powerconsumption.dtypes)

o = ggplot(aes(x='Timestamp', y='Watt'), data=powerconsumption)
#o = o + geom_point() + geom_line()
o = o + stat_smooth(color='blue', method='loess', se=False, span=0.01, fit=True)
o = o + scale_x_date(labels=date_format("%Y-%m-%d\n %H:%M:%S"))

print(o)
