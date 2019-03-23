[y, sr] = audioread('C:\Users\depre\Desktop\muestrasguitarra\muestras_guitarra\acoustic.wav');

% La duración de cada muestra
dt = 1/sr;

% Vector tiempo que va desde 0 hasta el largo del original en pasos de dt
% para mostrar todas las muestras
t = 0:dt:(length(y)*dt)-dt;

compression = 80000;

% Creo un vector de 0 con el largo correspodiente al nuevo muestreo
final = zeros(1, length(y)-compression);

% Para ver en que divisor de compression vamos en la iteración
counter = 1;


for i = 1:length(y)
    % Si el numero es divisor de la compression no lo agregamos y
    % aumentamos el contador
    if i == floor(length(y)*counter/compression)
        counter = counter + 1;
    else
        final(i - (counter-1)) = y(i);
    end
end

sound(final, (sr*length(final)/length(y))); % para que se escuche a la misma velocidad
x = 0:dt:(length(y)*dt)-dt;
hold on;
plot(x, y);
plot(x, [final zeros(1, length(y)-length(final))]);
hold off;
grid;
xlabel('Seconds'); 
ylabel ('Amplitude');