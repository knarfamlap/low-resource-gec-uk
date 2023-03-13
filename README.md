# A Low-Resource Approach to the Grammatical Error Correction of Ukranian

## Getting Started

Clone this repo:

```bash
$ git clone https://github.com/knarfamlap/low-resource-gec-uk.git
```

Create a python envoriment:

```bash
$ python3 -m venv env
$ source env/bin/activate
```

Install dependencies

```bash
$ python3 -m pip install -r requirements.txt
```

## Training

Use the following script to train mT5-large:

```bash
$ python3 train.py --train_tsv /path/to/train/tsv \
    --valid_tsv /path/to/valid/tsv \
    --output_dir /path/to/output/dir \
    --model_name mt5-large \
    --batch_size 32 \
    --max_epochs 3
    ```
