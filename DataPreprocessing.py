import datetime
import logging
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

# Config
saveDatasetName = '202003_questions'
cleanedDatasetName = '202003_questions_cleaned'

# read csv file as dataframe
df_clean = pd.read_csv('./datasets/'+saveDatasetName+'.csv')


#TODO: add different clean methods

# remove html tag
def remove_specialchar(body):
    soup = BeautifulSoup(body, 'html.parser')
    return soup


# clean pipeline
def stack_clean(stacks, flag):
    for i in range(len(stacks)):
        if flag == 'html_tag':
            # print(type(stacks[i]))
            # print(stacks[i])
            stacks[i] = remove_specialchar(stacks[i])
    return stacks


# save dataset
def save_dataset(df, df_name):
    logging.info('Saving dataset...')
    # Create Saving Files
    # if not os.path.exists('/datasets'):
    #     os.makedirs('/datasets')
    df.to_csv(r'./datasets/' + df_name + '.csv', index=False, header=True)
    logging.info('Saved parsed dataset')


df_clean['body'] = stack_clean(df_clean['body'], 'html_tag')
save_dataset(df_clean, cleanedDatasetName)