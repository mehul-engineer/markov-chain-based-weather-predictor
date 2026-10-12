import numpy as np
import pandas as pd
from train import load_data,train

def load_matrix():
    matrix = pd.read_csv("matrix.csv",sep=',',header=0,index_col=0)
    return matrix.to_numpy()

def predict_weather(matrix: np.ndarray, current_weather: np.ndarray,noOfDays:int):
    current_weather = current_weather.reshape(3,1)
    lst = []
    for i in range(noOfDays):
        pred = matrix @ current_weather
        if(pred == current_weather).all():
            break
        lst.append(pred)
        current_weather = pred
    out = []
    for item in lst:
        max = item[0]
        ind = 0
        for i in range(0,3):
            if(item[i] > max):
                max = item[i]
                ind = i
        if(ind == 0):
            out.append("sunny")
        elif(ind == 1):
            out.append("cloudy")
        else:
            out.append("rainy")

    return out

if __name__ == "__main__":
    train(load_data())
    lst = predict_weather(load_matrix(),np.array([0,1,0]),100)
    for item in lst:
        print(f"{item},")  



