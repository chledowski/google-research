import argparse
import os
import math


def reader(filename):
    for row in open(filename, "r"):
        yield row.strip()


def parse_outs(exp_folder, pred_f, evict_f):
    pred_file = os.path.join(exp_folder, 'predictions', pred_f)
    evict_file = os.path.join(exp_folder, 'evictions', evict_f)
    output_file = os.path.join(exp_folder, 'parsed_output', evict_f)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    pred_reader = reader(pred_file)
    evict_reader = reader(evict_file)

    i = 0

    # pred_lines = 0
    # evict_lines = 0
    # for pred_line in pred_reader:
    #     if pred_line == "":
    #         pred_lines += 1
    # for evict_line in evict_reader:
    #     evict_lines += 1
    #
    # print(10, pred_lines, evict_lines)

    in_cache_line = False
    set_dict = {}
    instance_dict = {}
    while i < 200000:
        pred_line = next(pred_reader)
        # print(pred_line)
        if 'PC' in pred_line:
            instance_dict['pc'] = pred_line.split(' ')[1]
        if 'Address' in pred_line:
            instance_dict['address'] = pred_line.split(' ')[1]
        if 'Cache lines' in pred_line:
            in_cache_line = True
            instance_dict['cache_lines_pc'] = []
            instance_dict['cache_lines_address'] = []
            instance_dict['cache_lines_pred_rank'] = []
            instance_dict['cache_lines_prob'] = []
            instance_dict['cache_lines_reuse_distance'] = []
        if 'Attention' in pred_line:
            in_cache_line = False
        if in_cache_line and pred_line[:3] == '|  ':
            cache_line = pred_line.replace(' ', '').split('|')
            instance_dict['cache_lines_pc'].append(cache_line[2])
            instance_dict['cache_lines_address'].append(cache_line[3])
            instance_dict['cache_lines_pred_rank'].append(eval(cache_line[4]))
            instance_dict['cache_lines_prob'].append(eval(cache_line[5]))
            instance_dict['cache_lines_reuse_distance'].append(eval(cache_line[7]))

        if pred_line == "":
            evict_line = eval(next(evict_reader).replace('Infinity', 'math.inf').replace('false', 'False').replace('true', 'True'))
            instance_dict['evict'] = evict_line['evict']

            # assert instance_dict['pc'] == evict_line['pc'], f"PC does not match between pred ({instance_dict['pc']}) and evict ({evict_line['pc']}) file."
            # assert instance_dict['address'] == evict_line[
            #     'address'], f"Address does not match between pred ({instance_dict['address']}) and evict ({evict_line['address']}) file."
            if evict_line['set_id'] in set_dict:
                set_dict[evict_line['set_id']].append(instance_dict)
            else:
                set_dict[evict_line['set_id']] = [instance_dict]
            i += 1
            if i % 1000 == 0:
                print(i)
            # print(f"instance_dict: {instance_dict} \n")
    print(f"set_dict: {set_dict} \n")

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
