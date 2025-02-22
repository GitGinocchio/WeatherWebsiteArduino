# WeatherWebsiteArduino

Api: https://wttr.in/Città?format=j1

Documentazione relativa all'API: https://github.com/chubin/wttr.in

Si sostituisce città con la città di cui si vuole ottenere i dati

Dall'API raccogliamo:

- Pressione
- Temperatura
- Visibilità
- Umidità
- e Data Attuale
- ... magari anche altro

## Backend Sito

Il Backend del sito lo facciamo con la libreria Flask

Documentazione relativa a Flask: https://github.com/pallets/flask

Strutturiamo il sito in queste Route (o pagine):

Daniele (Pier):
- /                     (Home)
- /login & /register    (Forse la facciamo)
- /search               (Pagina per cercare una città o un paese)

>[!IMPORTANT]
> La pagina search potrebbe essere anche la stessa della home
> Quindi appena entri nel sito ti trovi la pagina per cercare la città

Giulio
- /weather              (Pagina per vedere con grafici i risultati ecc.)

>[!IMPORTANT]
> Per visualizzare i dati si può usare matplotlib
> attraverso la libreria si può creare un grafico con i dati raccolti dall'API

## Frontend Sito


>[!NOTE]
> Potete scrivere la procedura che volete attuare qui...
