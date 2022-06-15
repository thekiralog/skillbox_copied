def flatter(dom_base, keys: list, values: list):
    if isinstance(dom_base, dict):
        for key, value in dom_base.items():
            keys.append(key)
            if isinstance(value, dict):
                flatter(value, keys, values)
            elif isinstance(value, list):
                for item in value:
                    flatter(item, keys, values)
            else:
                values.append(value)
    return


data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

key_list = list()
value_list = list()
flatter(data, key_list, value_list)
print(key_list)
print(value_list)
data['ETH']['total_diff'] = 100
data['tokens'][0]['fst_token_info']['name'] = 'doge'
data['tokens'][0].pop('total_out')
data['ETH']['total_out'] = data['tokens'][1].pop('total_out')
data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')
