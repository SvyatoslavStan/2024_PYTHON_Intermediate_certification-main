import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int, help="Число")
    parser.add_argument("text", type=str, help="Строка")
    parser.add_argument("--verbose", action="store_true", help="Дополнительная информация")
    parser.add_argument("--repeat", type=int, default=1, help="Количество повторений строки")

    args = parser.parse_args()

    if args.verbose:
        print(f"Начинаем вывод строки {args.repeat} раз")
    
    for i in range(args.repeat):
        print(args.text)

    if args.verbose:
        print(f"Число: {args.number}, Строка: {args.text}, Повторений: {args.repeat}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Ошибка: необходимо передать как минимум два аргумента: number и text.")
        sys.exit(1)
    main()
