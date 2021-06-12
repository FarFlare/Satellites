import requests
from pprint import pprint

contract = "0x6ede7f3c26975aad32a475e1021d8f6f39c89d82"
token_id = "29717585154687144884817730631809658487984116655369711026868430457829559631873"
itemId = f"{contract}:{token_id}"


def get_by_id():
    resp = requests.get(f"https://api-staging.rarible.com/protocol/v0.1/ethereum/nft/items/{itemId}")
    return resp.json()


def get_meta_by_id():
    resp = requests.get(f"https://api-staging.rarible.com/protocol/v0.1/ethereum/nft/items/{itemId}")
    return resp.json()


def get_all():
    resp = requests.get(f"https://api-staging.rarible.com/protocol/v0.1/ethereum/nft/items/all")
    return resp.json()


def get_sell_orders(by_item=False):
    if by_item:
        resp = requests.get(f"https://api-staging.rarible.com/protocol/v0.1/ethereum/order/orders/sell/byItem",
                            params={"contract": contract,
                                    "tokenId": token_id})
    else:
        resp = requests.get(f"https://api-staging.rarible.com/protocol/v0.1/ethereum/order/orders/sell",
                            params={
                                "sort": "LAST_UPDATE"
                            })
    return resp.json()


def search_orders():
    # resp = requests.post(f"https://api-staging.rarible.com/protocol/v0.1/ethereum/order/indexer/orders/search",
    resp = requests.post(f"http://api-staging.rarible.com/protocol/ethereum/order/indexer/v1/orders/search",
                         data={"@type": "sell"})
    return resp.json()


# def make_order():
#     resp = requests.post(f"https://api-staging.rarible.com/protocol/v0.1/ethereum/order/orders",
#                          data={
#                              "type": "RARIBLE_V2",
#                              "maker": ""
#                          })


if __name__ == '__main__':
    pprint(get_sell_orders(True))
