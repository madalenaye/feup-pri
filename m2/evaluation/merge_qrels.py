import argparse

parser = argparse.ArgumentParser(description='Merge qrel files and query responses to trec evaluate')
# Set up argument parser

# First qrel file
parser.add_argument('qrel_file_txt', type=str, help='The file containing first to be merged qrel data.')
# Second qrel file
parser.add_argument('qrel_file2_txt', type=str, help='The file containing second to be merged qrel data.')
# Output merged response file
parser.add_argument("output_merged_qrels_txt", type=str, help="The file to save the merged responses data.")

# Parse arguments
args = parser.parse_args()

with open(args.qrel_file_txt, 'r') as qrel1:
    qrel_lines = qrel1.readlines();
    with open(args.qrel_file2_txt, 'r') as qrel2:
        qrel_lines2 = qrel2.readlines();
        qrel_lines2.append("\n");
        with open(args.output_merged_qrels_txt, 'w') as output_qrel:
            for line in qrel_lines:
                if line not in qrel_lines2:
                    qrel_lines2.append(line);
            output_qrel.writelines(qrel_lines2);


print(f"Merged qrel files have been saved to {args.output_merged_qrels_txt}.")
# Command to run below for ASh gym battle
# python3 merge_eval_trec.py ashBattle/simple_system/qrels.txt ashBattle/complex_system/qrel.txt ashBattle/simple_system/response.txt ashBattle/complex_system/response.txt ashBattle/merged_qrels.txt ashBattle/merged_response.txt