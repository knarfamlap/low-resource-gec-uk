import os
import argparse
import pandas as pd
from simplet5 import SimpleT5
from distutils import util
from pytorch_lightning.loggers import WandbLogger

def load_data(path_to_train_tsv, path_to_valid_tsv):
    train = pd.read_csv(os.path.join(path_to_train_tsv), sep="\t", 
                names=["source_text", "target_text"],
                on_bad_lines="skip",
                header=None)
    train = train.applymap(str)
    
    val = pd.read_csv(os.path.join(path_to_valid_tsv), sep="\t",
                names=["source_text", "target_text"],
                on_bad_lines="skip",
                header=None)

    val = val.applymap(str)

    return train, val

def main(args):
    model = SimpleT5()
    
    if args.from_local:
        model.from_pretrained(args.model_type, args.model_name)
    else:
        model.from_pretrained(args.model_type, f"google/{args.model_name}")

    train_df, val_df = load_data(args.train_tsv, args.valid_tsv) 
    model.train(train_df=train_df, # pandas dataframe with 2 columns: source_text & target_text
            eval_df=val_df, # pandas dataframe with 2 columns: source_text & target_text
            source_max_token_len = 128, 
            target_max_token_len = 128,
            batch_size = args.batch_size,
            max_epochs = args.max_epochs,
            use_gpu = True,
            outputdir = args.output_dir,
            early_stopping_patience_epochs = 2,
            dataloader_num_workers = 16,
            precision = 'bf16'
        )

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--train_tsv", type=str, required=True)
    p.add_argument("--valid_tsv", type=str, required=True)
    p.add_argument("--output_dir", type=str, default="output")
    p.add_argument("--model_type", type=str, default="mt5")
    p.add_argument("--model_name", type=str, default="mt5-large")
    p.add_argument("--batch_size", type=int, default=2)
    p.add_argument("--max_epochs", type=int, default=4)
    p.add_argument("--from_local", type=lambda x: bool(util.strtobool(x)), default=False, 
                                help="Is model_name a path or the name of the mt5 model")

    args = p.parse_args()
    main(args)
