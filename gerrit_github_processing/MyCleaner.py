import pandas as pd
import os
from Cleaner import Cleaner

# importing our tokenizer, same as the one our model will use
# here so that we do not have to instantiate one for each csv
from transformers import T5Tokenizer, T5Config, T5ForConditionalGeneration
t5_tokenizer = T5Tokenizer.from_pretrained("./model/TestModel.model")

# Building list of stopword passed to the cleaner,
# here so that we do not have to do it for each csv
keywords = ['abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 
			'const', 'continue', 'default', 'do', 'double','else', 'enum', 'extends', 'final', 
			'finally', 'float', 'for', 'if', 'goto', 'implements', 'import', 'instanceof', 'int', 
			'interface', 'long', 'native', 'new', 'package', 'private', 'protected', 'public',
			'return', 'short', 'static', 'strictfp', 'super', 'switch', 'synchronized', 'this', 
			'throw', 'throws', 'transient', 'try', 'void', 'volatile', 'while', 'true', 'false', 
			'null', '+=', '&&', '-=', '!=', '++', '||', '<=', '>=', '<<=', '>>=', '...', '--', 
			'/=', '>>>=', '<<<=', 'equals', 'inline', 'override']

keywords =	[k.upper() for k in keywords]

stopwords = [line.strip().upper() for line in open("./filters_lists/stop-words-english.txt")]
stopwords.append('NIT')

idioms = 	[line.strip().upper() for line in open("./filters_lists/my_idioms_300.txt")]

for word in stopwords:
	if word in idioms or word in keywords:
		stopwords.pop(stopwords.index(word))

english_cache = pd.read_csv(filepath_or_buffer = "./english_real_predictions.tsv",names=["comment", "accuracy", "lang"], sep='\t', index_col=0, dtype = str, na_filter=False).reset_index().drop_duplicates()


n_irrelevant_comments = 0
n_not_marked = 0
n_non_latin = 0
n_before_equals_after = 0
n_non_english = 0
n_too_long = 0
n_too_long_after = 0
n_multiple_rev = 0
n_comment_empty = 0
n_code_before_empty = 0
n_code_before_marked_empty = 0
n_code_after_empty = 0
n_final_duplicates = 0

n_starting_triplets = 0
n_total_triplets = 0

files = [f for f in os.listdir("./processed")]

for x in range(0,len(files)):
	if x > 1:
		print("completed: ", round((x * 100) / len(files),1), "%           ", end='\r')
	file_name =  os.path.join("./processed", files[x])
	try:
		df = pd.read_csv(filepath_or_buffer = file_name, index_col=0, dtype = str, na_filter=False)
		# df = df.drop(["id_df"], axis=1)

		n_starting_triplets += len(df)
		cleaner = Cleaner(df, t5_tokenizer, stopwords, english_cache)

		cleaner.remove_non_marked()
		cleaner.clean_df()

		# final cleaning : remove methods which has more than one review
		cleaner.remove_multiple_method_comments()

		n_irrelevant_comments += cleaner.irrelevant_comments
		n_not_marked += cleaner.not_marked
		n_non_latin += cleaner.non_latin
		n_before_equals_after += cleaner.before_equals_after
		n_non_english += cleaner.non_english
		n_too_long += cleaner.too_long
		n_too_long_after += cleaner.too_long_after
		n_multiple_rev += cleaner.multiple_reviews

		n_comment_empty += cleaner.comment_empty
		n_code_before_empty += cleaner.code_before_empty
		n_code_before_marked_empty += cleaner.code_before_marked_empty
		n_code_after_empty += cleaner.code_after_empty

		df = cleaner.getDF()
		
		if len(df):
			df.to_csv("./cleaned/" + files[x])
		
	except Exception as e:
		print(e)
		print(file_name)
		print()

frames = []
files = [f for f in os.listdir("./cleaned")]

for x in range(0,len(files)):
	file_name =  os.path.join("./cleaned", files[x])
	df = pd.read_csv(filepath_or_buffer = file_name, index_col=0, dtype = str, na_filter=False)
	frames.append(df)

result_df = pd.concat(frames)

# discard all the remaining duplicates
n_final_duplicates = len(result_df) - len(result_df.drop_duplicates(subset=["before", "after"]))
result_df = result_df.drop_duplicates(subset=["before", "after"])

# when a comment like "why null?" is processed, only null is left, and pandas interprets it as a NaN
result_df = result_df.fillna('null')
n_total_triplets = len(result_df)


result_df.to_csv("./final_df.csv")

print("number of starting triplets: ", n_starting_triplets)
print("number of total triplets: ", n_total_triplets)

print("number of irrelevant comments: ", n_irrelevant_comments)
print("number of not marked: ", n_not_marked)
print("number of non latin: ", n_non_latin)
print("number of before == after: ", n_before_equals_after)
print("number non English: ", n_non_english)
print("number too many tokens: ", n_too_long)
print("number too many tokens after method: ", n_too_long_after)
print("number of methods with multiple reviews: ", n_multiple_rev)

print("empty comments: ", n_comment_empty)
print("empty code before: ", n_code_before_empty)
print("empty code before marked: ", n_code_before_marked_empty)
print("empty code after: ", n_code_after_empty)
print("number of final duplicates: ", n_final_duplicates)



