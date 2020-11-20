import argparse
import os


def reader(filename):
    for row in open(filename, "r"):
        yield row.strip


def parse_outs(exp_folder, pred_f, evict_f):

    pred_file = os.path.join(exp_folder, 'predictions', pred_f)
    evict_file = os.path.join(exp_folder, 'evictions', evict_f)
    output_file = os.path.join(exp_folder, 'parsed_output', evict_f)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    pred_reader = reader(pred_file)
    evict_reader = reader(evict_file)

    print(pred_reader)
    print(next(pred_reader))
    print(next(pred_reader))
    print(next(pred_reader))
    print(next(pred_reader))
    print(next(pred_reader))
    print(next(pred_reader))
    print(next(pred_reader))
    print(next(pred_reader))
    print(next(pred_reader))
    print(next(pred_reader))
    print(next(pred_reader))
    # with open(pred_file, 'r') as f_p:
    #     with open(evict_file, 'r') as f_e:
    #         with open(output_file, 'w') as f_o:
    #             for line in f_p:
    #                 print(line.strip())
    #                 if line.strip() == "":
    #                     print(1)
    #                     break
    #             # predictions = f_p.readlines()
    #             evictions = f_e.readlines()
    #             # for line in predictions[:30]:
    #             #     print(line.strip())
    #             print()
    #             for line in evictions[:2]:
    #                 print(line.strip())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse output files")
    parser.add_argument('--exp-folder', required=True)
    parser.add_argument('--pred-file', required=True)
    parser.add_argument('--evict-file', required=True)

    args = parser.parse_args()

    parse_outs(args.exp_folder, args.pred_file, args.evict_file)
