import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##########################################
######### Values.txt reading
def print_reward(file, ymin=-1, ymax=3.5, y=None, title=None):
    df_values = pd.read_csv(file + "/Values.txt", sep="\t", header=0)
    # print(df_values.head())

    ### Reward plot

    nb_env = 8 # Number of parallel environments
    nb_av = 3 # Number of reloads
    index_row = np.array(df_values.index.values.tolist())
    nb_gen = df_values.at[ index_row[-1], 'Index'] + 1
    # print(nb_gen)
    list_gen = np.array(range(nb_gen))
    list_env = np.array(range(nb_env))

    for i in range(1, nb_av+1-2):   # enlever le -2 normalement

        plt.figure("Reward evolution run n_"+str(i), figsize=(12*0.6,8*0.6))
        if title is None :
            plt.title("Reward per episode")
        else : 
            plt.title(title)
        plt.xlabel("Episode")
        plt.ylabel("Reward")
        
        for env in list_env:
            try :
                # print(np.where( (index_row%nb_env)==env )[0])
                if np.shape(np.where( (index_row[(i-1)*nb_gen*nb_env:i*nb_gen*nb_env]%nb_env)==env )[0]) != (0,):
                    # print(np.shape(np.where( (index_row[(i-1)*nb_gen*nb_env:i*nb_gen*nb_env]%nb_env)==env )[0]))
                    plt.plot(list_gen, df_values.loc[ np.where( (index_row[(i-1)*nb_gen*nb_env:i*nb_gen*nb_env]%nb_env)==env )[0], "Reward"], label="env_"+str(env))
            except:
                pass

        plt.legend(loc="best")
        plt.ylim(ymin, ymax)
        plt.grid()
        if y is not None:
            plt.axhline(y=y, color ='r', linestyle='--')
        plt.show()

def print_area(file, ymin=-1, ymax=3.5, y=None, title = None):
    df_values = pd.read_csv(file + "/Values.txt", sep="\t", header=0)
    #print(df_values.head())

    ### Reward plot

    nb_env = 8 # Number of parallel environments
    nb_av = 3 # Number of reloads
    index_row = np.array(df_values.index.values.tolist())
    nb_gen = df_values.at[ index_row[-1], 'Index'] + 1
    # print(nb_gen)
    list_gen = np.array(range(nb_gen))
    list_env = np.array(range(nb_env))

    for i in range(1, nb_av+1-2):   # enlever le -2 normalement

        plt.figure("Reward evolution run n_"+str(i), figsize=(12*0.6,8*0.6))
        if title is None :
            plt.title("Area per episode")
        else : 
            plt.title(title)
        plt.xlabel("Episode")
        plt.ylabel("Area")
        
        for env in list_env:

            # print(np.where( (index_row%nb_env)==env )[0])
            try :
                if np.shape(np.where( (index_row[(i-1)*nb_gen*nb_env:i*nb_gen*nb_env]%nb_env)==env )[0]) != (0,):
                    #print(np.shape(np.where( (index_row[(i-1)*nb_gen*nb_env:i*nb_gen*nb_env]%nb_env)==env )[0]))
                    plt.plot(list_gen, df_values.loc[ np.where( (index_row[(i-1)*nb_gen*nb_env:i*nb_gen*nb_env]%nb_env)==env )[0], "Area"], label="env_"+str(env))
            except : 
                pass

        if y is not None:
            plt.axhline(y=y, color ='r', linestyle='--')

        plt.legend(loc="best")
        plt.grid()
       #  plt.ylim(ymin=-1, ymax=3.5)

        plt.show()


def print_finesse(file, ymin=-1, ymax=3.5, y=None, legend_pointille="", title = None):
    df_values = pd.read_csv(file + "/Values.txt", sep="\t", header=0)
    #print(df_values.head())

    ### Reward plot

    nb_env = 8 # Number of parallel environments
    nb_av = 3 # Number of reloads
    index_row = np.array(df_values.index.values.tolist())
    nb_gen = df_values.at[ index_row[-1], 'Index'] + 1
    # print(nb_gen)
    list_gen = np.array(range(nb_gen))
    list_env = np.array(range(nb_env))

    for i in range(1, nb_av+1-2):   # enlever le -2 normalement

        plt.figure("Finesse evolution run n_"+str(i), figsize=(12*0.6,8*0.6))
        if title is None :
            plt.title("Finesse per episode")
        else : 
            plt.title(title)
        plt.xlabel("Episode")
        plt.ylabel("Finesse")
        
        for env in list_env:
            try :
                # print(np.where( (index_row%nb_env)==env )[0])
                if np.shape(np.where( (index_row[(i-1)*nb_gen*nb_env:i*nb_gen*nb_env]%nb_env)==env )[0]) != (0,):
                    # print(np.shape(np.where( (index_row[(i-1)*nb_gen*nb_env:i*nb_gen*nb_env]%nb_env)==env )[0]))
                    plt.plot(list_gen, df_values.loc[ np.where( (index_row[(i-1)*nb_gen*nb_env:i*nb_gen*nb_env]%nb_env)==env )[0], "finesse_moy"], label="env_"+str(env))
            except :
                pass

        plt.legend(loc="best")
        plt.ylim(ymin, ymax)
        plt.grid()
        if y is not None:
            plt.axhline(y=y, color ='r', linestyle='--', label=legend_pointille)
        plt.legend()

        plt.show()


