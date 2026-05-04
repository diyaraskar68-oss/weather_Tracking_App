const cityInput = document.getElementById("city");
const weatherInfo = null;
const weatherInfotext = document.getElementById("weatherinfo");

cityInput.addEventListener("change", (event) => {
    const city = event.target.value;

    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=17596f2923a62b58389a861c0ba70e3a&units=metric`)
        .then(response => response.json()) // convert to data
        .then(data => {
            console.log(data); // full weather data

            // example: access specific info
            console.log("Temperature:", data.main.temp);
            console.log("Weather:", data.weather[0].description);
        })
        .catch(error => console.error("Error:", error));

    weatherInfo = data; // save data to global variable
});

weatherInfotext.textContent = weatherInfo;