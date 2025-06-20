import os
import sys

def flood_disk(path=".", depth=10, width=10):
    try:
        for i in range(width):
            new_dir = os.path.join(path, f"flood_{i}")
            os.makedirs(new_dir, exist_ok=True)
            print(f"[+] Criando: {new_dir}")
            if depth > 0:
                flood_disk(new_dir, depth - 1, width)
    except Exception as e:
        print(f"[!] Erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("[!] AVISO: Isso e uma ferramenta pra uso etico")
    confirm = input("Continuar? (s/n): ").strip().lower()
    if confirm == 's':
        flood_disk("/sdcard/disk_flood_test", depth=5, width=5)  
    else:
        print("Cancelado.")
