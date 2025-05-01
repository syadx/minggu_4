
def tampilkan_menu():
    print("\nPilih aksi:")
    print("1. Tambah tugas")
    print("2. Hapus tugas")
    print("3. Tampilkan daftar tugas")
    print("4. Keluar")

def tampilkan_tugas(tugas_list):
    if not tugas_list:
        print("Daftar tugas kosong.")
    else:
        print("Daftar Tugas:")
        for idx, tugas in enumerate(tugas_list, start=1):
            print(f"- {idx}. {tugas}")

def tambah_tugas(tugas_list):
    tugas = input("Masukkan tugas yang ingin ditambahkan: ").strip()
    if not tugas:
        raise ValueError("Tugas tidak boleh kosong.")
    tugas_list.append(tugas)
    print("Tugas berhasil ditambahkan!")

def hapus_tugas(tugas_list):
    if not tugas_list:
        print("Tidak ada tugas untuk dihapus.")
        return
    try:
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if nomor < 1 or nomor > len(tugas_list):
            raise IndexError("Tugas dengan nomor tersebut tidak ditemukan.")
        tugas_terhapus = tugas_list.pop(nomor - 1)
        print(f"Tugas '{tugas_terhapus}' berhasil dihapus.")
    except ValueError:
        print("Input tidak valid. Harap masukkan nomor tugas.")
    except IndexError as e:
        print(f"Error: {e}")

def main():
    tugas_list = []
    while True:
        tampilkan_menu()
        try:
            pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()
            if pilihan == '1':
                tambah_tugas(tugas_list)
            elif pilihan == '2':
                hapus_tugas(tugas_list)
            elif pilihan == '3':
                tampilkan_tugas(tugas_list)
            elif pilihan == '4':
                print("Keluar dari program.")
                break
            else:
                raise ValueError("Pilihan tidak valid. Harap pilih 1, 2, 3, atau 4.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
