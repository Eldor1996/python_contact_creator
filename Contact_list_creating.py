#Foydalanuvchini kutib oladigan va dastur haqida ma'lumot beruvchi funksiya yaratish
def Kirish():
    
    tanlov = int(input("""Pythondaki Konaktlar dasturiga xush kelibsiz.  
                    
                    >>> Mavjud amallar ro'yxati ?<<<
                    1. Mavjud Kontaktlarni ko'rsatish
                    2. Yangi Kontakt yaratish
                    3. Kontakt tekshirish
                    4. Kontaktni o'chirish
                    5. Chiqish
                    Tanlamoqchi bo'lgan amalingizni kiriting (1,2,3 yoki 4):  """))
    
#Funksiyani yopish    
    return tanlov

#kontakt_kitobchasi yaratish
def kontakt_kitobchasi():
    #kontaktlarni o'zida salovchi bo'sh lug'at
    kontakt = {}
    
    #Dasturni doimiy ishlashi uchun while loop yaratish
    while True:
        #Kirish funksiyasini chaqirish. 
        #tanlov o'zgaruvchisini yaratish
        tanlov = Kirish()
        
        
        if tanlov == 1:
            
            if bool(kontakt) != False:
                for k, v in kontakt.items():
                    print(k, '-->', v)
             
            else:
                print("Kontaktlar ro'yxatingiz bo'sh! Menyuga qaytib, Kontakt yarating")
        
        elif tanlov == 2:
            
            nomer = input("Iltimos kiritmoqchi bo'lgan raqamingizni yozing: ")
            ism = input("Ushbu raqamni kim deya saqlamoqchisiz? Ism va familiya shaklida kiriting ")
            
            #kiritilgan kontaktning ro'yxatda mavjuda bo'lib bo'lmaganini aniqlash
            
            if nomer not in kontakt.items():
                kontakt.update({ism:nomer})
                #Xabar chiqarish
                print('Kontaktingiz muvaffaqiyatli saqlandi')
                print('Sizing kontaktlaringiz quyida mavjud: ')
                
                for k, v in kontakt.items():
                    print(k, '-->', v)
            
            else:
                print("Kiritmoqchi bo'lgan kontaktingiz allaqachon mavjud")
                
        
        elif tanlov == 3:
            
            nom = input("Ko'rmoqchi bo'lgan kontaktingizni ismini kiriting")
            
            if nom in kontakt:
                
                print('The contact is',nom,':',kontakt[nom])
                
                
            else:
                print("Bu kontakt mavjud emas, Asosiy menyuga qayting")
                
              
        elif tanlov == 4:
            
            nom = input("O'chirmoqchi bo'lgan kontaktingizni nomini kiriting: ")
            
            if nom in kontakt:
                
                print('The contact is',nom,':',kontakt[nom])
                
                
            else:
                print("Bu kontakt mavjud emas, Asosiy menyuga qayting")
            
            
            #foydalanuvchi rostdan ham o'chirmoqchi ekanligini tasdiqlash
            confirm = input("Rostdan ham siz bu kontaktni o'chirib yuborishni xoxlaysizmi? Xa yoki Yo'q")
            
            if confirm.capitalize() == 'Xa':
                
                kontakt.pop(nom,None)
                
                for k, v in kontakt.items():
                    print("Sizning yangilangan kontaktlar ro'yxatingiz quyida mavjud: ")
                    print(k, '-->', v)
            
            else:
                print("Asosiy menyuga qaytish")
            
        elif tanlov == 5:
            print("Python kontaktlar ro'yxatidan foydalanganingiz uchun tashakkur")
            break
            
            
        else:
            print("Noto'g'ri tanlov! ")
            
            
        

    

kontakt_kitobchasi()
