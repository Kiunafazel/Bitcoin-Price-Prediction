
import pandas as pd
import yfinance as yf

old = pd.read_csv("bitcoin.csv")

old["Date"] = pd.to_datetime(old["Date"])
last_date = old["Date"].max()

new = yf.download(
    "BTC-USD",
    start=(last_date + pd.Timedelta(days=1)).strftime("%Y-%m-%d"),
    end="2026-11-01",
    interval="1d",
    auto_adjust=False,
    progress=False
)

if isinstance(new.columns, pd.MultiIndex):
    new.columns = new.columns.get_level_values(0)

new = new.reset_index()

new = new[["Date", "Open", "High", "Low", "Close", "Volume"]]

new = new.rename(columns={
    "Volume": "Vol."
})

new["Date"] = pd.to_datetime(new["Date"])

combined = pd.concat(
    [old, new],
    ignore_index=True
)

combined = combined.drop_duplicates(
    subset="Date",
    keep="last"
)

combined = combined.sort_values("Date")

combined.to_csv("bitcoin_updated.csv", index=False)

print("Dataset updated!")
print("Last date:", combined["Date"].max())
print("Total rows:", len(combined))
print(combined.tail())
