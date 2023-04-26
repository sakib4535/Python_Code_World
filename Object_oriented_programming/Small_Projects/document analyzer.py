import matplotlib.pyplot as plt
import string

class DocumentAnalyzer:

    def __init__(self, filename):
        self.filename = filename
        self.frequencies = {}
        self.unique_counts = {}

    def analyzer(self):
        with open(self.filename, 'r') as f:
            for line in f:
                for char in line.lower():
                    if char in string.ascii_lowercase:
                        if char in self.frequencies:
                            self.frequencies[char] += 1
                        else:
                            self.frequencies[char] = 1
                self.unique_counts[len(set(line))] = self.unique_counts.get(len(set(line)), 0) + 1
    def plot_frequencies(self):
        if not self.frequencies:
            self.analyzer()

        x = [char for char in self.frequencies.keys()]
        y = [count for count in self.frequencies.values()]
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
        plt.bar(x, y, color=colors[:len(x)])
        plt.title("Frequency of Alphabets")
        plt.xlabel("Alphabets")
        plt.ylabel("Frequency of the Characters")
        plt.show()


    def plot_unique_counts(self):
        if not self.unique_counts:
            self.analyzer()

        x = [char for char in self.unique_counts.keys()]
        y = [freq for freq in self.unique_counts.values()]
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
        plt.bar(x, y, color=colors)
        plt.title("Frequency of Unique Character Counts")
        plt.xlabel("Number of Unique Characters")
        plt.ylabel("Frequency")
        plt.show()

analyzer = DocumentAnalyzer('texting.txt')
analyzer.plot_frequencies()
analyzer.plot_unique_counts()