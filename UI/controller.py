import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self,e):
        dist = self._view.txt_distanza.value
        if dist is None or dist == "" or not dist.isdigit():
            self._view.create_alert("Inserire la distanza")
            return

        lista_archi = []
        dist = int(dist)
        self._model.buildGraph(dist)
        lista_archi = self._model._grafo.edges()

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene: {self._model.getNumNodi()} nodi"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene: {self._model.getNumArchi()} archi"))
        #for arco in lista_archi:
           # self._view.txt_result.controls.append(ft.Text(str(lista_archi)))
        n = 1
        for arco in lista_archi:
            self._view.txt_result.controls.append(ft.Text(f"tratta {n}: {arco}"))
            n +=1


        self._view.update_page()