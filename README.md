## Description
I want to let you know about a scammer wallet that drained ~100K$
Very many wallets in various EVM networks, mainly Ethereum and zkSync Era.
You can write a simple script or use an off-the-shelf one to analyze all the wallets that fell victim to the attack.
All wallets(not counting routers and contract addresses) == sybils that in my opinion used some script that compromised their private keys.

## Scammer's address
```
0x12476f5e2fde2f2b6179a8a884e4b53ab8fd6105
```
[parse_addresses.json](https://github.com/whonion/7330cfd305a3ad22b1013db812314c8d)

<details>
  <summary>Mainnet Incoming Addresses:</summary>
    "0x815c5b5682b65c824f6ff30271a41492a367f3f7",<br>
    "0xd82fc5e578ab7ea3038686f489da73725666bd7e",<br>
    "0x015e02b53c284a7e58a2706b602caa95ef9a986e",<br>
    "0xd3b5fc539d2168ba4bc3f174b5e1e68632823621",<br>
    "0x02dce608f759a97ecbcd6f5b148137e4ee7a20e2",<br>
    "0x33cea37f72357edda0c2f47d90ab5fb95e8e1622",<br>
    "0x7f3e367b54fcbdc54a51be7ec4d55b6c67bc5596",<br>
    "0x3524ff8d740a4f1be13f2cdd2f2345e54dc0c6b0",<br>
    "0x01327ca699949ca90b9dc330ea53ce299bf71795",<br>
    "0x7980dcd4f79f58c4568e0392dc9132fe874f682f",<br>
    "0xff9f7dda4c0ac2b852330c22de97301cd4531568",<br>
    "0xf16f998749d3a4c4792aad2497475363ab734afa",<br>
    "0x43a4878215b0fb9bf687b5a7338d5d24d33dffb1",<br>
    "0x7d78677ef3b9e71a5e5696171dc55301244f579c",<br>
    "0xf851cda02ba316bd9789bb8c135751a98b4a39e0"<br>
</details>


# Reasoning
All addresses have been emptied in the following EVM networks:
 - Ethereum
 - Arbitrum
 - Polygon
 - BNB Chain
 - Avalanche 
 - zkSync Era
# Methodology
In my analysis, I used a simple Python script to interact with the [etherscan.io](https://etherscan.io) API.
I parsed out all interactions between this address and other addresses, including Uniswap/1inch routers and token interactions. You can use fine-grained analysis to exclude router and token addresses from this list. Or use Arkham, which specializes in this.

## Also other addresses of scammers (includes first scammer's address):
```
0x12476f5e2fde2f2b6179a8a884e4b53ab8fd6105
0xf106d10b463f4226998d7c9839febef2b4325df0
0x594cc38bb577f900104bdf3ee53667ebe1fe5f9b
0xC107e8AD4b3AE3c1A228567a4B61dA7138681FD4
```
[sybil_result.json](https://github.com/whonion/py-sybil-drained-parser/blob/main/sybil_result.json)
## Rewards Address

```
whonion.eth
```