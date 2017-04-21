#! /usr/bin/env python



from googlefinance import getQuotes
import json

print(json.dumps(getQuotes('AAPL'), indent=2))

