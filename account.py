from datetime import date
from client import Client

class Account:
    CURRENCIES = ['BOB', 'USD', 'EUR']
    ACCOUNT_TYPES = ['Saving Box', 'Current Account']

    persona = Client()
    nombre = persona.get_name
    apellido = persona.get_lastName
    telefono = persona.get_phone
    email = persona.get_email
    direccion = persona.get_address

    def __init__(self, number, nombre, apellido, telefono, email, currency, account_type):
        self.number = number
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.currency = currency
        self.account_type = account_type
        self.current_record = 0
        self.records = {}
        self.balance = 0

    def add_funds(self, amount):
        self.balance += amount
        self.current_record += 1
        self.records[self.current_record] = {
            'movement_type': 'Credit',
            'date': date.today(),
            'amount': amount
        }

    def get_funds(self, amount):
        self.balance -= amount
        self.current_record += 1
        self.records[self.current_record] = {
            'movement_type': 'Debit',
            'date': date.today(),
            'amount': amount
        }

    def get_balance(self):
        return self.balance

    def get_records(self):
        formatted = ''
        for element in self.records.items():
            record = element[1]
            formatted += f' Nro cuenta: {self.number} Fecha: {record["date"].day}/{record["date"].month}/{record["date"].year} - Tipo: {record["movement_type"]} - Monto: {record["amount"]}\n'
        return formatted

    def get_currency(self):
        return self.currency
    
    def get_account(self):
        print(f"{self.number}   {self.nombre}   {self.apellido}     {self.telefono}     {self.email}       {self.balance}")

    def get_number(self):
        return self.number
    
    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_telefono(self):
        return self.telefono
    
    def get_email (self):
        return self.email
    
    def get_currency(self):
        return self.currency
    
    def get_account_type (self):
        return self.account_type
    

