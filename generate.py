import argparse
import fileinput
from simplet5 import SimpleT5

def get_line(path_to_data):
    for l in open(path_to_data):
        yield l.strip()

def main(args):
    model = SimpleT5()
    model.load_model("mt5", args.path_to_model, use_gpu=True)
    
    for line in fileinput.input(('-',)):
        line = line.strip('\n')
        print(model.predict(line, 
                        do_sample=False,
                        early_stopping=False,
                        num_beams=5,
                        max_length=128,
                        clean_up_tokenization_spaces=False)[0])

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--path_to_model", type=str, default="output")
    p.add_argument("--orig", type=str)

    args = p.parse_args()
    main(args)
