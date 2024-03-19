import math
import matplotlib.pyplot as plt
from Generaldistribution import Distribution

class Binomial(Distribution):
    def __init__(self, prob=.5, size =20):
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
        self.n = size
        self.p = prob
    
    def calculate_mean(self):
        self.mean = self.p * self.n

        return self.mean
    
    def calculate_stdev(self):
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))

        return self.stdev
    
    def replace_stats_with_data(self):
        self.n = len(self.data)
        self.p = 1.0 * sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        
        return  self.p, self.n
    
    def plot_bar(self):
        counts = [(1 - self.p) * self.n, self.p * self.n]
        plt.bar([0, 1], counts)
        plt.title ('Barchart of a binomial distribution')
        plt.xlabel('Probability')
        plt.ylabel('Count')

    def pdf(self, k):
        coefficient = math.factorial(self.n) / (math.factorial(k) * (math.factorial(self.n - k)))
        y = (self.p ** k) * (1 - self.p) ** (self.n - k)
                  
        return coefficient * y
    
    def plot_bar_pdf(self):
        x = list(range(self.n + 1))
        y = []
        
        for d in range(self.n+1):
            y_values = self.pdf(d)
            y.append(y_values)
        plt.bar(x,y)
        plt.title ('Barchart of a pdf of a binomial distribution')
        plt.xlabel('Probability')
        plt.ylabel('Count')
        
        plt.show()
                   
        return x,y
                   
    def __add__(self, other):
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        result = Binomial()
        result.n = self.n + other.n 
        result.p = self.p 
        result.mean = result.calculate_mean()
        result.stdev = result.calculate_stdev()
                   
        return result
    
    def __repr__(self):
        
        return "mean {}, standard deviation {}, p {}, n {}".format(self.mean, self.stdev, self.p, self.n)
        
        
