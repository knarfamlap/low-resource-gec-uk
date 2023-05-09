# A Low-Resource Approach to the Grammatical Error Correction of Ukranian

This repository contains the code for the paper ["A Low-Resource Approach to the Grammatical Error Correction of Ukrainian"](https://aclanthology.org/2023.unlp-1.14/) presented at EACL 2023 at the UNLP Workshop.

Authors: Frank Palma Gomez, Alla Rozovskaya, Dan Roth

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

## Inference

To generate hypothesis

```bash
$ python3 generate.py --path_to_model /path/to/trained/model \
                      --orig /path/to/inputs
```

`generate.sh` is a wrapper file that can generate hypothesis in parallel.

### Citation

```bib
@inproceedings{gomez-etal-2023-low,
    title = "A Low-Resource Approach to the Grammatical Error Correction of {U}krainian",
    author = "Gomez, Frank  and
      Rozovskaya, Alla  and
      Roth, Dan",
    booktitle = "Proceedings of the Second Ukrainian Natural Language Processing Workshop (UNLP)",
    month = may,
    year = "2023",
    address = "Dubrovnik, Croatia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.unlp-1.14",
    pages = "114--120",
    abstract = "We present our system that participated in the shared task on the grammatical error correction of Ukrainian. We have implemented two approaches that make use of large pre-trained language models and synthetic data, that have been used for error correction of English as well as low-resource languages. The first approach is based on fine-tuning a large multilingual language model (mT5) in two stages: first, on synthetic data, and then on gold data. The second approach trains a (smaller) seq2seq Transformer model pre-trained on synthetic data and fine-tuned on gold data. Our mT5-based model scored first in {``}GEC only{''} track, and a very close second in the {``}GEC+Fluency{''} track. Our two key innovations are (1) finetuning in stages, first on synthetic, and then on gold data; and (2) a high-quality corruption method based on roundtrip machine translation to complement existing noisification approaches.",
}
```

```
