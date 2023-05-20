flight(msk, spb).
flight(msk, ekt).
flight(msk, novos).
flight(spb, novos).
flight(spb, sochi).
flight(spb, minsk).
flight(ekt, sochi).
flight(sochi, kiev).
flight(minsk, novos).
flight(minsk, kiev).

linked(X, Y) :- flight(X, Y).
linked(X, Y) :- 
	flight(X, Z),
	linked(Z, Y).
