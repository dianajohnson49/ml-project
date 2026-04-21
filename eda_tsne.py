import numpy as np
import pandas as pd
import os
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def readData(datafile):
    # get the current directory: directory name for the abs path of the curr file
    dirpath = os.getcwd()
    abspath = dirpath + "\\" + datafile

    # read data into a pandas dataframe. data file is comma separated so use read_csv
    df = pd.read_csv(abspath)
     
    return df


# convert categorical data to numerical 
def convertData(data, drop:list[str], maps:list[dict], export:tuple[bool, str]):
    # drop indicated columns (should be a list of header names)
    if drop:
        for i in range(len(drop)):
            data = data.drop(columns=drop[i])

    if maps:
        idx=0
        for feat in data.columns:
            if data[feat].dtype == 'string':
                #print(f"Converting column {feat} with map {idx}")
                data[feat] = data[feat].map(maps[idx])
                idx += 1
            elif data[feat].dtype == 'bool':
                data[feat] = data[feat].astype(int)
                        
        if (export[0]):
            data.to_csv(export[1])

    return data


def main():
    mapGender = {'Male':0, 'Female':1, 'Other':2}
    mapGenre = {"Mobile Games":0, "MOBA":1, "FPS":2, "Battle Royale":3, "MMO":4, "RPG":5, "Strategy":6}
    mapPrimary = {"Age of Empires":0, "Apex Legends":1, "CS:GO":2, "Call of Duty":3, "Candy Crush":4, "Civilization VI":5, 
                "Clash of Clans":6, "Cyberpunk 2077":7, "Dota 2":8, "Elden Ring":9, "Elder Scrolls Online":10, 
                "Final Fantasy XIV":11, "Fortnite":12, "Genshin Impact":13, "League of Legends":14, "Mobile Legends":15, 
                "Overwatch":16, "PUBG":17, "PUBG Mobile":18, "Skyrim":19, "StarCraft II":20, "Valorant":21, 
                "Warzone":22, "World of Warcraft":23 }
    mapPlatform = {"PC":0, "Multi-platform":1, "Console":2, "Mobile":3}
    mapSQual = {"Insomnia":0, "Very Poor":1, "Poor":2, "Fair":3, "Good":4}
    mapSDis = {"Never":0, "Rarely":1, "Sometimes":2, "Often":3, "Always":4}
    mapAperf = {"Failing":0, "Poor":1, "Below Average":2, "Average":3, "Good":4, "Excellent":5}
    mapMood = {"Depressed":0, "Anxious":1, "Angry":2, "Irritable":3, "Withdrawn":4, "Restless":5, "Normal":6, "Excited":7, "Euphoric":8}
    mapMSFreq = {"Never":0, "Rarely":1, "Sometimes":2, "Often":3, "Daily":4}
    mapAddict = {"Low":0, "Moderate":1, "High":2, "Severe":3}
    mapBinary = {"TRUE":1, "FALSE":0}
    maps = [mapGender, mapGenre, mapPrimary, mapPlatform, mapSQual, mapSDis, mapAperf, mapMood, mapMSFreq, mapAddict]


    # filename = "GamingandMentalHealth.csv"  
    # data = readData(filename)

    # # drop primary game for now 
    # dropCols = ["record_id"]
    # exportTo = (True, "GamingandMentalHealth_conv_noid.csv")
    # data_conv = convertData(data.copy(), dropCols, maps, exportTo)

    # #print(data.head(1))

    data = readData("ml-project/GamingandMentalHealth_final.csv")
    # spearman = data.corr(method='spearman')
    # print(spearman)

    data = data.to_numpy()

    x = data[:, 0:-1]       # data is all features
    target = data[:,-1]     # target is mental_health_risk

    scaler = StandardScaler()
    xscaled = scaler.fit_transform(x)

    ndims = 3 # dims of the embedded space
    # tsne = TSNE(ndims)
    # result = tsne.fit_transform(xscaled)
    # result_df = pd.DataFrame({'TSNE_col1': result[:,0], 'TSNE_col2': result[:,1], 'TSNE_col3' : result[:,2], 'GamingMentalHealth' : target})
    

    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')
    # cmap = plt.get_cmap('tab10', -4)
    # img = ax.scatter(xs=result_df['TSNE_col1'], ys=result_df['TSNE_col2'], zs=result_df['TSNE_col3'], c=result_df['GamingMentalHealth'], cmap=cmap)
    # plt.title("Gaming Mental health risk data in 3D (TSNE)")
    # fig.colorbar(img, ax=ax, label='Risk Level')
    # plt.show()


    pca = PCA(ndims)
    result_pca = pca.fit_transform(xscaled)
    result_pca = pd.DataFrame({'PCA_col1': result_pca[:,0], 'PCA_col2': result_pca[:,1], 'PCA_col3' : result_pca[:,2], 'GamingMentalHealth' : target})
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    #cmap = plt.get_cmap('tab10', 4)
    cmap = ListedColormap(['tab:green','tab:purple','tab:pink','tab:brown'])
    img = ax.scatter(xs=result_pca['PCA_col1'], ys=result_pca['PCA_col2'], zs=result_pca['PCA_col3'], c=result_pca['GamingMentalHealth'], cmap=cmap)
    plt.title("Gaming Mental health risk data in 3D (PCA)")
    fig.colorbar(img, ax=ax, label='Risk Level')
    plt.show()


main()