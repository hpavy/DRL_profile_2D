import pandas as pd
def find_best(file):
    df = pd.read_csv(file + "/Values.txt", sep="\t", header=0)
    best = df[df['Reward'] == df['Reward'].max()].iloc[0,1:11]
    return best.values
