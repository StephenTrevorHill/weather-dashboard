
document.addEventListener("DOMContentLoaded", () => {
    const countryPicker = document.getElementById("country-picker");
    const cityPicker = document.getElementById("city-picker");

    // Fetch country list
    fetch("/api/countries")
        .then(res => res.json())
        .then(countries => {
            countries.forEach(country => {
                const option = document.createElement("option");
                option.value = country;
                option.textContent = country;
                countryPicker.appendChild(option);
            });
        });

    // Load cities on country change
    countryPicker.addEventListener("change", () => {
        const country = countryPicker.value;
        cityPicker.innerHTML = '<option value="">Select city</option>';
        cityPicker.disabled = true;

        if (country) {
            fetch(`/api/cities?country=${encodeURIComponent(country)}`)
                .then(res => res.json())
                .then(cities => {
                    cities.forEach(city => {
                        const option = document.createElement("option");
                        option.value = city;
                        option.textContent = city;
                        cityPicker.appendChild(option);
                    });
                    cityPicker.disabled = false;
                });
        }
    });
});

