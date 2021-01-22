# A file for keeping track of scripts that may be useful for reference later.

"""
for widget in self.horizontalLayout_5.children():
                    if isinstance(widget, QCheckBox):
                        print("checkBox: %s  - %s" % (widget.objectName(), widget.checkState()))
"""

"""
# calculate dispersion metrics for each hour
iqr_fifty = []
iqr_eighty = []
iqr_hundred = []
median = []

for hour_in_day, list_of_glucose_values in glucose_grouped_by_hour_in_day.items():
    if not list_of_glucose_values:
        iqr_fifty.append(0)
        iqr_eighty.append(0)
        iqr_hundred.append(0)
        median.append(0)
    else:
        iqr_fifty.append(iqr(list_of_glucose_values, interpolation='midpoint'))
        iqr_eighty.append(
            iqr(list_of_glucose_values, rng=(10, 90), interpolation='midpoint'))
        iqr_hundred.append(
            iqr(list_of_glucose_values, rng=(0, 100), interpolation='midpoint'))
        median.append(np.median(list_of_glucose_values))

print()
for val in iqr_fifty:
    print(val)
print()
for val in iqr_eighty:
    print(val)
print()
for val in iqr_hundred:
    print(val)
print()
for val in median:
    print(val)
print()

return iqr_fifty, iqr_eighty, iqr_hundred, median
"""
