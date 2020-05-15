import numpy as np
from math import floor


class NeuNet:

    def __init__(self, layers, rate, coef):
        self.layers = layers
        self.rate = rate
        self.coef = coef

        self.w1 = np.random.rand(layers[0], layers[1])
        self.w2 = np.random.rand(layers[1], layers[2])

        self.b1 = np.random.rand(layers[1])
        self.b2 = np.random.rand(layers[2])

        self.output = None

    def activ(self, x):

        # activation function

        return x

    def dActiv(self, x):

        # derivative of the activation function
        return 1

    def train(self, x, y, iterations):
        """
            train the nn with the given data and send back the changes
        """
        pos = 0
        for i in range(iterations):
            X = x[pos].T
            Y = y[pos]
            result = self.forward(X)
            self.backwards(X, Y, result)

            pos = (pos + 1) % (len(x))

    def getOutput(self, x, y):
        '''
            actually use the nn
        '''
        pos = 0
        while (pos < len(x)):
            X = x[pos].T
            Y = y[pos]
            print("input: ", str(X[0]))
            output = self.forward(X[0])
            error = self.error(output, Y[0])
            print("computed output:", str(output))
            print("real output:", str(Y))
            print("error: {:.3f}".format(error))
            print("\n")
            pos += 1

    def error(self, computed, real):
        """
            getting the error using the mean squared error formula
        """
        return np.sum((np.square(real - computed)) / 2)

    def forward(self, inpuT):
        """
            here we make the actual computations
        """
        self.output = self.activ(np.dot(inpuT, self.w1) + self.b1)
        return self.activ(np.dot(self.output, self.w2) + self.b2)

    def backwards(self, X, Y, output):
        """
        update the weights
        """
        first = (Y - output) * self.dActiv(output)
        second = np.dot(2 * first, self.w2.T) * self.dActiv(self.output)

        computedW2 = np.dot(self.output.T, 2 * first)
        computedW1 = np.dot(X.T, second)

        self.w1 += self.rate * computedW1 * (1 / self.coef)
        self.w2 += self.rate * computedW2 * (1 / self.coef)


def getData(name):
    x = []
    y = []
    with open(name, "r") as file:
        text = file.readlines()
        for line in text:
            line = line.strip('\n')
            if len(line) == 0:
                continue
            line = line.split()
            line = [[float(x)] for x in line]
            xT = line[:-1]
            yT = line[-1]
            x.append(np.array(xT))
            y.append(np.array(yT))
    return x, y


def split(x, y):
    split = floor(len(y) * 0.75)
    return x[:split], y[:split], x[split:], y[split:]


if __name__ == "__main__":
    noIterations = 1000
    noNeurons = 6
    rate = 0.0001
    coef = 10

    x, y = getData("db2.txt")
    xTrain, yTrain, xTest, yTest = split(x, y)
    layer = [x[0].shape[0], noNeurons, y[0].shape[0]]

    net = NeuNet(layer, rate, coef)
    net.train(xTrain, yTrain, noIterations)
    net.getOutput(xTest, yTest)
