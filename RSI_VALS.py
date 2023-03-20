from trading_data_MAIN2 import pair_prices
import random
Currency_prices=pair_prices()
print(Currency_prices)
currencies=[['EURUSDX'],['JPYX'],['GBPUSDX'],['AUDUSDX'],['NZDUSDX'],['EURJPYX'],['GBPJPYX'],['EURGBPX'],['EURCADX'],['EURSEKX'],['EURCHFX'],['EURHUFX'],['EURJPYX'],['CNYX'],['HKDX'],['SGDX'],['INRX'],['MXNX'],['PHPX'],['IDRX'],['THBX'],['MYRX'],['ZARX'],['RUBX']]

#cleaning data off special characters

currency_prices=[]
for pair in Currency_prices:
    #print(pair)
    if len(pair)>20:
        val=[]
        for i in pair:
            if '"' in i:
                k=i.replace('"',"")
                if ">" in k:
                    j=k.replace('>',".")
                    val.append(float(j))
            elif ">" in i:
                m=i.replace('>',".")
                val.append(float(m))
            else:
                val.append(float(i))
        currency_prices.append(val)
    else:
        pass
length=len(currency_prices)

currency_with_vals=[]

for values in currency_prices:
    print(values)
    for currency in currencies:
        currency_with_vals.append[currency,values]

print(currency_with_vals)
#print(length)
#print(currency_prices[23])
#name=currencies[0]+'.csv'
#print(name)

def RSI(currency_price):
    global currency_prices
    window_length = 14
# Initialize containers for avg. gains and losses
    gains = []
    losses = []
# Create a container for current lookback prices
    window = []
# Keeps track of previous average values
    prev_avg_gain = None
    prev_avg_loss = None
    # Create a container for our final output (as a csv)
    output = [['date', 'close', 'gain', 'loss', 'avg_gain', 'avg_loss', 'rsi']]
    for i, price in enumerate(currency_price):
    # keep track of the price for the first period
    # but don't calculate a difference value.
        if i == 0:
            window.append(price)
            output.append([i+1, price, 0, 0, 0, 0, 0])
            continue
    # After the first period, calculate the difference
    # between price and previous price as a rounded value
        difference = round(currency_price[i] - currency_price[i - 1], 2)
        # Record positive differences as gains
        if difference > 0:
            gain = difference
            loss = 0
# Record negative differences as losses
        elif difference < 0:
            gain = 0
            loss = abs(difference)
# Record no movements as neutral
        else:
            gain = 0
            loss = 0
# Save gains/losses
        gains.append(gain)
        losses.append(loss)
# Continue to iterate until enough
# gains/losses data is available to
# calculate the initial RS value
        if i < window_length:
            window.append(price)
            output.append([i+1, price, gain, loss, 0, 0, 0])
            continue
        # Calculate SMA for first gain
        if i == window_length:
            avg_gain = sum(gains) / len(gains)
            avg_loss = sum(losses) / len(losses)
# Use WSM after initial window-length period
        else:
            avg_gain = (prev_avg_gain * (window_length - 1) + gain) / window_length
            avg_loss = (prev_avg_loss * (window_length - 1) + loss) / window_length
# Keep in memory
        prev_avg_gain = avg_gain
        prev_avg_loss = avg_loss
# Round for later comparison (optional)
        avg_gain = round(avg_gain, 2)
        avg_loss = round(avg_loss, 2)
        prev_avg_gain = round(prev_avg_gain, 2)
        prev_avg_loss = round(prev_avg_loss, 2)
        # use avg. gains and losses to calculate
# the RS value rounded to the nearest
# 2 decimal places
        rs = round(avg_gain / avg_loss, 2)
        # use the RS value to calculate the
# RSI to the nearest 2 decimal places
        rsi = round(100 - (100 / (1 + rs)), 2)
        # Remove oldest values
        window.append(price)
        window.pop(0)
        gains.pop(0)
        losses.pop(0)
# Save Data
        output.append([i+1, price, gain, loss, avg_gain, avg_loss, rsi])
    return output

def save_data_csv():
    global currencies
    global currency_prices
    currency_price=currency_prices
    import csv
    i=0
# Create a new CSV file to store output data
    for currency in currencies:
        if i<=len(currency_with_vals):
            price_value=currency_with_vals[i][1]
            name=currency[0]+'RSI.csv'
            currency_RSI=RSI(price_value)
            with open(name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(currency_RSI)
            i=i+1
        else:
            break
save_data_csv()
