clear
clc
Float = [0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 1];

n=0;
e=0;
mantissa=0;
r=-1;

for i=9:-1:2
    e = e + Float(i)*2^n;
    n = n + 1
end

% aca estoy asumiendo que el exponenete es normalizado
exp = e - 127

for i=10:16
    mantissa = mantissa + Float(i)*2^r;
    r = r - 1
end

decimal = (-1)^Float(1)*(1+mantissa)*2^exp
