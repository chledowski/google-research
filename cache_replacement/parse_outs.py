import argparse
import os


def parse_outs(exp_folder, pred_f, evict_f):

    pred_file = os.path.join(exp_folder, 'predictions', pred_f)
    evict_file = os.path.join(exp_folder, 'evictions', evict_f)
    output_file = os.path.join(exp_folder, 'parsed_output', evict_f)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(pred_file, 'r') as f_p:
        with open(evict_file, 'r') as f_e:
            with open(output_file, 'w') as f_o:
                predictions = f_p.readlines()
                evictions = f_e.readlines()
                for line in predictions[:60]:
                    print(line.strip())
                print()
                print(2, evictions[:2])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse output files")
    parser.add_argument('--exp-folder', required=True)
    parser.add_argument('--pred-file', required=True)
    parser.add_argument('--evict-file', required=True)

    args = parser.parse_args()

    parse_outs(args.exp_folder, args.pred_file, args.evict_file)
