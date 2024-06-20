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

            print(f"Code : {barcode_data}")
            break
        
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