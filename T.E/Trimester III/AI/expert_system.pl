
/*Medical Diagnosis expert system*/
go:-
hypothesis(Disease),
write('The patient might be having '),
write(Disease),
nl,
write('TAKE CARE '),
undo.

/*Hypothesis that should be tested*/
hypothesis(cold) :- cold, !.
hypothesis(flu) :- flu, !.
hypothesis(typhoid) :- typhoid, !.
hypothesis(measles) :- measles, !.
hypothesis(malaria) :- malaria, !.
hypothesis(unknown). /* no diagnosis*/

/*Hypothesis Identification Rules*/

cold :-
verify(headache),
verify(runny_nose),
verify(sneezing),
verify(sore_throat),
nl.

flu :-
verify(fever),
verify(headache),
verify(chills),
verify(body_ache),
nl.

typhoid :-
verify(headache),
verify(abdominal_pain),
verify(poor_appetite),
verify(fever),
nl.

measles :-
verify(fever),
verify(runny_nose),
verify(rash),
verify(conjunctivitis),
nl.

malaria :-
verify(fever),
verify(sweating),
verify(headache),
verify(nausea),
verify(vomiting),
verify(diarrhea),
nl.

/* how to ask questions */
ask(Question) :-
write('Does the patient have following symptom:'),
write(Question),
write('? '),
read(Response),
nl,
( (Response == yes ; Response == y)
->
assert(yes(Question)) ;
assert(no(Question)), fail).

:- dynamic yes/1,no/1.
/*How to verify something */
verify(S) :-
(yes(S)
 ->
true ;
(no(S)
 ->
fail ;
ask(S))).
/* undo all yes/no assertions*/
%undo :- retract(yes(_)),fail.
%undo :- retract(no(_)),fail.
undo.



/*
OUTPUT
% /home/stuff/code/mit-stuff/t9/ai/expert_system.pl
1 ?- go.
Does the patient have following symptom:headache? y.
Does the patient have following symptom:runny_nose? y.
Does the patient have following symptom:sneezing? y.
Does the patient have following symptom:sore_throat? y.
The patient might be having cold
TAKE CARE
true.
2 ?- y.
*/
