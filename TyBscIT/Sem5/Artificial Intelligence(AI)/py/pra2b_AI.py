def Tower(n, from_rod, to, aux):
    if n == 1:
        print(f"Move disk 1 from rod {from_rod} to rod {to}")
        return
    Tower(n-1, from_rod, aux, to)
    print(f"Move disk {n} from rod {from_rod} to rod {to}")
    Tower(n-1, aux, to, from_rod)

n = 3
Tower(n, 'A', 'C', 'B')
