"""
This module holds functions that are responsible for creating a new
decision tree and for using the tree for data classificiation.
"""

from table import Table

class DecisionTree():
    def __init__(self, table, target_column, fitness_func):
        self.table = table
        self.target_component = target_column
        self.fitness_func = fitness_func
        self.tree = None

    def build(self):
        '''Build the decision tree.'''
        target_values = self.table.select(self.target_column)

        if not self.table:
            return None
        elif len(set(target_values)) == 1:
            return target_values[0]
        else:
            splitting_column = self.choose_column()

            if splitting_column is None:
                return sample_analysis.mode(target_values) #Could be average or median for continuous data
            else:
                self.tree = {'splitting_column': splitting_column}
                #Could be a problem on big data
                splits = {}
                for row in self.table.get_rows():
                    try:
                        splits[row[splitting_column]].append(row)
                    except:
                        splits[row[splitting_column]] = [row]
                for split in splits:
                    subtree = DecisionTree(Table(splits[split]), self.target_column, self.fitness_func)
                    self.tree[split] = subtree

    def choose_column(self, significance=0.0):
        '''Get the attribute with the highest information gain.'''
        best_gain = 0.0
        best_column = None

        for column in self.table.columns:
            gain = fitness_func(vectors, attribute, target_attribute)
            if gain > best_gain:
                best_gain = gain
                best_column = column

        if best_gain > significance: #Chosen for significance
            return best_column
        else:
            return None


