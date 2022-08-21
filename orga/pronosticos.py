def mm(data, n):
    num = 0
    for x in data:
        num += x
    return num/n

def mmp(data, ponds, n):
    num = 0
    for i in range(0, len(data)):
        num += data[i]*ponds[i]
    den = 0
    for i in ponds:
        den += i
    return num/den

# a es el coeficiente de alisado (constante de alisado)
# d_ant es la demanda real del periodo anterior
# f_ant es la estimacion del periodo anterior (f de forecast)
# calcula el siguiente termino de la sucesion de suavizamiento exponencial
def suav_e(a, d_ant, f_ant):
    return f_ant + a*(d_ant-f_ant)

# calcula el termino n de la sucesion de suavizamiento exponencial
def nsuav_e(data, a, d_ant, f_ant):
    ans = f_ant
    for x in data:
        ans = suav_e(a, x, ans)
    return ans