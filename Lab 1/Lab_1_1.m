[y, sr] = audioread('C:\Users\depre\Desktop\muestrasguitarra\muestras_guitarra\acoustic.wav');

% La duración de cada muestra
dt = 1/sr;

% Vector tiempo que va desde 0 hasta el largo del original en pasos de dt
% para mostrar todas las muestras
t = 0:dt:(length(y)*dt)-dt;

delay_sec = 1;
cantidad = 1;

% Concatenar el vector de 0 al principio con la señal original para crear el
% Efecto de Eco
delay = (cat(2, zeros(1, floor(sr*delay_sec)), y'))';
t_delay = 0:dt:(length(delay)*dt)-dt;

fade = 1:-1/length(y):0;
for i = 1:length(y)
    delay(i + floor(sr*delay_sec)) = delay(i + floor(sr*delay_sec))*fade(i);
end

final = cat(2, y', zeros(1, floor(sr*delay_sec))) + delay'.*cantidad;
% sound(final, sr);
x = 0:dt:(length(final)*dt)-dt;
hold on;
plot(x, delay);
% plot(x, cat(2, y', zeros(1, floor(sr*delay_sec))));
hold off;
grid;
xlabel('Seconds'); 
ylabel ('Amplitude');