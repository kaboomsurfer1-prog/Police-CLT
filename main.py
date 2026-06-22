# Legacy Police Bot

Bot Discord pentru Poliția Română - Legacy of CLT.

## Funcții

- Pe serverul Poliției, în canalul de demisii, dacă un membru scrie `demisia` sau `demisie` urmat de motiv, botul creează o cerere cu 2 butoane:
  - `Acceptă Demisia`
  - `Refuză Demisia`
- Format pentru cerere:
  - `demisia motivul tău`
  - Exemplu: `demisia Nu mai am timp să activez în facțiune.`
- Motivul demisiei apare în cererea inițială, în loguri și în anunțul de pe serverul principal.
- La acceptare:
  - marchează cererea ca acceptată;
  - calculează câte zile a stat membrul în facțiune, dacă data intrării este setată;
  - trimite log pe serverul Poliției;
  - trimite anunț pe serverul principal FiveM;
  - NU elimină roluri automat. Rolurile se elimină manual.
- La refuz:
  - cere motivul printr-un formular;
  - postează mesajul public cu motivul;
  - trimite log pe serverul Poliției.
- Comenzi staff:
  - `/setintrare membru data` — setează data intrării în facțiune.
  - `/intrare membru` — verifică data intrării și zilele.
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

## Format data intrării

Acceptă:

- `YYYY-MM-DD`, exemplu `2026-06-22`
- `DD/MM/YYYY`, exemplu `22/06/2026`
- `DD-MM-YYYY`, exemplu `22-06-2026`
- `DD.MM.YYYY`, exemplu `22.06.2026`
