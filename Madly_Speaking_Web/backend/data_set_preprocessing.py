"""
Because the ROC dataset has the format:

storyid,storytitle,sentence1,sentence2,sentence3,sentence4,sentence5

The goal of this script is to "reaugment" the file such that title will be in the form 

Write a story about {insert story title}.


"""

import pandas as pd

# Load the dataset
df = pd.read_csv('dataset_2017.csv')


df['input'] = 'write a story about ' + df['storytitle'].astype(str)

# Combine the story sentences into one output string
sentence_cols = ['sentence1', 'sentence2', 'sentence3', 'sentence4', 'sentence5']
df['output'] = df[sentence_cols].astype(str).agg(' '.join, axis=1)

# Keep only the input-output columns for fine-tuning
processed_df = df[['input', 'output']]


processed_df.to_csv('t5_formatted_dataset.csv', index=False)