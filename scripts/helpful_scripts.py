from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_VAL = 2000000000

LOCAL_CHAINS = ["developmenet", "ganache-local"]


def get_account():
    # if network.show_active() == "development":
    if network.show_active() in LOCAL_CHAINS:
        account = accounts[0]
        return account
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    if len(MockV3Aggregator) <= 0:  ## onlye deploy once
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_VAL, "ether"), {"from": get_account()}
        )

        # priceFeed = mock__.address

    priceFeed = MockV3Aggregator[-1].address

    return priceFeed
