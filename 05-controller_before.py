

class FakeDB:
    table = []


class Person:
    def __init__(self, dni: int):
        self.dni = dni

    def __eq__(self, other):
        return self.dni == other.dni


def main() -> None:
    _db = FakeDB()
    dni = input("Ingrese dni de nueva persona ")
    persona = Person(dni)
    if persona not in _db.table:
        _db.table.append(persona)
    else:
        print(f"El campo se encuentra en la lista")

    dni_2 = input("Ingrese otro ")
    persona_2 = Person(dni_2)
    if persona_2 not in _db.table:
        _db.table.append(persona)
    else:
        print(f"El campo se encuentra en la lista")

    print(_db.table)

if __name__ == '__main__':
    main()