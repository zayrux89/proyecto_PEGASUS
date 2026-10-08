import sqlite3
import pandas as pd
from datetime import datetime
import os

DB_NAME = "pegasus_demo.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    # Tabla para Fatiga y Somnolencia
    c.execute('''
        CREATE TABLE IF NOT EXISTS fatiga_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conductor TEXT NOT NULL,
            fecha_hora TEXT NOT NULL,
            area_cargo TEXT,
            q1 TEXT, q2 TEXT, q3 TEXT, q4 TEXT, q5 TEXT,
            q6 TEXT, q7 TEXT, q8 TEXT, q9 TEXT, q10 TEXT, q11 TEXT,
            estado_alerta TEXT NOT NULL,
            supervisor TEXT
        )
    ''')
    
    # Tabla para Checklist de Minibus
    c.execute('''
        CREATE TABLE IF NOT EXISTS checklist_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patente TEXT NOT NULL,
            fecha_hora TEXT NOT NULL,
            km_inicio INTEGER,
            km_termino INTEGER,
            conductor TEXT NOT NULL,
            estado_general TEXT NOT NULL,
            detalle_fallas TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_fatiga(data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO fatiga_logs (
            conductor, fecha_hora, area_cargo,
            q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,
            estado_alerta, supervisor
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()

def insert_checklist(data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO checklist_logs (
            patente, fecha_hora, km_inicio, km_termino, conductor, estado_general, detalle_fallas
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()

def get_fatiga_data():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM fatiga_logs ORDER BY fecha_hora DESC", conn)
    conn.close()
    return df

def get_checklist_data():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM checklist_logs ORDER BY fecha_hora DESC", conn)
    conn.close()
    return df
