import pandas as pd

df = pd.read_csv('hotels.csv')
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict('records')
df_cards_authorize = pd.read_csv('card_security.csv', dtype=str)


class Hotel:
    def __init__(self, code):
        self.code = code
        self.name = df.loc[df['id'] == int(self.code), 'name'].iloc[0]

    def available(self):
        return df.loc[df['id'] == int(self.code), 'available'].iloc[0] == 'yes'

    def book(self):
        df.loc[df['id'] == int(self.code), 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)


class ReservationTicket:

    def __init__(self, customer_name, hotel):
        self.customer_name = customer_name
        self.hotel = hotel

    def generate(self):
        return f"""
        Here is your data reservation:
        Hotel name: {self.hotel.name}
        Customer: {self.customer_name}
        """


class ReservationTicketSPA(ReservationTicket):

    def generate(self):
        return f"""
        Here is your data SPA reservation:
        Hotel name: {self.hotel.name}
        Customer: {self.customer_name}
        """


class CreditCard:

    def __init__(self, card_number):
        self.card_number = card_number

    def validate(self, expiration, cvc, holder):
        card_info = {'number': self.card_number, 'expiration': expiration, 'cvc': cvc, 'holder': holder}
        if card_info in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):

    def authorize(self, given_password):
        password = df_cards_authorize.loc[df_cards_authorize['number'] == self.card_number, 'password'].iloc[0]
        if given_password == password:
            return True
        else:
            return False


if __name__ == '__main__':
    print(df)
    hotel_code = input("Enter hotel's code:")
    hotel = Hotel(hotel_code)
    if hotel.available():
        credit_card = SecureCreditCard(card_number='1234567890123456')
        if credit_card.validate(expiration='12/26', cvc='123', holder='JOHN SMITH') \
                and credit_card.authorize(given_password='mypass'):
            hotel.book()
            customer_name = input("Enter your name:")
            spa = True if input("Do you want SPA?") == 'yes' else False

            if spa:
                reservation_ticket = ReservationTicketSPA(customer_name, hotel)
            else:
                reservation_ticket = ReservationTicket(customer_name, hotel)

            print(reservation_ticket.generate())
        else:
            print('There are some problems with payment')
    else:
        print('Not available')
