import economy


def main():
    print('Welcome to WikiLeverage')
    a = economy.EconomicActor(400, 800)
    print(a.equity)


if __name__ == '__main__':
    main()
