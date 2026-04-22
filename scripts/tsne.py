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
    abspath = dirpath + "\\data\\" + datafile

    # read data into a pandas dataframe. data file is comma separated so use read_csv
    df = pd.read_csv(abspath)
     
    return df


def main():
    # read in the fully numerical, imputed data
    data = readData("GamingandMentalHealth_final.csv")

    # convert the pd dataframe to numpy array for modeling
    data = data.to_numpy()

    # split into data and target
    x = data[:, 0:-1]       # data is all features
    target = data[:,-1]     # target is mental_health_risk

    # standardize data: standardScaler uses x-mean/stddev 
    scaler = StandardScaler()
    xscaled = scaler.fit_transform(x)

    # project into 3d space
    ndims = 3 # dims of the embedded space
    tsne = TSNE(ndims)  # create tsne object with 3 dims
    result = tsne.fit_transform(xscaled) # actually calculate tsne on the scaled dataset!
    # create a dataframe with each tsne vector and the target for easier plotting
    result_df = pd.DataFrame({'TSNE_col1': result[:,0], 
                              'TSNE_col2': result[:,1], 
                              'TSNE_col3' : result[:,2], 
                              'GamingMentalHealth' : target})
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    # create a new colormap just so that the classes are easier to differentiate
    cmap = ListedColormap(['tab:green','tab:purple','tab:pink','tab:brown'])
    # create scatterplot: use the class labels to specify color groups and use the custom cmap 
    img = ax.scatter(xs=result_df['TSNE_col1'], 
                     ys=result_df['TSNE_col2'], 
                     zs=result_df['TSNE_col3'], 
                     c=result_df['GamingMentalHealth'], cmap=cmap)
    plt.title("Gaming Mental health risk data in 3D (TSNE)")
    fig.colorbar(img, ax=ax, label='Risk Level') # colorbar as a legend since that was easiest
    plt.show()


main()