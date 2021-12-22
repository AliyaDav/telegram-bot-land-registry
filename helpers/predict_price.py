import pickle
import pandas as pd
import numpy as np
from sklearn.base import TransformerMixin

def predict(surface, rooms, floor):

    filename = 'hgbr_final.pickle'
    hgbr = pickle.load(open(filename, 'rb'))

    test = pd.DataFrame(data={'Surface' : [int(surface)], 'Rooms' : str(rooms), 'Floor' : str(floor)})
    
    return int(np.exp(hgbr.predict(test)))

class DenseTransformer(TransformerMixin):

    def fit(self, X, y=None, **fit_params):
            return self

    def transform(self, X, y=None, **fit_params):
            return X.todense()