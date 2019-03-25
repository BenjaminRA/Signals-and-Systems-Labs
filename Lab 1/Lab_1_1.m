[y, sr] = audioread('C:\Users\depre\Desktop\muestrasguitarra\muestras_guitarra\acoustic.wav');

% La duración de cada muestra
dt = 1/sr;

% Vector tiempo que va desde 0 hasta el largo del original en pasos de dt
% para mostrar todas las muestras
t = 0:dt:(length(y)*dt)-dt;

% Vector con la cantidad de retardo correspondiente a cada eco
delay_sec = [0.0001 0.0002 0.0003];

max = 0;
for i = 1:length(delay_sec)
    if max < delay_sec(i)
        max = delay_sec(i);
    end
end

t_total = 0:dt:((length(y)+floor(sr*max))*dt)-dt;
final = cat(2, y', zeros(1, floor(sr*max)));
hold on;
grid;
xlabel('Seconds'); 
ylabel ('Amplitude');
plot(t_total, final);
for i = 1:length(delay_sec)
    % Concatenar el vector de 0 al principio con la señal original para crear el
    % Efecto de Eco
    delay = (cat(2, zeros(1, floor(sr*delay_sec(i))), y'));
    delay = cat(2, delay, zeros(1, (length(y)+floor(sr*max))-length(delay)));
    fade = (cat(2, zeros(1, floor(sr*delay_sec(i))), 1:-1/length(y):0));
    fade = cat(2, fade, zeros(1, (length(y)+floor(sr*max))-length(fade)));
    for j = 1:length(delay)
       delay(j) = delay(j)*fade(j);
       final(j) = final(j)+delay(j);
    end
    plot(t_total, delay);
end
plot(t_total, final);
hold off;
sound(final, sr)
