import pickle


class Vehiculo:
    color = ''
    motor = ''
    ruedas = 0
    puertas = ''
    velocidad = 0

    def __init__(self, name, color, motor, ruedas, puertas):
        self.name = name
        self.color = color
        self.motor = motor
        self.ruedas = ruedas
        self.puertas = puertas

    def acelerar(self):
        self.velocidad += 10
        print('velocidad =', self.velocidad)


def save(obj):
    f = open(f'{obj.name}.bin', 'wb')
    pickle.dump(obj, f)
    f.close()


def load(obj):
    f = open(obj+'.bin', 'rb')
    return pickle.load(f)


def main():
    auto = load('auto')
    auto.acelerar()


if __name__ == '__main__':
    main()
