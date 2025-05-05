# Knapsack-Problem-Solver---Greedy-vs-Brute-Force-Python-
proyek ini merupakan implementasi penyelesaian Knapsack Problem dengan dua pendekatan berbeda, yaitu Greedy Heuristics dan Brute Force Search. Program ini mengevaluasi kombinasi barang berdasarkan berat, keuntungan (profit), dan volume, lalu membandingkan performa masing-masing metode dalam bentuk tabel yang rapi.

## Fitur
* Representasi data barang dalam bentuk `(weight, profit, volume)`.
* Implementasi metode **Greedy** berdasarkan:
  * Berat terkecil
  * Profit terbesar
  * Volume terkecil
  * Rasio keuntungan terhadap (berat + volume)
* Implementasi metode **Brute Force** untuk mencari solusi optimal.
* Perbandingan hasil setiap metode dalam bentuk tabel konsol:
  * Barang terpilih
  * Total berat, profit, dan volume
  * Efisiensi berdasarkan kriteria yang dipilih

## Struktur Kode
* `calculate_solution`: Menghitung total berat, profit, dan volume dari solusi.
* `greedy_by_criteria`: Fungsi greedy generik berdasarkan kriteria tertentu.
* `brute_force`: Menelusuri semua kemungkinan kombinasi untuk menemukan solusi optimal.
* `print_combined_table`: Menampilkan tabel ringkasan perbandingan hasil dari semua metode.
* 
## Contoh Output
Program akan menampilkan tabel yang berisi data setiap barang, nilai densitas, serta apakah barang tersebut dipilih oleh masing-masing metode.

## Tujuan
Proyek ini bertujuan untuk:
* Mempelajari dan membandingkan efektivitas metode greedy dan brute force dalam menyelesaikan Knapsack Problem.
* Menyediakan dasar kode yang dapat dikembangkan lebih lanjut, misalnya dengan algoritma Genetika atau Dynamic Programming.
