import numpy as np
import pandas as pd

# https://www.sentiweb.fr/1023.pdf

# lyme disease

#%%
prevalence = 9 / 100000
# prevalence = 9.3 / 100000
N = 100000
# N = 1000000000

#%%
false_positive_rate = 1 / 100
false_negative_rate = 1 / 100

positive = int(N * prevalence)
negative = N - positive

# true_positive + false_negative = positive
# true_negative + false_positive = negative
# false_positive_rate = false_positive / negative
# false_negative_rate = false_negative / positive

false_positive = int(false_positive_rate * negative)
false_negative = int(false_negative_rate * positive)

true_positive = positive - false_negative
true_negative = negative - false_positive

accuracy = (true_negative + true_positive) / N
chances_of_being_sick_if_tested_positive = true_positive / (true_positive + false_positive)
chances_of_being_sick_if_tested_negative = false_negative / (true_negative + false_negative)

#%%
print(f"accuracy: {100*accuracy:.2f} %")
print(f"positive: {positive}")
print(f"false_positive: {false_positive}")
print(f"chances_of_being_sick_if_tested_positive: {100*chances_of_being_sick_if_tested_positive:.8f} %")
print(f"chances_of_being_sick_if_tested_negative: {100*chances_of_being_sick_if_tested_negative:.8f} %")

#%%
# negative = N
# positive = 0

positive = int(N * prevalence)
negative = N - positive

false_positive = 0
false_negative = positive

true_positive = positive - false_negative
true_negative = negative - false_positive

accuracy = (true_negative + true_positive) / N
chances_of_being_sick_if_tested_positive = true_positive / (true_positive + false_positive)
chances_of_being_sick_if_tested_negative = false_negative / (true_negative + false_negative)

#%%
print(f"accuracy: {100*accuracy:.12f} %")
print(f"chances_of_being_sick_if_tested_positive: {100*chances_of_being_sick_if_tested_positive:.8f} %")
print(f"chances_of_being_sick_if_tested_negative: {100*chances_of_being_sick_if_tested_negative:.8f} %")

# lyme disease

#%%
prevalence = 3 / 100
# prevalence = 9.3 / 100000
N = 100000
# N = 1000000000

#%%
false_positive_rate = 1 / 100
false_negative_rate = 30 / 100

positive = int(N * prevalence)
negative = N - positive

# true_positive + false_negative = positive
# true_negative + false_positive = negative
# false_positive_rate = false_positive / negative
# false_negative_rate = false_negative / positive

false_positive = int(false_positive_rate * negative)
false_negative = int(false_negative_rate * positive)

true_positive = positive - false_negative
true_negative = negative - false_positive

accuracy = (true_negative + true_positive) / N
chances_of_being_sick_if_tested_positive = true_positive / (true_positive + false_positive)
chances_of_being_sick_if_tested_negative = false_negative / (true_negative + false_negative)

#%%
print(f"accuracy: {100*accuracy:.2f} %")
print(f"positive: {positive}")
print(f"true_positive: {true_positive}")
print(f"false_negative: {false_negative}")
print(f"false_positive: {false_positive}")
print(f"true_negative: {true_negative}")
print(f"chances_of_being_sick_if_tested_positive: {100*chances_of_being_sick_if_tested_positive:.8f} %")
print(f"chances_of_being_sick_if_tested_negative: {100*chances_of_being_sick_if_tested_negative:.8f} %")
