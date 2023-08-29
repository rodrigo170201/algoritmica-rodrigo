from account import Account

class Bank:
    
    def __init__ (self, name_bank, nit, address, email, telephone):
        self.name_bank = name_bank
        self.nit = nit
        self.address = address
        self.email = email
        self.telephone = telephone
        self.accounts = []

    def add_account (self, account):
        if isinstance(account, Account):
            self.accounts.append(account)
        else:
            raise ValueError("No se agregó la cuenta a la lista")
        

    def get_accounts (self):
        if not self.accounts:
            print("No hay cuentas en el banco")
        else:
            print(f"{self.get_name_bank()}")
            print(f"Nit: {self.get_nit()}")
            print(f"Dirección: {self.get_address()}")
            print(f"Teléfono: {self.get_telephone()}",end="\n")
            print(f"Cuentas agregadas son:")
            print(f"Nro Cuenta:        Nombre:             Apellido:          Telefono:            email:                         Moneda:               Tipo de cuenta:")
            for account in self.accounts:
                print(f"{account.get_number()}              {account.get_nombre()}             {account.get_apellido()}             {account.get_telefono()}             {account.get_email()}           {account.get_currency()}               {account.get_account_type()}")
        
    
    def get_name_bank(self):
        return self.name_bank

    def get_nit(self):
        return self.nit

    def get_address (self):
        return self.address
    
    def get_email(self):
        return self.email
    
    def get_telephone(self):
        return self.telephone
    

