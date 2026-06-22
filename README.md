# Legacy Police Bot

Bot Discord pentru Poliția Română - Legacy of CLT.

## Funcții

- Pe serverul Poliției, în canalul de demisii, dacă un membru trimite modelul corect, botul creează o cerere cu 2 butoane:
  - `Acceptă Demisia`
  - `Refuză Demisia`
- Format pentru cerere:

```text
Nume: numele tău
Ore: numărul de ore
Motiv: motivul demisiei
```

- Exemplu:

```text
Nume: Jmarok
Ore: 120
Motiv: Nu mai am timp să activez în facțiune.
```

- Botul acceptă și varianta cu `demisia` / `demisie` înainte de model:

```text
demisia
Nume: Jmarok
Ore: 120
Motiv: Nu mai am timp să activez în facțiune.
```

- `Nume`, `Ore` și `Motiv` apar în cererea inițială, în loguri și în anunțul de pe serverul principal.
- Demisia poate fi depusă doar dacă data și ora intrării sunt setate pentru membru. Dacă nu sunt setate, botul respinge cererea și cere conducerii să folosească `/setintrare`.
- La acceptare:
  - marchează cererea ca acceptată;
  - calculează exact cât timp a stat membrul în facțiune, pe zile, ore și minute;
  - trimite log pe serverul Poliției;
  - trimite anunț pe serverul principal FiveM;
  - NU elimină roluri automat. Rolurile se elimină manual.
- La refuz:
  - cere motivul refuzului printr-un formular;
  - postează mesajul public cu motivul;
  - trimite log pe serverul Poliției.
- Comenzi staff:
  - `/setintrare membru data ora` — setează data și ora intrării în facțiune.
  - `/intrare membru` — verifică data/ora intrării și timpul exact în facțiune.
  - `/demisii limit` — arată ultimele cereri.

## Railway

1. Creează un repo GitHub cu aceste fișiere.
2. Railway → New Project → Deploy from GitHub.
3. În Railway → Variables adaugă valorile din `.env.example`, mai ales `DISCORD_TOKEN`.
4. Recomandat: creează un Volume și montează-l la `/data`, deoarece baza SQLite se salvează la `/data/legacy_police.db`.
5. Start command: `python main.py`

## Discord Developer Portal

Activează la bot:

- `MESSAGE CONTENT INTENT`
- `SERVER MEMBERS INTENT`

## Permisiuni bot

Botul are nevoie de:

- View Channels
- Send Messages
- Embed Links
- Read Message History
- Use Slash Commands
- Manage Messages doar dacă setezi `DELETE_TRIGGER_MESSAGE=true`

## Format data și ora intrării

Comanda se folosește așa:

```text
/setintrare @membru 22/06/2026 20:30
```

Format dată acceptat:

- `YYYY-MM-DD`, exemplu `2026-06-22`
- `DD/MM/YYYY`, exemplu `22/06/2026`
- `DD-MM-YYYY`, exemplu `22-06-2026`
- `DD.MM.YYYY`, exemplu `22.06.2026`

Format oră acceptat:

- `HH:MM`, exemplu `20:30`
- `HH`, exemplu `20` pentru `20:00`

## Versiune

Versiune curentă: `1.0.5-data-ora-intrare`

În Railway logs trebuie să apară:

```text
Versiune bot: 1.0.5-data-ora-intrare
```

Dacă nu apare această versiune în logs, Railway rulează încă un `main.py` vechi.
