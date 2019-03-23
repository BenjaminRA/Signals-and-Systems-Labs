[y, sr] = audioread('C:\Users\depre\Desktop\muestrasguitarra\muestras_guitarra\acoustic.wav');

% La duración de cada muestra
dt = 1/sr;

% Vector tiempo que va desde 0 hasta el largo del original en pasos de dt
% para mostrar todas las muestras
t = 0:dt:(length(y)*dt)-dt;

times = 1;

% Creo un vector de 0 con el largo correspodiente al nuevo muestreo
final = zeros(1, length(y)*(times+1));

% Itero el vector final en pasos de los 0 que queremos poner entre
% cada valor, en cada iteración solo copiamos el valor correspondiente a
% esa muestra ya que tenemos los 0 listos
for i = (times+1):(times+1):length(final)
    final(i) = y(i/(times+1));
end

% sound(final, sr);
x = 0:dt:(length(final)*dt)-dt;
hold on;
plot(x, [y' zeros(1, length(final)-length(y))]);
plot(x, final);
hold off;
grid;
xlabel('Seconds'); 
ylabel ('Amplitude');