def set_simulation():
    print('Customer -> Merchant : Place Order')
    print('Merchant -> Payment Gateway : Send Payment Details')
    print('Payment Gateway -> Certificate Authority : Validate Certificate')
    print('Payment Gateway -> Merchant : Approve Payment')
    print('Merchant -> Customer : Confirm Order')


if __name__ == '__main__':
    set_simulation()
