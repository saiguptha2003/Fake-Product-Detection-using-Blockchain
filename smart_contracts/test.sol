// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SupplyChain {
    address public owner;

    struct product{
        uint productId;
        string role;
        string productName;
        productStatus []  StatusAtStop;
    }
    struct productStatus{
        string status;
        string source;
        string destination;
        string remarks;
    }
    mapping(uint => product) public products;
    uint public productCount;
    

    event ProductAdded(
        uint productId,
        string role,
        string productName,
        string status,
        string source,
        string destination,
        string remarks
    );
    function ProductAdd  ( uint _productId, string memory _role, string memory _productName, string memory _status, string memory _source, string memory _destination, string memory _remarks) public{
        productCount++;
        products[productCount].productId = _productId;
        products[productCount].role = _role;
        products[productCount].productName = _productName;

        products[productCount].StatusAtStop.push(productStatus(_status, _source, _destination, _remarks));
    }
    constructor() {
        owner = msg.sender;
    }
    function GetProduct(uint _productId) public view returns (uint, string memory, string memory, productStatus[] memory){
        return (products[_productId].productId, products[_productId].role, products[_productId].productName, products[_productId].StatusAtStop);

    }
    function GetProductCount() public view returns (uint){
        return productCount;
    }
    function StatusAddtoProduct(uint _product_id, string memory _status, string memory  _source, string memory _destination, string memory _remarks) public{
        products[_product_id].StatusAtStop.push(productStatus( _status,_source, _destination, _remarks));
    }
    
    
}