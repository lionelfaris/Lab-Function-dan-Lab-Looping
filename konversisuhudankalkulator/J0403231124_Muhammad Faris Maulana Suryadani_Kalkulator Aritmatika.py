""""
Muhammad Faris Maulana Suryadani 
J0403231124
TPL B1

"""

def kalkulator():
    """
    Melakukan operasi aritmatika pada sejumlah argumen.

    Returns:
        int atau float : Hasil dari operasi aritmetika.

    Raises:
        ValueError: Terjadi ketika operator tidak valid. Operator yang didukung: '+', '-', '*', '/'.
        ZeroDivisionError: Terjadi ketika ada pembagian dengan nol.
    """
    try:
        operator = input("Masukkan operator / tanda baca (+, -, *, /): ")
        if operator not in ('+', '-', '*', '/'):
            raise ValueError("Operator tidak valid. Operator yang didukung: '+', '-', '*', '/'")

        args = [float(arg) for arg in input("Masukkan argumen (angka yang ingin dihitung), pisahkan dengan spasi: ").split()]

        if operator == '/' and 0 in args:
            raise ZeroDivisionError("Tidak boleh melakukan pembagian dengan npl.")

        result = args[0]

        for num in args[1:]:
            if operator == '+':
                result += num
            elif operator == '-':
                result -= num
            elif operator == '*':
                result *= num
            elif operator == '/':
                result /= num

        return result
    except ValueError as ve:
        return f"Kesalahan Nilai: {ve}"
    except ZeroDivisionError as zde:
        return f"Kesalahan Pembagian Nol: {zde}"

# Contoh penggunaan
"""
Masukkan operator / tanda baca (+, -, *, /): +
Masukkan argumen (angka yang ingin dihitung), pisahkan dengan spasi: 10 12 3
25.0
"""
#Jalankan program
print(kalkulator())