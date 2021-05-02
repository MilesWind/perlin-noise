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


class noise_map:
    def __init__(self, dementions, shake, scale):
        self.dementions = dementions;
        self.shake = shake;
        self.scale = scale;

        layers = [];
        
        for i in range(dementions):
            layers.append(noise_layer(shake, scale));

    def calculate(self, pos):
        total = [];
        for i in range(self.dementions):
            total.append(layers[i].calculate(pos[i]));
        return sum(total) / len(total);
