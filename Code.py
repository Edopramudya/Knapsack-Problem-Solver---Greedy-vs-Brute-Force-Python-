# Data barang: (weight, profit, volume)
barang = [
    (10, 60, 10),  # Item 1
    (20, 100, 20), # Item 2
    (30, 120, 15), # Item 3
    (25, 90, 35),  # Item 4
    (40, 160, 50), # Item 5
    (35, 140, 45), # Item 6
]

max_weight = 100
max_volume = 100

# Fungsi untuk menghitung total weight, profit, dan volume dari sebuah solusi
def calculate_solution(solution):
    total_weight = 0
    total_profit = 0
    total_volume = 0
    for i, selected in enumerate(solution):
        if selected:
            total_weight += barang[i][0]
            total_profit += barang[i][1]
            total_volume += barang[i][2]
    return total_weight, total_profit, total_volume

# Fungsi untuk menghitung greedy berdasarkan kriteria
def greedy_by_criteria(criteria_fn):
    sorted_barang = sorted(barang, key=criteria_fn, reverse=True)
    total_weight = 0
    total_volume = 0
    solution = [0] * len(barang)
    for i, item in enumerate(sorted_barang):
        idx = barang.index(item)  # Dapatkan indeks asli item
        if total_weight + item[0] <= max_weight and total_volume + item[2] <= max_volume:
            solution[idx] = 1  # Pilih item
            total_weight += item[0]
            total_volume += item[2]
    return solution

# Brute Force untuk mencari solusi optimal
def brute_force():
    n = len(barang)
    best_solution = None
    max_profit = 0
    
    for i in range(1 << n):  # Iterasi semua kemungkinan solusi (2^n)
        solution = [(i >> j) & 1 for j in range(n)]  # Representasi biner
        total_weight, total_profit, total_volume = calculate_solution(solution)
        if total_weight <= max_weight and total_volume <= max_volume:
            if total_profit > max_profit:
                max_profit = total_profit
                best_solution = solution

    return best_solution

# Menampilkan hasil dalam satu tabel
def print_combined_table():
    headers = ["Item", "Weight", "Profit", "Volume", "Density", "Greedy by Weight", 
               "Greedy by Profit", "Greedy by Volume", "Greedy by Density", "Bruteforce"]
    
    # Hitung solusi greedy berdasarkan berbagai kriteria
    greedy_weight = greedy_by_criteria(lambda x: -x[0])  # Prioritaskan weight terkecil
    greedy_profit = greedy_by_criteria(lambda x: x[1])   # Prioritaskan profit terbesar
    greedy_volume = greedy_by_criteria(lambda x: -x[2])  # Prioritaskan volume terkecil
    greedy_density = greedy_by_criteria(lambda x: x[1] / (x[0] + x[2]))  # Profit/(Weight + Volume)
    
    # Hitung solusi brute force (solusi optimal)
    optimal_solution = brute_force()
    
    # Cetak header tabel
    print(f"{headers[0]:<6} {headers[1]:<8} {headers[2]:<8} {headers[3]:<8} {headers[4]:<10} "
          f"{headers[5]:<17} {headers[6]:<17} {headers[7]:<17} {headers[8]:<17} {headers[9]:<10}")
    
    # Cetak setiap baris untuk setiap item
    for i, (weight, profit, volume) in enumerate(barang):
        density = profit / (weight + volume)  # Hitung density
        print(f"{i+1:<6} {weight:<8} {profit:<8} {volume:<8} {density:<10.2f} "
              f"{greedy_weight[i]:<17} {greedy_profit[i]:<17} {greedy_volume[i]:<17} "
              f"{greedy_density[i]:<17} {optimal_solution[i]:<10}")
    
    # Hitung total beban, profit, volume untuk setiap metode
    greedy_weight_total = calculate_solution(greedy_weight)
    greedy_profit_total = calculate_solution(greedy_profit)
    greedy_volume_total = calculate_solution(greedy_volume)
    greedy_density_total = calculate_solution(greedy_density)
    optimal_total = calculate_solution(optimal_solution)
    
    print("\nTotal:")
    print(f"{'':<6} {'':<8} {'':<8} {'':<8} {'':<10} "
          f"{greedy_weight_total[0]:<17} {greedy_profit_total[0]:<17} {greedy_volume_total[0]:<17} "
          f"{greedy_density_total[0]:<17} {optimal_total[0]:<10} (Weight)")
    
    print(f"{'':<6} {'':<8} {'':<8} {'':<8} {'':<10} "
          f"{greedy_weight_total[1]:<17} {greedy_profit_total[1]:<17} {greedy_volume_total[1]:<17} "
          f"{greedy_density_total[1]:<17} {optimal_total[1]:<10} (Profit)")
    
    print(f"{'':<6} {'':<8} {'':<8} {'':<8} {'':<10} "
          f"{greedy_weight_total[2]:<17} {greedy_profit_total[2]:<17} {greedy_volume_total[2]:<17} "
          f"{greedy_density_total[2]:<17} {optimal_total[2]:<10} (Volume)")

# Menjalankan program dan mencetak tabel gabungan
print_combined_table()
