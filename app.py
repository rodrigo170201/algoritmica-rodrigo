from account import Account
from bank import Bank

if __name__ == '__main__':
    #Creo el banco
    banco_sol = Bank("Banco sol","123456","Banzer 6to anillo","bancosol@gmail.com","555-1234")
    #Creo cuentas
    my_account = Account(
        '12345','Rodrigo','Campos','78532293','rodrimontero17@gmail.com', Account.CURRENCIES[0], Account.ACCOUNT_TYPES[0])
    mi_cuenta = Account('54321','Juanito','Añez  ','78261598','juanito8912345@gmail.com',Account.CURRENCIES[1], Account.ACCOUNT_TYPES[0])
    #agrego las cuentas al banco
    banco_sol.add_account(my_account)
    banco_sol.add_account(mi_cuenta)
    #Movimientos
    my_account.add_funds(150)
    my_account.get_funds(80)
    my_account.get_funds(20)
    my_account.add_funds(50)
    mi_cuenta.add_funds(200)
    #Obteniendo todas las cuentas del banco
    print(banco_sol.get_accounts())
    #Obteniendo las cuentas
    print(f'Nro Cuenta      Nombre      Apellido        Telefono        Email                           Saldo')
    my_account.get_account()
    mi_cuenta.get_account()
    #Obteniendo los movimientos de la cuenta
    print('Los movimientos de la cuenta son:')
    print(my_account.get_records())
    print(mi_cuenta.get_records())
    
    
    
    
