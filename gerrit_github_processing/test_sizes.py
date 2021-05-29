import pandas as pd
import os

from transformers import T5Tokenizer, T5Config, T5ForConditionalGeneration
tokenizer = T5Tokenizer.from_pretrained("./model/TestModel.model")

df = pd.read_csv(filepath_or_buffer = "./final_df.csv", index_col=0, dtype = str, na_filter=False).reset_index().drop(["index"], axis=1)

# count_100 = 0
# count_200 = 0
# count_256 = 0
# count_300 = 0
# count_400 = 0
count = 0

for idx, row in df.iterrows():
	if idx % 10000 == 0:
		print(idx)
	comment = row["comment"]
	code_before = row["before"]
	code_after = row["after"]
	code_before_marked = row["before_marked"]
	comment_no_stopwords = row["comment_no_stopwords"]

	comment_no_stopwords_token_len = len(tokenizer.encode(comment_no_stopwords))
	comment_token_len = len(tokenizer.encode(comment))
	code_before_marked_token_len = len(tokenizer.encode(code_before_marked))
	code_after_token_len = len(tokenizer.encode(code_after))

	if comment_no_stopwords_token_len <= 100 and code_before_marked_token_len <= 100 and code_after_token_len <= 100 and comment_token_len <= 100 :
		count += 1
	# if (comment_no_stopwords_token_len + code_before_marked_token_len <= 400) and code_after_token_len <= 400 and comment_token_len <= 400:
	# 	count_400 += 1
	# if (comment_no_stopwords_token_len + code_before_marked_token_len <= 300) and code_after_token_len <= 300 and comment_token_len <= 300:
	# 	count_300 += 1
	# if (comment_no_stopwords_token_len + code_before_marked_token_len <= 256) and code_after_token_len <= 256 and comment_token_len <= 256:
	# 	count_256 += 1
	# if (comment_no_stopwords_token_len + code_before_marked_token_len <= 200) and code_after_token_len <= 200 and comment_token_len <= 200:
	# 	count_200 += 1
	# if (comment_no_stopwords_token_len + code_before_marked_token_len <= 100) and code_after_token_len <= 100 and comment_token_len <= 100:
	# 	count_100 += 1

print(count)

# print(count_100)
# print(count_200)
# print(count_256)
# print(count_300)
# print(count_400)
