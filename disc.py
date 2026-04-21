import json
import os

def check_sced_discrepancies():
    # Configuración de rutas
    base_path = r"C:\git\SCED"
    config_file = os.path.join(base_path, "config.json")
    objects_dir = os.path.join(base_path, "objects")

    # 1. Leer config.json
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {config_file}")
        return
    except json.JSONDecodeError:
        print(f"Error: El archivo {config_file} no es un JSON válido")
        return

    # Obtener la lista de objetos esperados
    expected_objects = config_data.get("ObjectStates_order", [])
    
    # 2. Escanear el directorio de objetos
    # Obtenemos nombres de archivos (sin .json) y nombres de carpetas
    if not os.path.exists(objects_dir):
        print(f"Error: La carpeta {objects_dir} no existe")
        return

    actual_entries = os.listdir(objects_dir)
    
    # Conjuntos para búsqueda rápida
    files_without_ext = {os.path.splitext(f)[0] for f in actual_entries if f.endswith('.json')}
    folders = {f for f in actual_entries if os.path.isdir(os.path.join(objects_dir, f))}

    print(f"--- Análisis de Discrepancias SCED ---")
    print(f"Objetos definidos en config.json: {len(expected_objects)}")
    print(f"Archivos .json encontrados en /objects: {len(files_without_ext)}")
    print("-" * 40)

    # 3. Buscar discrepancias
    missing_json = []
    found_count = 0

    for obj_name in expected_objects:
        if obj_name in files_without_ext:
            found_count += 1
            # Opcional: Avisar si existe el JSON pero no la carpeta (si consideras que es un error)
            # if obj_name not in folders:
            #    print(f"[Nota] {obj_name} tiene JSON pero no carpeta adjunta.")
        else:
            missing_json.append(obj_name)

    # 4. Reportar resultados
    if not missing_json:
        print("✅ ÉXITO: Todos los objetos de ObjectStates_order tienen su archivo .json correspondiente.")
    else:
        print(f"❌ ERROR: Faltan {len(missing_json)} archivos .json en la carpeta objects:")
        for missing in missing_json:
            print(f"   - {missing}.json")

    # 5. Buscar archivos huérfanos (están en la carpeta pero no en el config.json)
    orphans = files_without_ext - set(expected_objects)
    if orphans:
        print("\n⚠️ ADVERTENCIA: Archivos .json en la carpeta que NO están en ObjectStates_order:")
        for orphan in sorted(orphans):
            print(f"   - {orphan}.json")

if __name__ == "__main__":
    check_sced_discrepancies()