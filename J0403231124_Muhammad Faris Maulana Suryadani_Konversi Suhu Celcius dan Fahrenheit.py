def hitung_suhu (jenis_suhu, angka_suhu) :
    """
    Program mengubah nilai suhu dari skala Celcius (C) ke skala Fahrenheit (F) dan sebaliknya.
    
    Argumen :
    jenis_suhu (str) : jenis dari suhu yang diinput oleh user ("C" untuk Celcius dan "F" untuk Fahrenheit)
    angka_suhu (float) : inputan user berupa angka suhu yang ingin diubah skalanya
    
    Return :
    float : nilai dari suhu yang telah diubah berupa tipe data float
    
    Raises :
    Jika inputan user dalam "jenis suhu" berupa selain "C" dan "F", akan menghasilkan ValueError
    
    Contoh : 
    Masukkan jenis suhu yang ingin diubah : C
    Masukkan angka suhu : 0
    Suhu yang sudah diubah adalah : 32.0
    
    Masukkan jenis suhu yang ingin diubah : F
    Masukkan angka suhu : 0
    Suhu yang sudah diubah adalah : -17.77777777777778
    """
    
    if jenis_suhu == "F" or jenis_suhu == "f" :
        suhu_sudah_diubah = (angka_suhu - 32) * 5/9
    elif jenis_suhu == "C" or jenis_suhu == "c" :
        suhu_sudah_diubah = (angka_suhu * 9/5 ) + 32
    else : 
        raise ValueError("Hanya dapat mengenali suhu dalam Celcius (C) dan Fahrenheit (F) !")
    return suhu_sudah_diubah

hitung = hitung_suhu(str (input ("Masukkan jenis suhu yang ingin diubah ( Celcius (C) / Fahrenheit (F) ) : ")), float (input ("Masukkan angka suhu : ")))
print ("Suhu yang sudah diubah adalah :",hitung)

