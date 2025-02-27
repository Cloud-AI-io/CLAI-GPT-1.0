import re

def validate_contract(contract_code):
    """
    Validates Solidity smart contract syntax using basic AI rules.
    """
    if "contract" not in contract_code or "function" not in contract_code:
        return False, "❌ Invalid contract format"
    if not re.search(r"pragma solidity \^0\.8\.0;", contract_code):
        return False, "❌ Solidity version is missing or incorrect"
    return True, "✅ Contract is valid"

if __name__ == "__main__":
    with open("../contracts/generated_contract.sol", "r") as file:
        contract_code = file.read()

    is_valid, message = validate_contract(contract_code)
    print(message)
