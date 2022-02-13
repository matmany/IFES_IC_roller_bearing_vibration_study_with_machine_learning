import scipy.io
import pandas as pd
import os

def convert_mat_to_csv(file, dir_name):
    filename = os.fsdecode(file)
    if filename.endswith(".mat"):
        generate_csv(filename, dir_name)

def get_mat_data(filename, dir_name):
    print('Processando:' + filename)
    mat_contents = scipy.io.loadmat(dir_name + '/' + filename)
    mat_contents = {k:v for k, v in mat_contents.items() if k[0] != '_'}
    return pd.DataFrame({k: pd.Series(v[0]) for k, v in mat_contents.items()})

def generate_csv(filename, dir_name):
    data = get_mat_data(filename, dir_name)
    filename = filename.replace('.mat', '.csv')
    
    if not os.path.exists(dir_name + '_CSV'):
        os.makedirs(dir_name + '_CSV')

    data.to_csv(dir_name+"_CSV/"+filename)


dir_name = './Sinais_NR15_M07_F10_1'
signals_to_convert_dir = os.fsencode(dir_name)

for file in os.listdir(signals_to_convert_dir):
    convert_mat_to_csv(file, dir_name)

#mat = scipy.io.loadmat('./Sinais_NR15_M07_F10_1/time_K001.mat')
#mat = {k:v for k, v in mat.items() if k[0] != '_'}
#data = pd.DataFrame({k: pd.Series(v[0]) for k, v in mat.items()}) # compatible for both python 2.x and python 3.x

#data.to_csv("./example.csv")