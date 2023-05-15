n = 0
bacteria = 200 * 2 ** n
for bacteria in range(10):
    print(bacteria)
print('hour\t\t Number of bacteria')
print(f"{0}\t\t\t\t{200 * 2 ** 0}")
print(f"{5}\t\t\t\t{200 * 2 ** 5}")
print(f"{10}\t\t\t\t{200 * 2 ** 10}")
print(f"{15}\t\t\t\t{200 * 2 ** 15}")



hour_values = [0, 5, 10, 15]
bacteria_values = [200, 6400, 204800, 6553600]


print(f"{'Hour':>5}{'Number of Bacteria':>15}")
print("-" * 25)


for hour, bacteria in zip(hour_values, bacteria_values):
    print(f"{hour:>5}{bacteria:>15}")

