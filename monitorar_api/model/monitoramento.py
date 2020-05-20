# -*- coding: utf-8 -*-

class Monitoramento:

    def __init__(self):
        self._id = int()
        self._tab_cad = str()
        self._id_cad = int()

    def listar_mudancas(self):
        return self.__dict__

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def tab_cad(self):
        return self._tab_cad

    @tab_cad.setter
    def tab_cad(self, tab_cad):
        self._tab_cad = tab_cad

    @property
    def id_cad(self):
        return self._id

    @id_cad.setter
    def id_cad(self, id_cad):
        self._id_cad = id_cad







