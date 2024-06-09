import xml.etree.ElementTree as ET
from typing import List, Dict, Any

def generate_pokemon_xml(pokemons: List[Dict[str, Any]], file_path: str):
    root = ET.Element("pokemons")

    for pokemon in pokemons:
        pokemon_elem = ET.SubElement(root, "pokemon")
        
        for key, value in pokemon.items():
            if isinstance(value, dict) or isinstance(value, list):
                value = str(value)  
            
            ET.SubElement(pokemon_elem, key).text = str(value)

    tree = ET.ElementTree(root)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
