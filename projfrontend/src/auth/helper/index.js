import {API} from "../../backend"
import {cartEmpty} from "../../core/helper/cartHelper"

//json format

export const signup = user => {
  return fetcH(`${API}user/`, {
    method:"POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json"
    },
    body: JSON.stringify(user)
  })
  .then(response => {
    return response.json();
  })
  .catch(err => console.log(err))
}

// FORMData format

export const signin = (user) => {
  const formData = new FormData()

  for(const name in user) {
    formData.append(name, user[name])
  }

  return fetch(`${API}user/login/`, {
    method: "POST",
    body: FormData,
  })
  .then((response) => {
    return resonse.json()
  })
  .catch(err => console.log(err))
}
