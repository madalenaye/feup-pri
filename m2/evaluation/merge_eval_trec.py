import argparse

parser = argparse.ArgumentParser(description='Merge qrel files and query responses to trec evaluate')
# Set up argument parser

# First qrel file
parser.add_argument('qrel_file_txt', type=str, help='The file containing first to be merged qrel data.')
# Second qrel file
parser.add_argument('qrel_file2_txt', type=str, help='The file containing second to be merged qrel data.')
# First query response file
parser.add_argument('query_response_txt', type=str, help='The file containing response data.')
# Second query response file
parser.add_argument('query_response2_txt', type=str, help='The file to save the merged data.')
# Output merged qrel file
parser.add_argument("output_merged_qrels_txt", type=str, help="The file to save the merged qrels data.")
# Output merged response file
parser.add_argument("output_merged_responses_txt", type=str, help="The file to save the merged responses data.")

# Parse arguments
args = parser.parse_args()

with open(args.qrel_file_txt, 'r') as qrel1:
    qrel_lines = qrel1.readlines();
    with open(args.qrel_file2_txt, 'r') as qrel2:
        qrel_lines2 = qrel2.readlines();
        with open(args.output_merged_qrels_txt, 'w') as output_qrel:
            for line in qrel_lines:
                if line not in qrel_lines2:
                    qrel_lines2.append(line);
            output_qrel.writelines(qrel_lines2);

with open(args.query_response_txt, 'r') as response1:
    response_lines = response1.readlines()
    with open(args.query_response2_txt, 'r') as response2:
        response_lines2 = response2.readlines()
        with open(args.output_merged_responses_txt, 'w') as output_response:
            seen_third_words = set()
            temp = []
            for line in response_lines:
                words = line.split()
                if len(words) > 2:
                    seen_third_words.add(words[2])
                temp.append(line)
            for line2 in response_lines2:
                words2 = line2.split()
                if len(words2) > 2 and words2[2] in seen_third_words:
                    continue
                temp.append(line2)
                if len(words2) > 2:
                    seen_third_words.add(words2[2])
            output_response.writelines(temp)
print(f"Merged qrel and response files have been saved to {args.output_merged_qrels_txt} and {args.output_merged_responses_txt} respectively.")
# Command to run below for ASh gym battle
# python3 merge_eval_trec.py ashBattle/simple_system/qrels.txt ashBattle/complex_system/qrel.txt ashBattle/simple_system/response.txt ashBattle/complex_system/response.txt ashBattle/merged_qrels.txt ashBattle/merged_response.txt