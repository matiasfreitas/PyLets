import math

#Outras
def find_gcd(NumpyArray):
    """Retorna o Maximo Divisor Comum de um Numpy Array"""
    def gcd(x, y): 
        while y > 0: 
            x, y = y, x % y
        return x
    Ngcd = NumpyArray[0]
    for i in range(1, len(NumpyArray)): 
        Ngcd = gcd(Ngcd, NumpyArray[i])
    return Ngcd
      
def find_lcm(NumpyArray):
    """Retorna o Minimo Multiplo Comum de um Numpy Array"""
    def gcd(x, y): 
        while y > 0: 
            x, y = y, x % y
        return x
    def lcm(x, y):
        return x * y / gcd(x, y) 
    Nlcm = NumpyArray[0]

    for i in range(1, len(NumpyArray)): 
        Nlcm = lcm(Nlcm, NumpyArray[i])
    return Nlcm

def FNysquistForBits (FrequenciaHzs,NiveisBits):
    "Exibe a quantidade de bits por segundo necessária pra amostrar e depois quantizar um sinal"
    value = int(2*FrequenciaHzs*math.log(NiveisBits, 2))   
    print("Frequencia de %i Hzs com %i Niveis"%(FrequenciaHzs,NiveisBits))
    print("Amostragem Minima de %i bits por segundo"%(value))
    return(value)
