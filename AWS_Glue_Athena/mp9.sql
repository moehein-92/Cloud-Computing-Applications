SELECT day1 as day, airline1 as airline, view1.origin_airport, view1.destination_airport as stopover_airport, 
view1.departure_delay as origin_departure_delay, view1.arrival_delay as stopover_arrival_delay, 
view2.departure_delay as stopover_departure_delay, view2.arrival_delay as destination_arrival_delay
FROM view1, view2
WHERE view1.airline1=view2.airline2 AND
view1.origin_airport='SFO' AND
view2.destination_airport='JFK' AND
view1.destination_airport=view2.origin_airport AND
view1.cancelled=0 AND
view2.cancelled=0 AND
view1.diverted=0 AND
(view2.day2*1440 + (FLOOR(view2.scheduled_departure/100)*60+view2.scheduled_departure%100) + view2.departure_delay) -
((view1.day1*1440 + (FLOOR(view1.scheduled_departure/100)*60+view1.scheduled_departure%100) + view1.departure_delay + view1.elapsed_time) + 
((FLOOR(view1.scheduled_arrival/100)*60+view1.scheduled_arrival%100)-((FLOOR(view1.scheduled_departure/100)*60+view1.scheduled_departure%100)+
view1.scheduled_time)%1440)) BETWEEN 60 AND 180;
