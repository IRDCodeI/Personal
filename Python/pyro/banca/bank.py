import random as rd
import Pyro4

@Pyro4.expose
class Bank:

    clients = set()

    def withdraw(self, account, mount):
        for e in self.clients:
            if e.account == account:
                e.credit = e.credit - mount

        print(f"Account: {account} remove {mount}$")

    def deposit(self, account, mount):
        for e in self.clients:
            if e.account == account:
                e.credit = e.credit + mount
        
        print(f"Account: {account} add {mount}$")

    def transfer(self, account, account_b, mount):
        for e in self.clients:
            if e.account == account:
                e.credit = e.credit - mount
            if e.account == account_b:
                e.credit = e.credit + mount

        print(f"Account: {account} transfer to {account_b} mount of {mount}")

    def add_clients(self, *args):
        for arg in args:
            self.clients.add(arg)

    def list_clients(self):
        for e in self.clients:
            print(f"Account: {e.account} - Credit: {e.credit}")

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()

uri = daemon.register(Bank)
ns.register("pyro.bank", uri)
print("Wait for requests")

daemon.requestLoop()