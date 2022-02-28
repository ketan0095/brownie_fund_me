from brownie import FundMe, network, config
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_CHAINS


def deploy_fund_me():
    account = get_account()

    print("account is ", account)
    # fund_me = FundMe.deploy({"from": account})

    # pass the pricefeed to fundme contract

    # if using persistant network use rinkeby
    # else use mocks

    if network.show_active() not in LOCAL_CHAINS:
        # priceFeed = "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e"
        priceFeed = config["network"][network.show_active()]["eth_usd_price_feed"]

    else:

        priceFeed = deploy_mocks()

    fund_me = FundMe.deploy(
        priceFeed,  ## will go to constuctor in fundmesol
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )

    return fund_me


def main():
    deploy_fund_me()
