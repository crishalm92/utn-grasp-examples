
class Person:
    def __init__(self, dni: int):
        self.dni = dni

    def __eq__(self, other):
        return self.dni == other.dni

    def __repr__(self):
        return f"im a person with dni {self.dni}"


class FakeDB:
    table = []

    def search_by_dni(self, dni: int) -> bool:
        for value in self.table:
            if dni == value.dni:
                return True
        return False

    def add_person(self, persona: Person):
        try:
            self.table.append(persona)
            return True
        except:
            return False

    def get_all_values(self) -> list:
        return self.table


class MyController:
    _my_dao = FakeDB()

    def value_in_db(self, dni: int) -> bool:
        if self._my_dao.search_by_dni(dni):
            return True
        return False

    def add_person(self, dni: int) -> bool:
        persona = Person(dni)
        return self._my_dao.add_person(persona)

    def return_all(self) -> list:
        return self._my_dao.get_all_values()


def main() -> None:
    dni = input("Ingrese dni de nueva persona ")
    controller = MyController()
    if not controller.value_in_db(dni):
        controller.add_person(dni)
    else:
        print(f"El campo se encuentra en la lista")

    dni_2 = input("Ingrese otro ")
    if not controller.value_in_db(dni_2):
        controller.add_person(dni_2)
    else:
        print(f"El campo se encuentra en la lista")

    print(controller.return_all())


if __name__ == '__main__':
    main()