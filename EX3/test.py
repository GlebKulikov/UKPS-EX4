import main

test1 = main.Test()
def main():
    test1.start()
    print(test1.find_adress_postive("г. Москва, м. Тушинская, ул. Свободы, 23"))
    print(test1.find_adress_negative("Улица Билибекова дом Кандратьева "))
    print(test1.authrisation("0000000000"))
    print(test1.researsh_input("Кроссовки Nike"))
    print(test1.researsh_input("ggghhfFFFFfg"))
    print(test1.researsh_input_photo("test_img.png"))
    print(test1.researsh_input("кросовки-ботинки женские"))

if __name__ == '__main__':
    main()