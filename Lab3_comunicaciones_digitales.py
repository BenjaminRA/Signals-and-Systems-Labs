import random
import string
import numpy as np
import matplotlib.pyplot as plt
from reedsolo import *

def assertEqual(msg1, msg2):
    if msg1 == msg2:
        return True
    return False

def generate_msgs(length):
    res = ''.join(random.choices(string.ascii_lowercase, k = length))
    return res

def generate_error(msg, err):
    cnt = 0
    for i in range(len(msg)):
        choice = np.random.choice([False, True], p=[1 - err, err])
        if choice:
            msg[i] = np.random.randint(32 , 126)
            cnt += 1

    return [msg, cnt]

def mean(msgs):
    mean = 0.0
    for elem in msgs:
        mean += elem
    mean /= len(msgs)
    return mean

def variance(msgs, mean):
    variance = 0.0

    for elem in msgs:
        variance += (elem - mean)**2

    variance /= len(msgs)
    return variance

if __name__ == "__main__":
    error = float(input("Inserte Probabilidad de Error [0.1, 0.01, 0.001, 0.0001]: "))

    rs = RSCodec(25)
    msgs = [generate_msgs(random.randint(10, 30)) for _ in range(30)]
    enc_msgs = [rs.encode(msg) for msg in msgs]
    err_enc_msgs = [generate_error(msg, error) for msg in enc_msgs]

    for i in range(30):
        enc_msg_decode = rs.decode(enc_msgs[i])
        err_enc_msg_decode = rs.decode(err_enc_msgs[i][0])
        print("msg - dec(enc_msg): ", assertEqual(msgs[i], enc_msg_decode.decode('utf-8')))
        print("msg - dec(err_enc_msg): ", assertEqual(msgs[i], err_enc_msg_decode.decode('utf-8')))
        print("----------------------------------")

    aux = [elem[1] for elem in err_enc_msgs]
    mean = mean(aux)
    variance = variance(aux, mean)

    print(mean, variance)

    plt.xlabel('Mensajes')
    plt.ylabel('Cantidad de errores en cada mensaje')
    plt.plot(range(1, 31), aux, 'ro', label='Errores / Mensaje')
    plt.axhline(y=mean, color='g', linestyle='-', label="Mediana")
    plt.axhline(y=variance, color='b', linestyle='-', label="Varianza")
    plt.axis([1, 30, 0, max(aux) + 1])
    plt.suptitle('Decodificador con {} probabilidad de errores.'.format(error))
    plt.legend(bbox_to_anchor=(1.1, 1), loc='upper left', borderaxespad=0.)
    plt.subplots_adjust(right=.75)
    plt.show()
