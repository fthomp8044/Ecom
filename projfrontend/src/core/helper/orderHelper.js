import {API} from "../../backend";

export const createOrder = (userId, token, orderData) => {
  const fromData = new FormData();

  for (const name in orderData) {
    formData.append(name, orderData[name])
  }
//create an order based on the formdata from the backend
  return fetch(`$[API]order/add/${userId}/${token}/`, {
    method: 'POST',
    body: formData
  })
  .then(response => {
    return response.json()
  })
  .catch(err => console.log(err))
}
