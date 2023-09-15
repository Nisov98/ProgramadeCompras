from ownable import Ownable

class Cart(Ownable):
    # ... (otros métodos y atributos)

    def check_out(self):
        if self.owner.wallet.balance >= self.total_amount():
            # Realizar la transferencia de dinero y propiedad por cada artículo en el carrito
            for item in self.items:
                # Transferir el precio de compra al monedero del propietario del artículo
                item.owner.wallet.deposit(item.price)
                # Transferir la propiedad del artículo al propietario del carrito
                item.owner = self.owner

            # Vaciar el contenido del carrito
            self.items = []
            print("🛒 Carrito vaciado")
        else:
            print("⚠️ Saldo insuficiente en el monedero")

        # Actualizar el saldo del monedero del propietario del carrito después de la compra
        self.owner.wallet.withdraw(self.total_amount())

