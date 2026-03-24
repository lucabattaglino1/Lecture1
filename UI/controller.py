import flet as ft

from gestionale.gestoreOrdini import GestoreOrdini


class Controller:

    def __init__(self, v):
        self._view = v
        self._model = GestoreOrdini()

    def add_ordine(self, e):

        #PRODOTTO
        nomePstr = self._view._txtInNomeP.value

        if nomePstr == "":
            self._view._lvOut.controls.append(ft.Text(value = "Attenzione il campo è vuoto"))
            self._update_page()
            return

        try:
            prezzo = float(self._view._txtInPrezzoP.value)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text(value: "Attenzione il prezzo deve essere un numero", color = "red"))
            self._view.update_page()
            return

        try:
            quantita = int(self._view._txtInQuantita.value)
        except ValueError:
            self._view._lvOut.controls.append( ft.Text(value: "Attenzione la quantità deve essere un intero", color = "red"))
            self._view.update_page()
            return

        #CLIENTE
        nomeC = self._view._txtInNomeC.value

        if nomeC == "":
            self._view._lvOut.controls.append(ft.Text(value = "Attenzione il campo è vuoto"))
            self._update_page()
            return

        mail = self._view._txtInMail.value

        if mail == "":
            self._view._lvOut.controls.append(ft.Text(value = "Attenzione il campo è vuoto"))
            self._update_page()
            return

        categoria = self._view._txtInCategoria.value

        if categoria == "":
            self._view._lvOut.controls.append(ft.Text(value = "Attenzione il campo è vuoto"))
            self._update_page()
            return

        #creo ordine
        ordine = self._model.crea_ordine(nomePstr, prezzo, quantita, nomeC, mail, categoria)

        self._model.add_ordine(ordine)

        # una volta creato l'ordine pulisco
        self._view._txtInNomeP.value = ""
        self._view._txtInPrezzoP.value = ""
        self._view._txtInQuantitaP.value = ""
        self._view._txtInNomeC.value = ""
        self._view._txtInMailP.value = ""
        self._view._txtInCategoriaP.value = ""

        self._view._lvOut.controls.append(ft.Text(value: "Ordine correttamente inserito"), color = "green")
        self._view._lvOut.controls.append(ft.Text("Dettagli ordine: "))
        self._view._lvOut.controls.append(ft.Text(ordine.riepilogo()))
        self._view.update_page()


    def gestisci_ordine(self, e):
        self._view._lvOut.controls.clear()
        risultato, ordine = self._model.processa_prossimo_ordine()

        if risultato:
            self._view._lvOut.controls.append(ft.Text(value = "Ordine correttamente inserito",color = "green"))
            self._view._lvOut.controls.append(ft.Text(ordine.riepilogo()))
            self._view.update_page()
        else:
            self._view._lvOut.controls.append(ft.Text(value = "non ci sono ordini in coda",color = "blue"))
            self._view.update_page()

    def gestisci_all_ordini(self, e):
        self._view._lvOut.controls.clear()
        ordini = self._model.processa_tutti_ordini() #recupero gli ordini dal modello

        if not ordini: #se la lista è vuota
            self._view._lvOut.controls.append(ft.Text(value = "Non ci sono ordini in coda",color = "blue"))
            self._view.update_page()
        else: #se c'è qualcosa nella lista
            self._view._lvOut.controls.append(ft.Text("\n"))
            self._view._lvOut.controls.append(ft.Text(value= f"Ho processato correttamente {len(ordini)}", color="green"))
            for o in ordini:
                self._view._lvOut.controls.append(ft.Text(value=o.riepilogo()))
            self._view.update_page()


    def stampa_sommario(self, e):
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(ft.text(value= "Di seguito il sommario dello stato del business"))
        self._view._lvOut.controls.append(ft.Text(self._model.get_riepilogo()))
        self._view.update_page()