def print_max_reward(file):
    df_values = pd.read_csv(file + "/Values.txt", sep="\t", header=0)
    print(f"Le reward maximum est de {df_values['Reward'].max()}")


def print_reward_mean(file, ymin=-1, ymax=3.5, y=None, title=None, legend_pointille= None):
    df_values = pd.read_csv(file + "/Values.txt", sep="\t", header=0)
    result_max = df_values.groupby(df_values['Index']).max()
    plt.plot(result_max.index, result_max['Reward'], color = 'b', label='Max')
    result_mean = df_values.groupby(df_values['Index']).mean()
    plt.plot(result_mean.index, result_mean['Reward'], color='purple', label='Mean')
    plt.plot(df_values['Index'], df_values['Reward'], 'o', markersize=2, color='g', label= 'Values')
    plt.legend()
    plt.grid()

    if title is None :
        plt.title("Reward per episode")
    else : 
        plt.title(title)
    plt.xlabel("Episode")
    plt.ylabel("Reward")

    plt.ylim(ymin, ymax)
    if y is not None:
        if legend_pointille is not None : 
            plt.axhline(y=y, color ='r', linestyle='--', label=legend_pointille)
            plt.legend()
        else :
            plt.axhline(y=y, color ='r', linestyle='--')
    plt.show()


def print_finesse_mean(file, ymin=-1, ymax=3.5, y=None, title=None, legend_pointille= None):
    df_values = pd.read_csv(file + "/Values.txt", sep="\t", header=0)
    result_max = df_values.groupby(df_values['Index']).max()
    plt.plot(result_max.index, result_max['finesse_moy'], color = 'b', label='Max')
    result_mean = df_values.groupby(df_values['Index']).mean()
    plt.plot(result_mean.index, result_mean['finesse_moy'], color='purple', label='Mean')
    plt.plot(df_values['Index'], df_values['finesse_moy'], 'o', markersize=2, color='g', label= 'Values')
    plt.legend()
    plt.grid()

    if title is None :
        plt.title("finesse per episode")
    else : 
        plt.title(title)
    plt.xlabel("Episode")
    plt.ylabel("Finesse")

    plt.ylim(ymin, ymax)
    if y is not None:
        if legend_pointille is not None : 
            plt.axhline(y=y, color ='r', linestyle='--', label=legend_pointille)
            plt.legend()
        else :
            plt.axhline(y=y, color ='r', linestyle='--')
    plt.show()


def print_area_mean(file, ymin=-1, ymax=3.5, y=None, title=None, legend_pointille= None):
    df_values = pd.read_csv(file + "/Values.txt", sep="\t", header=0)
    result_max = df_values.groupby(df_values['Index']).max()
    plt.plot(result_max.index, result_max['Area'], color = 'b', label='Max')
    result_mean = df_values.groupby(df_values['Index']).mean()
    plt.plot(result_mean.index, result_mean['Area'], color='purple', label='Mean')
    plt.plot(df_values['Index'], df_values['Area'], 'o', markersize=2, color='g', label= 'Values')
    plt.legend()
    plt.grid()

    if title is None :
        plt.title("Area per episode")
    else : 
        plt.title(title)
    plt.xlabel("Episode")
    plt.ylabel("Area")
    if y is not None:
        if legend_pointille is not None : 
            plt.axhline(y=y, color ='r', linestyle='--', label=legend_pointille)
            plt.legend()
        else :
            plt.axhline(y=y, color ='r', linestyle='--')
    plt.show()

def find_best(file):
    df = pd.read_csv(file + "/Values.txt", sep="\t", header=0)
    best = df[df['Reward'] == df['Reward'].max()].iloc[0,1:11]
    return best.values

def find_best_ep(file):
    df = pd.read_csv(file + "/Values.txt", sep="\t", header=0)
    best = df[df['Reward'] == df['Reward'].max()]
    return best