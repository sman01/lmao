
import os
import glob
import pandas as pd
os.chdir(r"/home/sman/Desktop/lmao/reviews/")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(type(all_filenames))
print(all_filenames)
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "Review.csv", index=False, encoding='utf-8-sig')
print("all done")
