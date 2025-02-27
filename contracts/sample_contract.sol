// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AIChain {
    address public owner;
    uint256 public totalSupply;

    constructor(uint256 initialSupply) {
        owner = msg.sender;
        totalSupply = initialSupply;
    }

    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(amount <= totalSupply, "Insufficient balance");
        totalSupply -= amount;
        return true;
    }
}
