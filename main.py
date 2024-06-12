import argparse

def main():
    parser = argparse.ArgumentParser(description="Currency Converter")
    parser.add_argument("from_currency", type=str, help="Currency to convert from")
    parser.add_argument("to_currency", type=str, help="Currency to convert to")
    parser.add_argument("amount", type=float, help="Amount to convert")
    
    args = parser.parse_args()
    
    try:
        result = convert(args.from_currency, args.to_currency, args.amount)
        result = round(result, precision[args.to_currency])
        print(f"{args.amount} {args.from_currency} = {result} {args.to_currency}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
