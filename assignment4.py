import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as pls

def count_kmers(sequence, k):
    """
    This function counts kmers of size k, where k is specified as an argument. It receives sequence and K as argument.
    """
    if not sequence or k==0:
        raise ValueError('sequence is empty or k=0')
    number = min(4**k , len(sequence)-k+1)
    return(number)


def count_df (sequence):
    """
    This function creates a pandas data frame containing all possible k and the associated number of observed and expected kmers.
    """
    df = pd.DataFrame(columns=['k','observed', 'posibility'])
    if not sequence:
        return(df)
    sequence_length =  len(sequence)
    for k in range(sequence_length):
        count_observed={}
        for i in range(sequence_length-k):
            temp = sequence[i:i+k+1]
            if temp in count_observed:
                count_observed[temp] +=1
            else:
                count_observed[temp] =1
        df.loc[k]=[k+1,len(count_observed),count_kmers(sequence,k+1)]
    return(df)

def print_df(df):
    """
    This function print data frame containing all possible k and the associated number of observed and expected kmers. It receives dataframe as an argument.
    """
    if df.empty:
        raise ValueError('There is no data, the sequence is empty')
    print('k  ', 'observed   ', 'posibility')
    for index, row in df.iterrows():
        print(row['k'],'    ', row['observed'],'        ', row['posibility'])
    print('observed= ', df['observed'].sum() , ',  posibility= ', df['posibility'].sum())


def linguistic_complexity(df):
    """
    This function calculates linguistic complexity. It receives dataframe as an argument.
    """
    if df.empty:
        raise ValueError('There is no data, the sequence is empty')
    return(df['observed'].sum() / df['posibility'].sum() )

def plot_df(df):
    """
    This function produces a graph from the data frame of the proportion of each kmer observed. It receives data frame as an argument.

    """
    if  df.empty:
        raise ValueError('There is no graph, the sequence is empty')
    df['proportion'] = df.observed / df.posibility
    df.plot(x='k', y='proportion', kind='bar')
    pls.show()

def datacheck(sequence):
    """
    This function checks the sequence for not empty and not wrong characters. It receives sequence as an argument.

    """
    if not sequence:
        print('There is no data, the sequence is empty')
        return False
    elif set(sequence).issubset(['A','C','T','G']):
        return True
    else:
        print('The sequence contains wronge code')
        return False


if __name__ == '__main__':
    sequence=str(sys.argv[1:])[2:-2]
#    sequence = ''
    if datacheck(sequence):
        print('your sequence is:', str(sequence))
        df = count_df(sequence)
        print_df(df)
        print('linguistic complexity', linguistic_complexity(df))
        plot_df(df)






















"""
def count_observed_kmers2 (sequence):
    df = pd.DataFrame(columns=['k','observed', 'posibility'])

    sequence_length =  len(sequence)
    count_observed={}
    for k in range(sequence_length):
        df.loc[k]=[k+1,2,count_kmers(sequence,k+1)]
        for i in range(sequence_length-k):
            print(sequence[i:i+k+1])
            temp = sequence[i:i+k+1]
            if temp in count_observed:
                count_observed[temp] +=1
            else:
                count_observed[temp] =1
    print('-------------')
    for words in count_observed:
        print( words, count_observed[words])
    print(len(count_observed))
    return(len(count_observed))
"""
