import sys
import pandas as pd

presidents_df = pd.read_csv("president_heights.csv", sep=',')

x = int(sys.argv[1]) #start of a slice
y = int(sys.argv[2]) #stop of a slice

def presidents():
    heights = presidents_df.iloc[x:y, 2]
    av_heights = round(heights.mean(), 2)

    print(f' The average height of presidents number {x} to {y} is {av_heights}')

presidents()
