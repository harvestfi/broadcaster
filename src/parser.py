# - $950K in gas saved
# - 1340 FARM buybacks
# - 2158 FARM buybacks (ps + autoharvest)
# - $1,7M Income generated


def get_hardworks_summary(hardworks) -> int:
    gas_saved = 0
    farm_buybacks = 0
    total_income = 0

    for hardwork in hardworks:
        gas_saved += hardwork["savedGasFees"]
        farm_buybacks += hardwork["farmBuyback"]
        total_income += hardwork["fullRewardUsd"]

    return {
        "gas_saved": gas_saved,
        "farm_buybacks": farm_buybacks,
        "total_income": total_income,
    }

def get_ps_summary(ps_history) -> int:
    current_state = 0
    emissions = ps_history[len(ps_history)-1]["sharePrice"] - ps_history[0]["sharePrice"]
    
    return {
        "emissions": emissions
    }