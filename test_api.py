#!/usr/bin/env python3

import requests
import json
import time
import subprocess
import sys
import os

def test_api():
    base_url = "http://localhost:5000"
    
    print("Testing Superheroes API...")
    
    # Test GET /heroes
    print("\n1. Testing GET /heroes")
    response = requests.get(f"{base_url}/heroes")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        heroes = response.json()
        print(f"Found {len(heroes)} heroes")
        print(f"First hero: {heroes[0] if heroes else 'None'}")
    
    # Test GET /heroes/:id
    print("\n2. Testing GET /heroes/1")
    response = requests.get(f"{base_url}/heroes/1")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        hero = response.json()
        print(f"Hero: {hero['name']} ({hero['super_name']})")
        print(f"Powers: {len(hero.get('hero_powers', []))}")
    
    # Test GET /heroes/:id (not found)
    print("\n3. Testing GET /heroes/999 (not found)")
    response = requests.get(f"{base_url}/heroes/999")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    
    # Test GET /powers
    print("\n4. Testing GET /powers")
    response = requests.get(f"{base_url}/powers")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        powers = response.json()
        print(f"Found {len(powers)} powers")
        print(f"First power: {powers[0] if powers else 'None'}")
    
    # Test GET /powers/:id
    print("\n5. Testing GET /powers/1")
    response = requests.get(f"{base_url}/powers/1")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        power = response.json()
        print(f"Power: {power}")
    
    # Test PATCH /powers/:id
    print("\n6. Testing PATCH /powers/1")
    update_data = {
        "description": "Updated description with more than 20 characters for validation"
    }
    response = requests.patch(f"{base_url}/powers/1", json=update_data)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        power = response.json()
        print(f"Updated power: {power}")
    
    # Test POST /hero_powers
    print("\n7. Testing POST /hero_powers")
    hero_power_data = {
        "strength": "Average",
        "power_id": 1,
        "hero_id": 3
    }
    response = requests.post(f"{base_url}/hero_powers", json=hero_power_data)
    print(f"Status: {response.status_code}")
    if response.status_code == 201:
        hero_power = response.json()
        print(f"Created hero power: {hero_power}")
    else:
        print(f"Error: {response.json()}")
    
    # Test POST /send-email
    print("\n8. Testing POST /send-email")
    response = requests.post(f"{base_url}/send-email")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    
    print("\nAPI testing completed!")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the Flask app is running on localhost:5000")
        print("Run: python app.py")