
import sys
from .transformations import cartesian_to_spherical, spherical_to_cartesian
from .file_operations import write_results_to_file, read_coordinates_from_file

def main():
    print("=== Пакет преобразования координат ===\n")
    
    while True:
        print("Выберите действие:")
        print("1. Преобразовать декартовы координаты в сферические")
        print("2. Преобразовать сферические координаты в декартовы")
        print("3. Обработать файл с координатами")
        print("4. Выход")
        
        choice = input("\nВаш выбор (1-4): ").strip()
        
        if choice == '1':
            # Декартовы в сферические
            try:
                x = float(input("Введите x: "))
                y = float(input("Введите y: "))
                z = float(input("Введите z: "))
                
                r, theta, phi = cartesian_to_spherical(x, y, z)
                print(f"Результат: r={r:.2f}, theta={theta:.2f}°, phi={phi:.2f}°")
                
                save = input("Сохранить в файл? (y/n): ").lower()
                if save == 'y':
                    write_results_to_file([f"Декартовы: ({x}, {y}, {z}) -> Сферические: (r={r:.2f}, θ={theta:.2f}°, φ={phi:.2f}°)"], 
                                         "results.txt")
                    print("Результат сохранен в results.txt")
                    
            except ValueError:
                print("Ошибка: введите числа!")
                
        elif choice == '2':
            # Сферические в декартовы
            try:
                r = float(input("Введите r: "))
                theta = float(input("Введите theta (градусы): "))
                phi = float(input("Введите phi (градусы): "))
                
                x, y, z = spherical_to_cartesian(r, theta, phi)
                print(f"Результат: x={x:.2f}, y={y:.2f}, z={z:.2f}")
                
                save = input("Сохранить в файл? (y/n): ").lower()
                if save == 'y':
                    write_results_to_file([f"Сферические: (r={r}, θ={theta}°, φ={phi}°) -> Декартовы: ({x:.2f}, {y:.2f}, {z:.2f})"], 
                                         "results.txt")
                    print("Результат сохранен в results.txt")
                    
            except ValueError:
                print("Ошибка: введите числа!")
                
        elif choice == '3':
            filename = input("Введите имя файла: ")
            try:
                coords = read_coordinates_from_file(filename)
                results = []
                
                for coord in coords:
                    if len(coord) == 3:
                        x, y, z = coord
                        r, theta, phi = cartesian_to_spherical(x, y, z)
                        result = f"({x}, {y}, {z}) -> (r={r:.2f}, θ={theta:.2f}°, φ={phi:.2f}°)"
                        results.append(result)
                        print(result)
                
                if results:
                    write_results_to_file(results, "batch_results.txt")
                    print(f"\nВсе результаты сохранены в batch_results.txt")
                    
            except FileNotFoundError:
                print("Файл не найден!")
            except Exception as e:
                print(f"Ошибка при обработке файла: {e}")
                
        elif choice == '4':
            print("Выход из программы.")
            break
            
        else:
            print("Неверный выбор! Попробуйте снова.")
        
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()
