from brownie import AdvancedCollectible, config, network
from scripts.helpful_script import get_account, OPENSEA_URL, get_contract, fund_with_link

token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": account}
    )
    fund_with_link(advanced_collectible.address)
    advanced_tx = advanced_collectible.createCollectible({"from": account})
    advanced_tx.wait(1)
    print("New Token is created.")
    return advanced_collectible, advanced_tx


def main():
    deploy_and_create()