document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("btn").addEventListener("click", () => {
    const height = Number(document.getElementById("height").value);
    const weight = Number(document.getElementById("weight").value);

    if (isNaN(weight) || isNaN(height) ){
    console.log("Error");
    return;
    }
    const bmi = Math.round(weight / (height / 100)**2);
    let message = `あなたのBMIは${bmi.toFixed(1)}です。`;
    if(bmi >= 25){
        message += "肥満体重です。";
    }else if (bmi>=18.5){
        message +="普通体重です。";
    }else{
        message +="瘦せ型です。";
    }
    document.getElementById("result").innerText = message;

  });
});
