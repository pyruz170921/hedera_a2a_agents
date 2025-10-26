// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "forge-std/Script.sol";
import "../src/StableCoin.sol";

contract DeployStableCoin is Script {
    function run() external {
        uint256 initialSupply = 1_000_000; // 1M tokens
        vm.startBroadcast();
        new StableCoin(initialSupply);
        vm.stopBroadcast();
    }
}
