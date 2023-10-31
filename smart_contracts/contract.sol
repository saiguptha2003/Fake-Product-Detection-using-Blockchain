// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SupplyChain {
    address public owner;

    enum Role { Manufacturer, Supplier, Customer }

    struct Product {
        uint productId;
        Role role;
        address entity;
        string serialNumber;
        string productName;
        string source;
        string destination;
        string remarks;
    }

    mapping(uint => Product) public products;
    uint public productCount;

    event ProductAdded(
        uint productId,
        Role role,
        address entity,
        string serialNumber,
        string productName,
        string source,
        string destination,
        string remarks
    );

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    function addProduct(
        Role _role,
        string memory _serialNumber,
        string memory _productName,
        string memory _source,
        string memory _destination,
        string memory _remarks
    ) public {
        require(_role != Role.Customer, "Customers can only verify products.");
        productCount++;
        products[productCount] = Product(
            productCount,
            _role,
            msg.sender,
            _serialNumber,
            _productName,
            _source,
            _destination,
            _remarks
        );
        emit ProductAdded(
            productCount,
            _role,
            msg.sender,
            _serialNumber,
            _productName,
            _source,
            _destination,
            _remarks
        );
    }

    function updateProductDetails(
        uint _productId,
        string memory _source,
        string memory _destination,
        string memory _remarks
    ) public {
        require(_productId <= productCount, "Invalid product ID");
        Product storage product = products[_productId];
        require(msg.sender == product.entity, "Only the product owner can update details");
        product.source = _source;
        product.destination = _destination;
        product.remarks = _remarks;
    }

    function getProduct(uint _productId) public view returns (Product memory) {
        require(_productId <= productCount, "Invalid product ID");
        return products[_productId];
    }
}
