import { abi } from "./constants.js";
import { ethers } from "./ethers.js";

const contractAddress = "0x696083a889ab7799cf66512dd7b2b770f0ac9aa7";
const contractABI = abi;

const connectButton = document.getElementById("connectButton");
connectButton.onclick = connect;

async function connect() {
  if (window.ethereum) {
    await window.ethereum.request({ method: "eth_requestAccounts" });
    document.getElementById("connectButton").innerHTML = "Send Transcation";
    document.getElementById("connectButton").onclick = maketranscation;
  } else {
    alert("Please install Metamask");
  }
}
async function maketranscation(){
  let productName = document.getElementById('ProductName').value;
  let status = document.getElementById('status').value;
  let destination = document.getElementById('destination').value;
  let remarks = document.getElementById('remarks').value;
  let product_id = document.getElementById('product_id').value;

  sendTransaction(product_id,'manufacturer',productName,status,'Factory',destination,remarks);
  sendDataToFlask();
}
async function sendTransaction(product_id, role,product_name, status,source, destination,remarks) {
  if (window.ethereum) {
    connectButton.innerHTML = " mining...";
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    const contract = new ethers.Contract(contractAddress, contractABI, signer);

    try {
      const transactionResponse = await contract.ProductAdd(product_id, role,product_name, status,source, destination,remarks);
      // Listen for the transaction to be mined, wait until mined
      await listenForTransactionMine(transactionResponse, provider); // await is working as we are waiting for promise
      console.log("Done!");
      connectButton.innerHTML = "Transcation Done!🎉🎉🎉";
    }

    catch (error) {
      connectButton.innerHTML = "Transcation Failed! :(";
      console.error("Transaction failed:", error);
    }
  } else {
    alert("Please install Metamask");
  }
}

function listenForTransactionMine(transactionResponse, provider) {
  console.log(`Mining ${transactionResponse.hash}...`);
  // This promise will wait for until the listner is completed and will call resolve if its completed succesfully else reject
  return new Promise((resolve, reject) => {
    // listen for this transaction to finish( This listner will call callback-function once there is one confirmation)
    provider.once(transactionResponse.hash, (transactionReciept) => {
      // Print the number of confirmations
      console.log(
        `Completed with ${transactionReciept.confirmations} Confirmations`
      );
      resolve();
    });
  });
}

async function getData() {
  if (window.ethereum) {
    console.log("getting....");
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    const contract = new ethers.Contract(contractAddress, contractABI, signer);
    try {
      const transactionResponse = await contract.GetProduct(1);
      console.log(transactionResponse);
    } catch (error) {
      console.log(error);
    }
  }
}



function sendDataToFlask()
{
  let productName = document.getElementById('ProductName').value;
  let status = document.getElementById('status').value;
  let destination = document.getElementById('destination').value;
  let remarks = document.getElementById('remarks').value;
  let role = 'manufacturer';
  let source = 'Factory';
  let product_id = document.getElementById('product_id').value;
  const data = {
    productName: productName,
    status: status,
    destination: destination,
    remarks: remarks,
    product_id: product_id,
    role: role,
    source: source,
  };

  fetch('/Manufacturer/addproduct', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
    })
    .catch(error => {
      console.error('Error:', error);
    });
}