import dataclasses


@dataclasses.dataclass
class Studente:
    matricola: int
    nome: str
    cognome: str
    CDS: str

    def __str__(self):
        return f" {self.nome},  {self.cognome} ({self.matricola})"
