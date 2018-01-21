# Pro Scheduler

## URUCHAMIANIE
W folderze Schedule znajdują się dwa podfoldery, w których przechowywane są pliki .py projektu - folder Schedule 
oraz pliki .py aplikacji - ScheduleApp. Plik db.sqlite3 reprezentuje bazę danych, natomiast plik manage.py służy do
uruchomienia aplikacji ScheduleApp. 
1. Aby uruchomić aplikację w systemie Windows, należy ustawić w wierszu polecenia
 katalog na Schedule i uruchomić aplikację poleceniem:

>python manage.py runserver

2. Adres serwera, na podany będzie poniżej(Starting development server at...) np.:

Performing system checks...

System check identified no issues (0 silenced).
May 30, 2016 - 14:21:54
Django version 1.9.6, using settings 'Schedule.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

W przeglądarke należy wpisać adres:

http://127.0.0.1:8000/ScheduleApp

## DZIAŁANIE

Aplikacja na stronie głównej(/ScheduleApp/) daje możliwość dodawania i usuwania dni z listy. Widoczne 
są też wszystkie zaplanowane dni oraz ilość zadań jaka została wpisana na dany dzień.

Po kliknięciu na link do danego dnia użytkownik zostaje przekierowany na strone planowania zadań(/ScheduleApp/5/daytasks/)
na dany dzień. Może podejrzeń, dodać lub usunąć zadania.

Po kliknięciu na link NewDay na stronie głównej, użytkownik zostaje przekierowany na stronę dodawania dnia, gdzie może wybrać datę 
i po zatwierdzeniu jest przekierowany spowrotem na stronę główną. 





