pragma solidity ^0.6.0;

    contract Challenge {
      address public owner;
      mapping (address => uint) public funds;
      bytes32 private secret;
     
      modifier isOwner {
        require(msg.sender == owner);
        _;
      }
     
      constructor (bytes32 _secret) public payable {
        owner = msg.sender;
        secret = keccak256(abi.encodePacked(_secret));
        funds[owner] = funds[owner] += msg.value;
      }
     
      function setSecret(bytes32 _secret) public isOwner {
        secret = keccak256(abi.encodePacked(_secret));
      }
     
      function changeOwner(bytes32 _secret) public {
        if(keccak256(abi.encodePacked(_secret)) == secret) {
          owner = msg.sender;
        }
      }
     
      function depositFunds() public payable {
        funds[msg.sender] = funds[msg.sender] += msg.value;
      }
     
      function withdrawFunds(uint _amount) public {
        if(funds[msg.sender] >= _amount) {
          payable(msg.sender).call.value(_amount)("");
          funds[msg.sender] = funds[msg.sender] -= _amount;
        }
      }
     
      function stealFunds() public isOwner {
        payable(msg.sender).transfer(address(this).balance);
      }
     
      fallback () external payable { }
      receive () external payable { }
    }