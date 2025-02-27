from model import SmartContractAI

def save_contract(contract_code, filename="generated_contract.sol"):
    """Saves generated smart contract to a file"""
    with open(f"../contracts/{filename}", "w") as file:
        file.write(contract_code)

if __name__ == "__main__":
    ai = SmartContractAI()
    contract = ai.generate_contract(contract_name="AIChain", initial_supply=500000)
    save_contract(contract)
    print(f"✅ Smart contract generated and saved as contracts/{filename}")
