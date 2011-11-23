"""
This module contains the functions for calculating the information gain of a
dataset as defined by the ID3 (Information Theoretic) heuristic.
"""

import math

def entropy(vectors, target_component):
    """
    Calculates the entropy of the given data set for the target attribute.
    """
    values = [vector[target_component] for vector in vectors]
    data_entropy = 0.0

    # Calculate the frequency of each of the values in the target attr
    for value in set(values):
        relative_frequency = values.count(value) / len(values)
        data_entropy += -relative_frequency * math.log(relative_frequency), 2)

    return data_entropy
    
def gain(vectors, component, target_component):
    """
    Calculates the information gain (reduction in entropy) that would
    result by splitting the data on the chosen attribute (attr).
    """
    values = [vector[component] for vector in vectors]
    value_frequencies = {}
    subset_entropy = 0.0
        
    # Calculate the sum of the entropy for each subset of records weighted
    # by their probability of occuring in the training set.
    for value in set(values):
        value_frequency = values.count(value) / len(values)
        data_subset = [vector for vector in vectors if vector[component] == value]
        subset_entropy += value_frequency * entropy(data_subset, target_component)

    # Subtract the entropy of the chosen attribute from the entropy of the
    # whole data set with respect to the target attribute (and return it)
    return entropy(vectors, target_component) - subset_entropy
            
