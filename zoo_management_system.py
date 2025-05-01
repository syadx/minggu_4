from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        if not name or not isinstance(name, str):
            raise ValueError("Nama hewan harus berupa string yang tidak kosong.")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Usia harus berupa bilangan bulat positif.")
        self.__name = name
        self.__age = age

    @abstractmethod
    def make_sound(self):
        pass

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        if name:
            self.__name = name

    def set_age(self, age):
        if isinstance(age, int) and age >= 0:
            self.__age = age

class Dog(Animal):
    def make_sound(self):
        return "Guk Guk!"

class Cat(Animal):
    def make_sound(self):
        return "Meong!"

class Lion(Animal):
    def make_sound(self):
        return "Raawrr!"

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Hanya objek turunan dari Animal yang dapat ditambahkan.")
        self.animals.append(animal)

    def show_animals(self):
        if not self.animals:
            print("Kebun binatang kosong.")
        else:
            print("Daftar Hewan di Kebun Binatang:")
            for idx, animal in enumerate(self.animals, start=1):
                print(f"{idx}. {animal.get_name()} ({animal.__class__.__name__}), usia {animal.get_age()} tahun, suara: {animal.make_sound()}")

def main():
    zoo = Zoo()

    while True:
        print("\n=== Sistem Manajemen Hewan ===")
        print("1. Tambah Hewan")
        print("2. Tampilkan Hewan")
        print("3. Keluar")

        choice = input("Masukkan pilihan (1/2/3): ")
        try:
            if choice == '1':
                jenis = input("Jenis hewan (Dog/Cat/Lion): ").capitalize()
                nama = input("Nama hewan: ").strip()
                usia = int(input("Usia hewan: "))
                if jenis == "Dog":
                    hewan = Dog(nama, usia)
                elif jenis == "Cat":
                    hewan = Cat(nama, usia)
                elif jenis == "Lion":
                    hewan = Lion(nama, usia)
                else:
                    raise ValueError("Jenis hewan tidak dikenal.")
                zoo.add_animal(hewan)
                print("Hewan berhasil ditambahkan!")
            elif choice == '2':
                zoo.show_animals()
            elif choice == '3':
                print("Keluar dari program.")
                break
            else:
                raise ValueError("Pilihan tidak valid.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
