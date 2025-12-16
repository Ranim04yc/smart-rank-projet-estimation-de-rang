"""
Script to generate the pickle model files from the training data.
This script replicates the model training logic from the Jupyter notebook.
"""

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
import pickle
import os

# Create models directory if it doesn't exist
os.makedirs("models", exist_ok=True)

# Load data
print("Loading data from rankdata.xlsm...")
df = pd.read_excel('./rankdata.xlsm')

# Fill missing values with mean
mean = df['avg'].mean()
df.fillna(mean, inplace=True)

# Define average calculation functions
def ai_avg(x):
    en = x['english'] * 1
    math = x['math'] * 2
    soa = x['soa'] * 3
    ai = x['ai'] * 4
    ml = x['ml'] * 2
    se = x['se'] * 3
    return (en + math + soa + ai + ml + se) / 15

def network_avg(x):
    en = x['english'] * 1
    math = x['math'] * 2
    soa = x['soa'] * 2
    ai = x['ai'] * 3
    ml = x['ml'] * 3
    se = x['se'] * 4
    return (en + math + soa + ai + ml + se) / 15

def logic_avg(x):
    en = x['english'] * 1
    math = x['math'] * 2
    soa = x['soa'] * 2
    ai = x['ai'] * 3
    ml = x['ml'] * 4
    se = x['se'] * 3
    return (en + math + soa + ai + ml + se) / 15

def software_avg(x):
    en = x['english'] * 1
    math = x['math'] * 2
    soa = x['soa'] * 2
    ai = x['ai'] * 4
    ml = x['ml'] * 3
    se = x['se'] * 3
    return (en + math + soa + ai + ml + se) / 15

# Calculate averages
print("Calculating averages...")
df['ai_avg'] = df.apply(ai_avg, axis=1)
df['network_avg'] = df.apply(network_avg, axis=1)
df['logic_avg'] = df.apply(logic_avg, axis=1)
df['software_avg'] = df.apply(software_avg, axis=1)

# Prepare training data
print("Preparing training data...")
x_train_ai = df[['avg', 'ai_avg']]
y_train_ai = df[['ai rank']]

x_train_software = df[['avg', 'software_avg']]
y_train_software = df[['software rank']]

x_train_logic = df[['avg', 'logic_avg']]
y_train_logic = df[['logic rank']]

x_train_network = df[['avg', 'network_avg']]
y_train_network = df[['network rank']]

# Train models
print("Training models...")
software_model = KNeighborsRegressor(n_neighbors=11, weights='distance')
software_model.fit(x_train_software.values, y_train_software.values)

ai_model = KNeighborsRegressor(n_neighbors=11, weights='distance')
ai_model.fit(x_train_ai.values, y_train_ai.values)

logic_model = KNeighborsRegressor(n_neighbors=11, weights='distance')
logic_model.fit(x_train_logic.values, y_train_logic.values)

network_model = KNeighborsRegressor(n_neighbors=11, weights='distance')
network_model.fit(x_train_network.values, y_train_network.values)

# Save models
print("Saving models...")
pickle.dump(software_model, open("models/software_model.pickle", "wb"))
pickle.dump(ai_model, open("models/ai_model.pickle", "wb"))
pickle.dump(logic_model, open("models/logic_model.pickle", "wb"))
pickle.dump(network_model, open("models/network_model.pickle", "wb"))

print("Models generated successfully!")
print("Files saved in ./models/ directory:")


