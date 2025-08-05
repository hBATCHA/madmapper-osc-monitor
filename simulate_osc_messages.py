#!/usr/bin/env python3
"""
Script de simulation d'envoi de messages OSC vers le moniteur
Simule les messages qu'un Manager pourrait envoyer vers MadMapper
"""

import time
import random
from pythonosc import udp_client

# Configuration
IP = "127.0.0.1"
PORT = 7000

def simulate_madmapper_messages():
    """Simule les messages OSC spécifiques du Manager vers MadMapper selon le tableau Stellantis"""
    
    # Créer le client OSC
    client = udp_client.SimpleUDPClient(IP, PORT)
    
    print(f"🎭 Simulation de messages OSC Stellantis vers {IP}:{PORT}")
    print("📡 Envoi de messages simulés du Manager vers MadMapper...")
    print("Appuie sur Ctrl+C pour arrêter.\n")
    
    message_count = 0
    
    try:
        while True:
            message_count += 1
            
            # Messages selon le tableau Stellantis
            message_type = random.choice([
                'lighting_cue',
                'system_control', 
                'activation_messages',
                'audio_analysis'
            ])
            
            if message_type == 'lighting_cue':
                # Numéro de la scène lighting /cueX.Y.Z
                x = random.randint(1, 10)
                y = random.randint(1, 5)
                z = random.randint(1, 3)
                address = f"/cue{x}.{y}.{z}"
                client.send_message(address, 1)  # Déclenchement int: {1}
                    
            elif message_type == 'system_control':
                # Eteindre tous les modules
                address = "/off_madmapper"
                client.send_message(address, 1)  # Déclenchement int: {1}
                
            elif message_type == 'activation_messages':
                # Messages d'activation des différents éléments
                activation_addresses = [
                    "/FrontDoors",      # Activation des panneaux de porte avant
                    "/RearDoors",       # Activation des panneaux de porte arrière  
                    "/WindowPillars",   # Activation des montants de baie
                    "/FrontFootwells",  # Activation des caves à pieds avant
                    "/RearFootwells",   # Activation des caves à pieds arrière
                    "/Strip",           # Activation du strip pdb
                    "/CeilingProjector" # Activation du projecteur plafond
                ]
                address = random.choice(activation_addresses)
                value = random.choice([0, 1])  # Activation int: {0,1}
                client.send_message(address, value)
                
            elif message_type == 'audio_analysis':
                # Messages d'analyse audio (trame port 1007)
                audio_params = [
                    ("/Opacity", "Valeur d'opacité"),      # Contrôle dynamique intensité
                    ("/Bass", "Bass"),                      # Valeur des graves
                    ("/Medium", "Medium"),                  # Valeur des medium  
                    ("/Treble", "Treble"),                 # Valeur des aigus
                    ("/Amplitude", "Amplitude")             # Valeur de l'amplitude
                ]
                address, description = random.choice(audio_params)
                value = random.uniform(0.0, 1.0)  # float: {0,1}
                client.send_message(address, value)
            
            print(f"✅ Message #{message_count} envoyé")
            
            # Attendre entre 1 et 3 secondes avant le prochain message
            time.sleep(random.uniform(1.0, 3.0))
            
    except KeyboardInterrupt:
        print(f"\n🛑 Simulation arrêtée. {message_count} messages envoyés au total.")

def send_specific_test_messages():
    """Envoie tous les types de messages du tableau Stellantis"""
    client = udp_client.SimpleUDPClient(IP, PORT)
    
    print("🧪 Envoi de messages de test Stellantis...\n")
    
    test_messages = [
        # Messages de scène lighting
        ("/cue1.1.1", 1, "Numéro de scène lighting - déclenchement"),
        ("/cue2.3.1", 1, "Numéro de scène lighting - déclenchement"),
        
        # Contrôle système
        ("/off_madmapper", 1, "Eteindre tous les modules"),
        
        # Messages d'activation (int: 0 ou 1)
        ("/FrontDoors", 1, "Activation panneaux porte avant"),
        ("/RearDoors", 0, "Activation panneaux porte arrière"),
        ("/WindowPillars", 1, "Activation montants de baie"),
        ("/FrontFootwells", 1, "Activation caves à pieds avant"),
        ("/RearFootwells", 0, "Activation caves à pieds arrière"),
        ("/Strip", 1, "Activation strip pdb"),
        ("/CeilingProjector", 1, "Activation projecteur plafond"),
        
        # Messages d'analyse audio (float: 0.0 à 1.0)
        ("/Opacity", 0.75, "Contrôle dynamique intensité lumineuse"),
        ("/Bass", 0.45, "Valeur des graves"),
        ("/Medium", 0.68, "Valeur des medium"),
        ("/Treble", 0.82, "Valeur des aigus"),
        ("/Amplitude", 0.91, "Valeur de l'amplitude")
    ]
    
    for i, (address, value, description) in enumerate(test_messages, 1):
        client.send_message(address, value)
        print(f"📤 Test {i:2d}: {address:20} -> {value:5} ({description})")
        time.sleep(0.5)
    
    print(f"\n✅ {len(test_messages)} messages de test Stellantis envoyés!")

if __name__ == "__main__":
    print("🎯 Simulateur de messages OSC Stellantis MadMapper")
    print("=" * 55)
    
    mode = input("Choisir le mode:\n1. Simulation continue (c)\n2. Messages de test Stellantis (t)\nChoix [c/t]: ").lower()
    
    if mode in ['t', 'test']:
        send_specific_test_messages()
    else:
        simulate_madmapper_messages()
