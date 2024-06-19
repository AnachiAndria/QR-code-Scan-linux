# QR Code Scanner

Ce projet est un scanner de QR codes en Python utilisant l'appareil photo de l'ordinateur. Il utilise `opencv` pour accéder à la caméra et `pyzbar` pour lire les QR codes en temps réel.

## Description

Ce projet permet de scanner des QR codes en temps réel en utilisant la webcam de l'ordinateur. Lorsque des QR codes sont détectés, ils sont encadrés et leur contenu est affiché à l'écran ainsi que dans la console.

## Dépendances

- Python 3
- `opencv-python`
- `pyzbar`

## Installation

1. **Cloner le dépôt** :
    ```bash
    git clone https://github.com/votre-utilisateur/votre-repo.git
    cd votre-repo
    ```

2. **Installer les dépendances** :
    ```bash
    pip install opencv-python pyzbar
    ```

3. **Rendre le script exécutable** :
    ```bash
    chmod +x scan_qr_camera.py
    ```

4. **Déplacer le script vers un répertoire inclus dans le PATH** (optionnel) :
    ```bash
    sudo mv scan_qr_camera.py /usr/local/bin/scan_qr_camera
    ```

## Utilisation

1. **Exécuter le script** :
    ```bash
    python scan_qr_camera.py
    ```
    Ou, si vous avez déplacé le script dans un répertoire du PATH :
    ```bash
    scan_qr_camera
    ```

2. **Quitter l'application** :
    Appuyez sur la touche `q` pour quitter l'application.

## Code du script

Voici le code complet du script `scan_qr_camera.py` :

```python
#!/usr/bin/env python3

import cv2
from pyzbar.pyzbar import decode

def scan_qr_code_from_camera():
    # Initialiser la capture vidéo avec l'appareil photo par défaut (webcam)
    cap = cv2.VideoCapture(0)

    while True:
        # Lire une image depuis la caméra
        ret, frame = cap.read()

        if not ret:
            print("Échec de la capture vidéo.")
            break

        # Décoder les QR codes dans l'image
        detected_barcodes = decode(frame)

        for barcode in detected_barcodes:
            # La donnée est en bytes, donc nous la convertissons en string
            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type

            # Dessiner un rectangle autour du QR code détecté
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Afficher la donnée décodée au-dessus du QR code
            cv2.putText(frame, f"{barcode_data} ({barcode_type})", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            print(f"QR Code data: {barcode_data}")
        
        # Afficher l'image avec les QR codes détectés
        cv2.imshow('QR Code Scanner', frame)

        # Arrêter la capture vidéo si l'utilisateur appuie sur 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libérer la capture vidéo et fermer les fenêtres ouvertes
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr_code_from_camera()
