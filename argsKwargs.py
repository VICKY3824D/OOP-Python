data = {
    "nama" : "Vidky Adhi Pradana",
    "niu" : 84204,
    "alamat" : "Jombang"
}

class Tampil():
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        
    def tampilan(self):
        print(f"Saya {self.kwargs['nama']}")
        
tamp = Tampil(**data)
tamp.tampilan()
