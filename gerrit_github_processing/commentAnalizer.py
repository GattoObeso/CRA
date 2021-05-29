import pandas as pd
import os


# from transformers import T5Tokenizer, T5Config, T5ForConditionalGeneration
# t5_tokenizer = T5Tokenizer.from_pretrained("./model/TestModel.model")

# keywords = ['abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 
# 			'const', 'continue', 'default', 'do', 'double','else', 'enum', 'extends', 'final', 
# 			'finally', 'float', 'for', 'if', 'goto', 'implements', 'import', 'instanceof', 'int', 
# 			'interface', 'long', 'native', 'new', 'package', 'private', 'protected', 'public',
# 			'return', 'short', 'static', 'strictfp', 'super', 'switch', 'synchronized', 'this', 
# 			'throw', 'throws', 'transient', 'try', 'void', 'volatile', 'while', 'true', 'false', 
# 			'null', '+=', '&&', '-=', '!=', '++', '||', '<=', '>=', '<<=', '>>=', '...', '--', 
# 			'/=', '>>>=', '<<<=', 'equals', 'inline', 'override']

# keywords =	[k.upper() for k in keywords]

# stopwords = [line.strip().upper() for line in open("./filters_lists/stop-words-english.txt")]
# stopwords.append('NIT')

# idioms = 	[line.strip().upper() for line in open("./filters_lists/my_idioms_300.txt")]

# for word in stopwords:
# 	if word in idioms or word in keywords:
# 		stopwords.pop(stopwords.index(word))

# from nltk.tokenize import word_tokenize
# comments = []

# df = pd.read_csv(filepath_or_buffer = "./final_df.csv", index_col=0).reset_index().drop(["index"], axis=1)
# df = df.drop(["before", "after", "before_marked"], axis=1)
# df['comment'] = df['comment'].apply(str)
# df['comment'] = df['comment'].str.lower()

# df1 = df[df.apply(lambda row: len(word_tokenize(row['comment'])) == 1, axis=1)]
# df2 = df[df.apply(lambda row: len(word_tokenize(row['comment'])) == 2, axis=1)]
# df3 = df[df.apply(lambda row: len(word_tokenize(row['comment'])) == 3, axis=1)]
# df4 = df[df.apply(lambda row: len(word_tokenize(row['comment'])) == 4, axis=1)]

# df1 = df1["comment"].value_counts()
# df2 = df2["comment"].value_counts()
# df3 = df3["comment"].value_counts()
# df4 = df4["comment"].value_counts()

# df1.to_csv("./CommentAnalysis/comment_analysis_1.csv")
# df2.to_csv("./CommentAnalysis/comment_analysis_2.csv")
# df3.to_csv("./CommentAnalysis/comment_analysis_3.csv")
# df4.to_csv("./CommentAnalysis/comment_analysis_4.csv")


# from Cleaner import Cleaner

# cleaner = Cleaner(pd.DataFrame([]), t5_tokenizer, stopwords, pd.DataFrame([]))
# print(cleaner.removeStopwords("never null"))

df = pd.read_csv(filepath_or_buffer = "./final_df.csv", index_col=0, na_filter=False).reset_index().drop(["index"], axis=1)
# print(df)
# df = df.fillna('null')
# print(df)
# print(len(df))
# print(df[df.isna().any(axis=1)])
# frames = []
# files = [f for f in os.listdir("./cleaned")]

# for x in range(0,len(files)):
# 	file_name =  os.path.join("./cleaned", files[x])
# 	df = pd.read_csv(filepath_or_buffer = file_name, index_col=0, dtype = str, na_filter=False)
# 	frames.append(df)

# # discard all the remaining duplicates
# result_df = pd.concat(frames)

# n_final_duplicates = len(result_df) - len(result_df.drop_duplicates(subset=["before", "after"]))
# result_df = result_df.drop_duplicates(subset=["before", "after"])
# n_total_triplets = len(result_df)

# df.to_csv("./final_df.csv")

# print(n_total_triplets)
# print(result_df)

