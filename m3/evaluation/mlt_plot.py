import matplotlib.pyplot as plt
import json

evaluations = "./evaluation/mlt/evaluation.json"
plot = "./evaluation/mlt"


def plot_evaluation():
    with open(evaluations, 'r') as file:
        data = json.load(file)
        file.close()
    
    similarities = []
    for i in range(len(data)):
        similarities.extend(data[i]['similarities'])
        

    plt.figure(figsize=(10, 6))
    plt.hist(similarities, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title("Histogram of Similarities", fontsize=16)
    plt.xlabel("Similarity Range", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.grid(axis='y', alpha=0.75)
    plt.savefig(f'{plot}/histogram.png')

def main():
    plot_evaluation()
    
if __name__ == "__main__":
    main()