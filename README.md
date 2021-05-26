# USING PRE-TRAINED MODELS TO PARTIALLY AUTOMATE CODE REVIEW ACTIVITIES

In this work, we investigate the capabilities of Generative Pre-trained Transformers, T5(Text-To-Text Transfer Transformer) to support code review.

## Pipeline

### Step 1 - Set up a GCS Bucket 
This GCS Bucket will hold all the data needed for Setting up, pre-training, fine-tuning and testing our T5 model.
To Set up a new GCS Bucket, please follow the orignal guide provided by Google. Here the link: https://cloud.google.com/storage/docs/quickstart-console.

### Step 2 - Get the datasets
#### Pre-Training
Obtained by mining (Stack Overflow)[https://www.brentozar.com/archive/2015/10/how-to-download-the-stack-overflow-database-via-bittorrent/] and (CodeSearchNet)[https://github.com/github/CodeSearchNet] data. You can download this here (!!)

#### Fine-Tuning
We will fine tune our T5 small on different datasets obtained by mining code review data from Gerrit and GitHub repositories

##### Fine-Tuning v1 (Small)
Same dataset used by [Tufano et al.](https://arxiv.org/abs/2101.02518), not abstracted code and raw comments. You can download this here (!!)
##### Fine-Tuning v2 (Small)
Same dataset used by [Tufano et al.](https://arxiv.org/abs/2101.02518), not abstracted code and cleaned comments. You can download this here (!!)
##### Fine-Tuning (Large)
Large dataset  You can download this here (!!)

### Step 3 - Train the [Sentencepiece](https://github.com/google/sentencepiece/blob/master/python/README.md) model
In order to pre-train and fine-tune a (T5 small)[https://github.com/google-research/text-to-text-transfer-transformer] model, we need a new sentencepiece model to accommodate the expanded vocabulary given by the pre-training dataset.

```
pip install sentencepiece
import sentencepiece as spm
spm.SentencePieceTrainer.train('--input=pretraining.txt --model_prefix=dl4se --vocab_size=32000 --bos_id=-1  --eos_id=1 --unk_id=2 --pad_id=0') 
```
The new model has to be trained on the entire pre-training corpus.

### Step 4 - Processing datasets for fine-tuning tasks
With this(!!) Colab notebook, you can process the fine tuning datasets of your choice to generate data for training the different tasks we will submit to T5

### Step 5 - Pre-Training and Fine-Tuning
To pre-train and then, fine-tune T5, please use the script we provide here:

- Pre-Training(!!)
- Fine-Tuning(!!)

### Step 6 - Generate the predictions
First you need to convert the TF model into a pytorch model by using TF_to_Pytorch(!!) , then run Generate Results(!!)

Our results: https://drive.google.com/drive/folders/14ywfhJorNNeWxgSV1bI0XIzlLAFu8odH?usp=sharing
