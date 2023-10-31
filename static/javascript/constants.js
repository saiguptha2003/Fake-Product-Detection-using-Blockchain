export const contractAddress = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512";

export const abi = [
  {
    inputs: [],
    stateMutability: "nonpayable",
    type: "constructor",
  },
  {
    anonymous: false,
    inputs: [
      {
        indexed: false,
        internalType: "uint256",
        name: "productId",
        type: "uint256",
      },
      {
        indexed: false,
        internalType: "string",
        name: "role",
        type: "string",
      },
      {
        indexed: false,
        internalType: "string",
        name: "productName",
        type: "string",
      },
      {
        indexed: false,
        internalType: "string",
        name: "status",
        type: "string",
      },
      {
        indexed: false,
        internalType: "string",
        name: "source",
        type: "string",
      },
      {
        indexed: false,
        internalType: "string",
        name: "destination",
        type: "string",
      },
      {
        indexed: false,
        internalType: "string",
        name: "remarks",
        type: "string",
      },
    ],
    name: "ProductAdded",
    type: "event",
  },
  {
    inputs: [
      {
        internalType: "uint256",
        name: "_productId",
        type: "uint256",
      },
    ],
    name: "GetProduct",
    outputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
      {
        internalType: "string",
        name: "",
        type: "string",
      },
      {
        internalType: "string",
        name: "",
        type: "string",
      },
      {
        components: [
          {
            internalType: "string",
            name: "status",
            type: "string",
          },
          {
            internalType: "string",
            name: "source",
            type: "string",
          },
          {
            internalType: "string",
            name: "destination",
            type: "string",
          },
          {
            internalType: "string",
            name: "remarks",
            type: "string",
          },
        ],
        internalType: "struct SupplyChain.productStatus[]",
        name: "",
        type: "tuple[]",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [],
    name: "GetProductCount",
    outputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "uint256",
        name: "_productId",
        type: "uint256",
      },
      {
        internalType: "string",
        name: "_role",
        type: "string",
      },
      {
        internalType: "string",
        name: "_productName",
        type: "string",
      },
      {
        internalType: "string",
        name: "_status",
        type: "string",
      },
      {
        internalType: "string",
        name: "_source",
        type: "string",
      },
      {
        internalType: "string",
        name: "_destination",
        type: "string",
      },
      {
        internalType: "string",
        name: "_remarks",
        type: "string",
      },
    ],
    name: "ProductAdd",
    outputs: [],
    stateMutability: "nonpayable",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "uint256",
        name: "_product_id",
        type: "uint256",
      },
      {
        internalType: "string",
        name: "_status",
        type: "string",
      },
      {
        internalType: "string",
        name: "_source",
        type: "string",
      },
      {
        internalType: "string",
        name: "_destination",
        type: "string",
      },
      {
        internalType: "string",
        name: "_remarks",
        type: "string",
      },
    ],
    name: "StatusAddtoProduct",
    outputs: [],
    stateMutability: "nonpayable",
    type: "function",
  },
  {
    inputs: [],
    name: "owner",
    outputs: [
      {
        internalType: "address",
        name: "",
        type: "address",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [],
    name: "productCount",
    outputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    name: "products",
    outputs: [
      {
        internalType: "uint256",
        name: "productId",
        type: "uint256",
      },
      {
        internalType: "string",
        name: "role",
        type: "string",
      },
      {
        internalType: "string",
        name: "productName",
        type: "string",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
];
