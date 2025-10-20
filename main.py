# ==============================================
# Program: TugasThread_AinurRopiq_312310502.py
# Nama : Ainur Ropiq
# NIM  : 312310502
# Deskripsi:
# Demonstrasi dua thread (Ainur dan Ropiq)
# yang menarik uang dari rekening bersama.
# Menunjukkan perbedaan hasil TANPA LOCK dan DENGAN LOCK.
# ==============================================

import threading
import time
import random

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.lock = threading.Lock()

    def withdraw_no_lock(self, amount, name):
        """Penarikan tanpa sinkronisasi."""
        print(f"[{name}] mencoba menarik {amount}...")
        current = self.balance
        time.sleep(random.random() * 0.01)
        if current >= amount:
            time.sleep(random.random() * 0.01)
            self.balance = current - amount
            print(f"[{name}] ✅ Berhasil menarik {amount} (Sisa saldo: {self.balance})")
        else:
            print(f"[{name}] ❌ Gagal menarik (Saldo: {self.balance})")

    def withdraw_with_lock(self, amount, name):
        """Penarikan dengan lock."""
        print(f"[{name}] mencoba menarik {amount}...")
        with self.lock:
            current = self.balance
            time.sleep(random.random() * 0.01)
            if current >= amount:
                time.sleep(random.random() * 0.01)
                self.balance = current - amount
                print(f"[{name}] ✅ Berhasil menarik {amount} (Sisa saldo: {self.balance})")
            else:
                print(f"[{name}] ❌ Gagal menarik (Saldo: {self.balance})")

def run_trial(use_lock=False):
    account = BankAccount(initial_balance=100)

    # pilih fungsi penarikan
    target = account.withdraw_with_lock if use_lock else account.withdraw_no_lock

    # dua peran orang
    t1 = threading.Thread(target=target, args=(80, 'Ainur'))
    t2 = threading.Thread(target=target, args=(80, 'Ropiq'))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"💰 Saldo akhir: {account.balance}")
    print("-" * 50)
    return account.balance

def multiple_runs(n, use_lock=False):
    results = []
    for i in range(1, n+1):
        mode = "DENGAN LOCK" if use_lock else "TANPA LOCK"
        print(f"\n🔹 Percobaan {i} ({mode})")
        saldo = run_trial(use_lock=use_lock)
        results.append(saldo)
    return results

# ==============================================
# MAIN PROGRAM
# ==============================================
if __name__ == "__main__":
    print("=== PROGRAM DEMONSTRASI THREADING BANK ===")
    print("Nama : Ainur Ropiq")
    print("NIM  : 312310502")
    print("===========================================\n")

    random.seed()

    print("=== TANPA LOCK (potensi race condition) ===")
    no_lock_results = multiple_runs(4, use_lock=False)

    print("\n=== DENGAN LOCK (aman & sinkron) ===")
    with_lock_results = multiple_runs(4, use_lock=True)

    print("\n=== RINGKASAN HASIL ===")
    print(f"Hasil Tanpa Lock : {no_lock_results}")
    print(f"Hasil Dengan Lock: {with_lock_results}")
    print("===========================================")
    print("Program selesai dijalankan oleh Ainur Ropiq (312310502)")
