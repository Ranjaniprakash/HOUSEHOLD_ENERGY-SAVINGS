# main.py
import sys, glob, os
from src.data_loader import load_keel_dataset
from src.model import train_energy_model
from src.recommendations import recommend_tips

def find_dat_file():
    # 1) If user passed a filename on the command line, use that
    if len(sys.argv) > 1:
        return sys.argv[1]
    # 2) Otherwise, look for any .dat in the CWD:
    candidates = glob.glob(os.path.join(os.getcwd(), '*.dat'))
    if not candidates:
        raise FileNotFoundError(
            "No .dat file found in the current directory.\n"
            "Either pass it as:  python main.py path/to/file.dat"
        )
    # just pick the first one
    return candidates[0]

def main():
    data_path = find_dat_file()
    print(f"Loading KEEL dataset from: {data_path}")
    df = load_keel_dataset(data_path)
    print(f"  → Loaded {df.shape[0]} rows, {df.shape[1]} columns")

    model, mse = train_energy_model(df)
    print(f"Trained LinearRegression model. Test MSE = {mse:.3f}")

    # predict on “average” day
    sample = df.iloc[:, :-1].mean().values.reshape(1, -1)
    pred = model.predict(sample)[0]
    print(f"Predicted daily consumption: {pred:.2f} kWh\n")

    print("Energy Saving Tips:")
    for tip in recommend_tips(pred):
        print(" •", tip)

if __name__ == "__main__":
    main()
