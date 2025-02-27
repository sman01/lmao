import os
import glob
import pandas as pd

os.chdir(r"/home/sman/Desktop/raflao/sman/review/")
extension = "csv"
all_filenames = [i for i in glob.glob("*.{}".format(extension))]
print(type(all_filenames))
all_filenames.sort()

# combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
# export to csv
combined_csv.to_csv("Final_Review.csv", index=False, encoding="utf-8-sig")
print("all done")
