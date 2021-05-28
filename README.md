# USING PRE-TRAINED MODELS TO PARTIALLY AUTOMATE CODE REVIEW ACTIVITIES

In this work, we investigate the capabilities of Generative Pre-trained Transformers, T5(Text-To-Text Transfer Transformer) to support code review.

## How to replicate our results

### Step 1 - Set up a GCS Bucket 
This GCS Bucket will hold all the data needed for Setting up, pre-training, fine-tuning, and testing our T5 model.
To Set up a new GCS Bucket, please follow the [orignal guide](https://cloud.google.com/storage/docs/quickstart-console.) provided by Google. 

### Step 2 - Get the datasets and all our utilities
You need to have [this](https://zenodo.org/record/4812785) folder on your GSC bucket. It will contain all of our data and some utilities to replicate our results.

In particular you will have:
- **Pre-Training dataset** Obtained by mining [Stack Overflow](https://www.brentozar.com/archive/2015/10/how-to-download-the-stack-overflow-database-via-bittorrent/) and [CodeSearchNet](https://github.com/github/CodeSearchNet) data. 
- **Fine-Tuning dataset** We will fine-tune our T5 small model on different datasets obtained by mining code review data from Gerrit and GitHub repositories.
   - **Fine-Tuning dataset v1 (Small)**
Same dataset used by [Tufano et al.](https://arxiv.org/abs/2101.02518), not abstracted code and raw comments. 
   - **Fine-Tuning dataset v2 (Small)**
Same dataset used by [Tufano et al.](https://arxiv.org/abs/2101.02518), not abstracted code and cleaned comments.
   - **Fine-Tuning dataset (Large)**
Our new Large dataset 

### (optional) Step 2.5 - Process the raw datasets
All our datasets are already processed, and it's all set up to start pre-training and fine-tuning the models.

However, if you want to replicate our pre-processing steps, you just need to follow [this](https://github.com/masies/CRA/blob/main/Replication_package_PreProcessing.ipynb) Colab notebook.  Here we will clean our raw datasets and train the [Sentencepiece](https://github.com/google/sentencepiece/blob/master/python/README.md) model to accommodate the expanded vocabulary given by the pre-training dataset.

### Step 3 - Pre-Training and Fine-Tuning
To pre-train and then fine-tune T5, please follow the colab notebooks provided:

- [Pre-Training](https://github.com/masies/CRA/blob/main/Replication_package_PreTraining.ipynb)
- [Fine-Tuning](https://github.com/masies/CRA/blob/main/Replication_package_FineTuning.ipynb)

### Step 4 - Generate the predictions
We generate results on different beams converting the model in PyTorch; if you want to generate predictions using a beam of 1, you can directly use the fine-tuning colab notebook linked above, once the model is fine-tuned, you can generate custom prediction. 
The code to convert the model is available [here](https://github.com/masies/CRA/blob/main/Replication_package_pytorchConversion.ipynb) and will also have all the functionalities to compute perfect predictions, almost perfect predictions, codeBleu and BLEU.

here you can see [Our results](https://docs.google.com/spreadsheets/d/1JBdZZaGhOSGLIKkZjkEWvRudg-TIWCuaeYTxGnTPOyE/edit?usp=sharing)
