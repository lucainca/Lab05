from dataclasses import dataclass

from networkx.classes import selfloop_edges


@dataclass(order=True)
class Corso:
    codins: str
    crediti: int
    nome: str
    pd: int

    def __str__(self):
        return f"{self.nome} ({self.codins})"



