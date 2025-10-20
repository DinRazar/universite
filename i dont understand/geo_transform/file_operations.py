
import json

def write_results_to_file(results, filename):
    """
    Записывает результаты преобразований в файл
    
    Args:
        results: список результатов
        filename: имя файла
    """
    with open(filename, 'w', encoding='utf-8') as f:
        for result in results:
            f.write(str(result) + '\n')

def read_coordinates_from_file(filename, coord_type='cartesian'):
    """
    Читает координаты из файла
    
    Args:
        filename: имя файла
        coord_type: тип координат ('cartesian' или 'spherical')
    
    Returns:
        list: список координат
    """
    coordinates = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                coords = [float(x) for x in line.split()]
                coordinates.append(coords)
    
    return coordinates
