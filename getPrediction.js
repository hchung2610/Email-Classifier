let userInput = document.getElementsByName("userInput");
console.log(userInput);

let form = userInput[0];
if (form) {
    form.addEventListener("submit", async (e) => {
        e.preventDefault();    
        let model = document.getElementsByName("model")[0].value;
        let variant = document.getElementsByName("variant")[0].value;
        let email = document.getElementsByName("email")[0].value;
        let prediction = await requestPrediction(model, variant, email);
        alert(prediction['prediction']);
    });
};

async function requestPrediction(model, variant, email) {
    let url = "http://localhost:5000/predict/" + model + "/" + variant + "/" + email;
    let response = await fetch(url).then(res => res.json());
    return response;
};

