#PATRÓN Y SU DURACIÓN
play :c4
sleep 1
play :e4
sleep 0.5
play :g4

#FUNCIONES
define :kick do
  sample :bd_haus
end

define :bass do
  play :c2
end

#THEN
kick
bass



#INSTRUMENTO
live_loop :drums do
  sample :bd_haus
  sleep 1
end

live_loop :bass do
  play :c2
  sleep 1
end


#COSAS IND

times do

loop do

ring

#EJ

notes = (ring :c3,:e3,:g3,:b3)

play notes.tick
sleep 0.5


set :energy, 0.6
get(:energy)


#SINCRONIZACIÓN

sync :bar
live_loop :clock do
  cue :bar
  sleep 4
end

live_loop :melody do
  sync :bar
  ...
end

#VARIABLES MUSICALES

escala = scale(:c3,:minor)

play escala.choose

#PARÁMETROS

play :c4,
  cutoff: 80,
  release: 0.5,
  amp: 0.7



#EFEKTOS (contenedores)

with_fx :reverb do
  play :c4
end

with_fx :echo do
  live_loop :lead do
    ...
  end
end


#ALEATORIEDAD CONTROLADA

play scale(:c3,:minor).choose

rrand(70,110)
use_random_seed 1234


#tips AGRUPAR

## INTRO

## DRUMS

## BASS

## PAD

## LEAD

## FX

#FLUJO

Clock, -drumms, -bass, -chords, -lead, -atmosphere, -effects ~


Tiempo: reloj, compases, tempo y sincronización.
Material: escalas, acordes, ritmos, muestras y motivos.
Comportamiento: reglas de repetición, variación, probabilidad y evolución.
Forma: introducción, desarrollo, clímax y cierre, o cualquier otra macroestructura.




