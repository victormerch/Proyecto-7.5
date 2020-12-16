-- 1 Mostrar la Carta inicial más repetida por cada jugador(mostrar nombre jugador y carta). 

-- 2 Jugador que realiza la apuesta más alta por partida. (Mostrar nombre jugador).
select nombre,max(apuesta),idpartida from
(select case 
when username is not null then usuario.username 
else descripcion end
as nombre,max(turnos.apuesta) as apuesta,partida.idpartida as idpartida from jugador
left join bot 
on bot.idbot=jugador.idbot
left join usuario 
on usuario.idusuario=jugador.idusuario
inner join participante 
on jugador.idjugador=participante.id_jugador
inner join turnos 
on participante.id_participante=turnos.idparticipante
inner join partida 
on turnos.idpartida=partida.idpartida
where turnos.apuesta is not null
group by partida.idpartida,username) tabla
where (apuesta,idpartida) in (select 
max(turnos.apuesta),partida.idpartida  as apuesta from jugador
left join bot 
on bot.idbot=jugador.idbot
left join usuario 
on usuario.idusuario=jugador.idusuario
inner join participante 
on jugador.idjugador=participante.id_jugador
inner join turnos 
on participante.id_participante=turnos.idparticipante
inner join partida 
on turnos.idpartida=partida.idpartida
group by partida.idpartida
order by max(turnos.apuesta) desc
)
group by idpartida;

-- 3 Jugador que realiza apuesta más baja por partida. (Mostrar nombre jugador).
select nombre,min(apuesta),idpartida from
(select case 
when username is not null then usuario.username 
else descripcion end
as nombre,min(turnos.apuesta) as apuesta,partida.idpartida as idpartida from jugador
left join bot 
on bot.idbot=jugador.idbot
left join usuario 
on usuario.idusuario=jugador.idusuario
inner join participante 
on jugador.idjugador=participante.id_jugador
inner join turnos 
on participante.id_participante=turnos.idparticipante
inner join partida 
on turnos.idpartida=partida.idpartida
where turnos.apuesta is not null
group by partida.idpartida,username) tabla
where (apuesta,idpartida) in (select 
min(turnos.apuesta),partida.idpartida  as apuesta from jugador
left join bot 
on bot.idbot=jugador.idbot
left join usuario 
on usuario.idusuario=jugador.idusuario
inner join participante 
on jugador.idjugador=participante.id_jugador
inner join turnos 
on participante.id_participante=turnos.idparticipante
inner join partida 
on turnos.idpartida=partida.idpartida
group by partida.idpartida
order by min(turnos.apuesta) desc
)
group by idpartida;

-- 4 Ratio  de turnos ganados por jugador en cada partida (%),mostrar columna Nombre jugador, Nombre partida, nueva columna "porcentaje %".

-- 5 Porcentaje de partidas ganadas Bots en general. Nueva columna "porcentaje %".
select *from ( select round(count(ganador_partida)*100/count(idpartida)) as "Porcentaje %" 
from partida p
inner join participante pa 
on p.ganador_partida=pa.id_participante
inner join jugador j 
on pa.id_jugador=j.idjugador
inner join bot b 
on j.idbot=b.idbot
where ganador_partida=pa.id_participante) as contador;

-- 6 Mostrar los datos de los jugadores y el tiempo que han durado sus partidas ganadas cuya puntuación obtenida es mayor que la media puntos de las partidas ganadas totales.

-- 7 Cuántas rondas se ganan en cada partida según el palo. Ejemplo: Partida 1 - 5 rondas - Bastos como carta inicial.

select idpartida as Partida, count(numero_turno) as Rondas_Ganadas, descripcion as Palo from turnos t
left join cartas c
on t.carta_inicial = c.idcartas
left join tipo_carta tc
on c.tipo = tc.idtipo_carta 
where puntos_final > puntos_inicio
group by idpartida, Palo;

-- 8 Cuantas rondas gana la banca en cada partida.

select idpartida as Partida,count(numero_turno) as Rondas_Ganadas from turnos t
left join cartas c
on t.carta_inicial = c.idcartas
left join tipo_carta tc
on c.tipo = tc.idtipo_carta 
where puntos_final > puntos_inicio and es_banca = 1
group by idpartida;

-- 9 Cuántos usuarios han sido la banca en una partida.
select count(es_banca) as usuario_banca, idpartida 
from turnos
where es_banca=1
group by idpartida;

-- 10 Partida con la puntuación más alta final de todos los jugadores, mostrar nombre jugador, nombre partida,así como añadir una columna nueva en la que diga si ha ganado la partida o no.

-- 11 Calcular la apuesta media por partida.

select avg(apuesta) as Apuesta_media, idpartida from turnos
group by idpartida;

-- 12 Mostrar los datos de los usuarios que no son bot, así como cual ha sido su última apuesta en cada partida que ha jugado.

-- 13 Calcular el valor total de las cartas y el numero total de cartas que se han dado inicialmente en las manos en la partida. Por ejemplo, en la partida se han dado 50 cartas y el valor total de las cartas es 47,5.

-- 14 Diferencia de puntos de los participantes de las partidas entre la ronda 1 y 5. Ejemplo: Rafa tenia 20 puntos, en la ronda 5 tiene 15, tiene -5 puntos de diferencia.

select turno5.p2-turno1.p1 Diferencia_puntos 
from (select distinct puntos_inicio p1 
from turnos t 
where numero_turno = 1 group by idpartida) turno1, 
( select puntos_inicio p2 
from turnos 
where numero_turno = 5) turno5;
