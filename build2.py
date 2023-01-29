class Home:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._rooms = []
        return cls._instance

    def __int__(self):
        pass
    def add_room(self, room):
        self._rooms.append(room)
    def get_rooms(self):
        return self._rooms
FirstHome = Home()
SecondHome = Home()
print(FirstHome is SecondHome)
FirstHome.add_room("Bathroom")
print(FirstHome.get_rooms())
print(FirstHome.get_rooms())
SecondHome.add_room("Dining room")
print(SecondHome.get_rooms())
print(SecondHome.get_rooms())
