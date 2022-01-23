class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __odamlar_soni = 0
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        Shaxs.__odamlar_soni +=1
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
    def __repr__(self):
        return f"Shaxs: {self.ism} {self.familya}. {self.tyil}-yilda tug'ilgan."

    @classmethod
    def get_odamlar_soni(cls):
        return cls.__odamlar_soni
    
class Talaba(Shaxs):
    """Talaba klassi"""
    __talabalar_soni =0
    def __init__(self,ism,familiya,passport,tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []
        Talaba.__talabalar_soni +=1
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    
    def fanga_yozil(self, fan):
        self.fanlar.append(fan)
        return self.fanlar
    
    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            print ("Siz bu fanga yozilmagansiz")
        return self.fanlar

    def __repr__(self):
        return f"Talaba: {self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi."    
    
    def __lt__(self,boshqa_talaba):
        return self.bosqich<boshqa_talaba.bosqich
    
    def __le__(self,boshqa_talaba):
        return self.bosqich<=boshqa_talaba.bosqich
    
    def __eq__(self,boshqa_talaba):
        return self.bosqich==boshqa_talaba.bosqich
    
    @classmethod
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni


talaba1 = Talaba("Valijon","Aliyev","FA112299",2000,"0000012")
talaba2 = Talaba("Sardor","O'rolov","FD15656", 2002, '1165634')
# print(talaba.get_talabalar_soni())
