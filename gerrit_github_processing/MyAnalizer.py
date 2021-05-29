import lizard
import pandas as pd
import os
from Analyzer import Analyzer

tot_data = 0
tot_duplicates = 0
tot_left = 0
tot_nan = 0
tot_owner = 0
tot_before_equal_after = 0
tot_comm_to_comm = 0
tot_no_comment = 0
tot_no_marked = 0
tot_no_method_after = 0
tot_no_method_before = 0
tot_no_valid_ref = 0
tot_triplets = 0

from uselessCSV import useless_csv

def processCSV(name, path, hub):

	if name in useless_csv:
		return

	global tot_data
	global tot_duplicates
	global tot_left
	global tot_nan
	global tot_owner
	global tot_before_equal_after
	global tot_comm_to_comm
	global tot_no_comment
	global tot_no_marked
	global tot_no_method_after
	global tot_no_method_before
	global tot_no_valid_ref
	global tot_triplets

	try:
		df = pd.read_csv(filepath_or_buffer = path)
		analyzer = Analyzer(df, hub)
		analyzer.remove_duplicates()
		analyzer.remove_owner_comments()
		analyzer.remove_nan_data()
		dfr = analyzer.analyze_data()

		tot_data 				+= len(df)
		tot_duplicates			+= analyzer.duplicates
		tot_left 				+= analyzer.left_side_cases
		tot_nan 				+= analyzer.nan_data
		tot_owner 				+= analyzer.owner_comments
		tot_before_equal_after 	+= analyzer.before_equal_after
		tot_comm_to_comm 		+= analyzer.comm_to_comm
		tot_no_comment			+= analyzer.no_comment
		tot_no_marked 			+= analyzer.no_marked
		tot_no_method_after 	+= analyzer.no_method_after
		tot_no_method_before 	+= analyzer.no_method_before
		tot_no_valid_ref 		+= analyzer.no_valid_ref
		tot_triplets 			+= len(dfr)

		if len(dfr) > 0:
			# print('current csv: ', name, " ------ ", len(dfr)) 
			dfr.to_csv("./processed/" + name)
		else :
			print('+++++ USELESS CSV: ', name)

	except Exception as e:
		print("----- CVS unreadable: ", name)
		print(e)

for file in os.listdir("./github"):
	path =  os.path.join("./github", file)
	processCSV(file, path, "GitHub")

for file in os.listdir("./gerrit"):
	path =  os.path.join("./gerrit", file)
	processCSV(file, path, "Gerrit")


print('starting triplets: ', tot_data)
print('original duplicates: ', tot_duplicates)
print('original left: ', tot_left)
print('original nan: ', tot_nan)
print("tot_owner", tot_owner)
print("tot_no_valid_ref", tot_no_valid_ref)
print("tot_comm_to_comm", tot_comm_to_comm)
print("tot_no_method_before", tot_no_method_before)
print("tot_no_marked", tot_no_marked)
print("tot_no_method_after", tot_no_method_after)
print("tot_before_equal_after", tot_before_equal_after)
print("tot_no_comment", tot_no_comment)
print("tot_triplets", tot_triplets)



