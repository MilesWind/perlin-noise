import random

class noise_layer:
    def __init__(self, shake, scale):
        self.shake = shake;
        self.scale = scale;
        self.offset = random.uniform(-69, 69);

        self.params = [];
        for i in range(len(shake)):
            self.params.append(random.uniform());

    def calculate(self, x):
        total = [];
        for p in self.params:
            total.append(self.scale * p * x + offset);
        return sum(total) / len(total);
