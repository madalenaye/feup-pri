#!/usr/bin/env python3

import argparse
import sys


def qrels_to_trec(qrels: list, query_id: int) -> None:
    """
    Converts qrels (query relevance judgments) to TREC evaluation format.

    Arguments:
    - qrels: A list of qrel lines (document IDs) from standard input.
    """
    for line in qrels:
        doc_id = line.strip().split()
        if (doc_id[1] == "1"):
            print(f"{query_id} 0 {doc_id[0]} 1")


if __name__ == "__main__":
    # Set up argument parsing for command-line interface
    parser = argparse.ArgumentParser(description="Read qrels from stdin and output them in TREC format.")

    # Add argument for optional run ID
    parser.add_argument(
        "--query-id",
        type=int,
        help="Query identifier.",
    )

    # Parse command-line arguments
    args = parser.parse_args()
    qrels = sys.stdin.readlines()
    qrels_to_trec(qrels, args.query_id)
