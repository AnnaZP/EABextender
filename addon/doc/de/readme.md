# EAB Extender#

* Autor: LUMEN PL
* Kompatibilität mit NVDA: 2019.3 und hoher

#Beschreibung#
Dieses Add-on ermöglicht es Benutzern, benutzerdefinierte Tastenkombinationen der Easy-Access Bar (EAB) auf Papenmeier-Braillezeilen zuzuweisen. Das Add-on erkennt automatisch die aktive Anwendung, sodass mehrere EAB-Konfigurationen für jede Anwendung erstellt werden können.

Zwischen mehreren Konfigurationen einer Anwendung kann schnell gewechselt werden, wodurch die Funktionalität der EAB erheblich erweitert wird. Beispielsweise kann eine Konfiguration zum Bewegen der Braillezeile in einem Textdokument verwendet werden, während eine andere zur Navigation im Anwendungsmenü dient.

#Kompatible Geräte#
Nachfolgend finden Sie eine Liste kompatibler Papenmeier-Geräte:
* BRAILLEX Live / Live+ / Live 20
* BRAILLEX Trio
* BRAILLEX EL 40c/60c/80c
* BRAILLEX 40s/66s/80s

#Definitionen#
Die Definitionen der in diesem Dokument aufgeführten Tasten entnehmen Sie bitte der Bedienungsanleitung des Geräts.

#Standardeinstellungen#
Standardmäßig verwendet das Papenmeier-Gerät die NVDA-Standardeinstellungen für die EAB, die beim Erstellen einer neuen Konfiguration angewendet werden.
Nachfolgend sind die EAB-Einstellungen der Standardkonfiguration aufgeführt:
* EAB links: verschiebt die Anzeige nach links
* EAB rechts: verschiebt die Braillezeile nach rechts
* EAB oben: verschiebt die Braillezeile eine Spalte nach oben
* EAB unten: verschiebt die Braillezeile eine Spalte nach unten
* Routing + EAB links: bewegt das Navigator-Objekt zum vorherigen Objekt
* Routing + EAB rechts: bewegt das Navigator-Objekt zum nächsten Objekt
* Routing + EAB oben: bewegt das Navigator-Objekt zum übergeordneten Objekt
* Routing + EAB unten: bewegt das Navigator-Objekt zum ersten untergeordneten Objekt

#Hauptmenüfenster#
Um das Hauptmenü zu öffnen, drücken Sie die Taste R1 auf der Papenmeier-Braillezeile. Dieses Menü kann einfach über die EAB bedient werden.

Im Menü des EAB Extender verhält sich die EAB wie folgt:
* Durch Drücken von EAB oben, unten, links oder rechts werden die Pfeiltasten nach oben bzw. unten emuliert, sodass durch die verfügbaren Konfigurationen gescrollt werden kann.
* Routing-Taste + EAB rechts emuliert die Tab-Taste und ermöglicht das Wechseln zwischen den Schaltflächen des Fensters.
* Routing-Taste + EAB links emuliert Shift+Tab und ermöglicht das Wechseln zwischen den Schaltflächen in umgekehrter Reihenfolge.
* Routing-Taste + EAB unten emuliert die Enter-Taste.
* Routing-Taste + EAB oben emuliert die Esc-Taste.

#Schaltflächen des Hauptmenüs#
* OK – aktiviert die ausgewählte Konfiguration und schließt das Fenster.
* Definieren – ermöglicht das Definieren von Tastenkombinationen in einer Konfiguration.
* Name ändern – ändert den Namen der ausgewählten Konfiguration.
* Löschen – löscht die ausgewählte Konfiguration.
* Neu – erstellt eine neue Konfiguration und öffnet ein Dialogfenster zur Namensvergabe.
* Schließen – schließt das Menü ohne Änderungen.

#Konfigurationsfenster#
Dieses Fenster zeigt acht EAB-Positionen, denen benutzerdefinierte Tastenkombinationen zugewiesen werden können.
* Verwenden Sie die Pfeiltasten, um eine EAB-Position auszuwählen.
* Drücken Sie Enter auf einer Position, um den Tastenerfassungsmodus zu aktivieren, und drücken Sie anschließend die gewünschte Tastenkombination, um sie der ausgewählten Position zuzuweisen.
* Wählen Sie anschließend OK, um zu speichern, oder Close, um ohne Speichern zu beenden.

#Braille-Einstellungen#
Durch Drücken der Taste L2 wird ein NVDA-Menü mit den Braille-Einstellungen geöffnet.