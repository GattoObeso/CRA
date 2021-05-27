# USING PRE-TRAINED MODELS TO PARTIALLY AUTOMATE CODE REVIEW ACTIVITIES

In this work, we investigate the capabilities of Generative Pre-trained Transformers, T5(Text-To-Text Transfer Transformer) to support code review.

## How to replicate our results

### Step 1 - Set up a GCS Bucket 
This GCS Bucket will hold all the data needed for Setting up, pre-training, fine-tuning and testing our T5 model.
To Set up a new GCS Bucket, please follow the [orignal guide](https://cloud.google.com/storage/docs/quickstart-console.) provided by Google. 

### Step 2 - Get the datasets and all our utilities

#### Pre-Training
Obtained by mining [Stack Overflow](https://www.brentozar.com/archive/2015/10/how-to-download-the-stack-overflow-database-via-bittorrent/) and [CodeSearchNet](https://github.com/github/CodeSearchNet) data. 

#### Fine-Tuning
We will fine tune our T5 small model on different datasets obtained by mining code review data from Gerrit and GitHub repositories

##### Fine-Tuning v1 (Small)
Same dataset used by [Tufano et al.](https://arxiv.org/abs/2101.02518), not abstracted code and raw comments. 
##### Fine-Tuning v2 (Small)
Same dataset used by [Tufano et al.](https://arxiv.org/abs/2101.02518), not abstracted code and cleaned comments.
##### Fine-Tuning (Large)
Our new Large dataset 

### (optional) Step 2.5 - Process the datasets
All our datasets are alredy processed and it's all set up to start pre-training and fine-tuning the models

However, if you want to replicate our pre-processing steps, you just need to follow [this](http://) Colab notebook.  Here we will clean our raw datasets and train the [Sentencepiece](https://github.com/google/sentencepiece/blob/master/python/README.md) model to accommodate the expanded vocabulary given by the pre-training dataset.

### Step 4 - Pre-Training and Fine-Tuning
To pre-train and then, fine-tune T5, please follow the colab notebooks provided:

- [Pre-Training](http://)
- [Fine-Tuning](http://)

### Step 5 - Generate the predictions
We generate results on different beams converting the model in pyTorch, if you want to generete predictions using a beam of 1, you can directly use the fine-tuning colab notebook linked above, once the model is fine-tuned, you can generate custum prediction. 
The code to convert the model is available [here](http://)
while to compute perfect predictions, almost perfect predictions, codeBleu and bleu, we used [this](http://) other colab notebook.

here you can see [Our results](https://docs.google.com/spreadsheets/d/1JBdZZaGhOSGLIKkZjkEWvRudg-TIWCuaeYTxGnTPOyE/edit?usp=sharing)
