import pandas as pd

def load_data():
    modelData = pd.read_csv("data.csv",sep=',',header=0)
    return modelData

def joint_distribution_reduction(modelData:pd.DataFrame,i):
    return modelData[modelData.iloc[:,i] == 1]

def train(modelData: pd.DataFrame):
    print("Training model with following coloumns:\n", modelData.columns)
    mat = pd.DataFrame(columns=['sunny','cloudy','rainy'],index=['sunny','cloudy','rainy'])
    matrix = {}
    i = 0
    for i in range(0,3):
       currentData = joint_distribution_reduction(modelData,i)
       dta = {'sunny':0, 'cloudy':0, 'rainy':0}
       states = ['sunny', 'cloudy', 'rainy']
       for j in range(5, 2,-1):
           data = currentData.iloc[:,j]
           k = 0;
           while k<data.shape[0]:
               if data.iloc[k] == 1:
                dta[states[j-3]] += 1
               k+=1
       total = data.shape[0]
       art = []
       for key, value in dta.items():
           dta[key] = value / total
           art.append(dta[key])
       mat.iloc[:,i] = art
    mat.to_csv("matrix.csv",index=True,header=True,sep=',')

if __name__ == "__main__":
    modelData = load_data()
    train(modelData)
       
       

           
               