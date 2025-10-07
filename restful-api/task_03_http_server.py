#!/usr/bin/python3
"""
Simple HTTP API using http.server
"""

import json
import http.server

# appele du serveur
class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Ici tu vérifieras self.path pour choisir la réponse
        # Exemple : si self.path == "/", tu enverras "Hello, this is a simple API!"
        pass


#  BaseHTTPRequestHandler   



# Méthode do_GET appelée



#self.path contient l’URL demandée (ex: "/data")   

