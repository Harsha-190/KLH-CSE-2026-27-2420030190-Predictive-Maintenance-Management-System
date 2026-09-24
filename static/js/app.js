document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("predictionForm");

    if (form) {
        form.addEventListener("submit", async (event) => {
            event.preventDefault();

            const data = Object.fromEntries(new FormData(form).entries());

            ["temperature", "vibration", "pressure", "runtime_hours",
             "machine_age", "load_percentage"].forEach(key => {
                data[key] = Number(data[key]);
            });

            const button = form.querySelector("button");
            button.disabled = true;
            button.textContent = "Analyzing...";

            try {
                const response = await fetch("/predict", {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify(data)
                });

                const result = await response.json();

                if (!response.ok) {
                    throw new Error(result.error || "Prediction failed.");
                }

                const box = document.getElementById("predictionResult");
                const riskText = document.getElementById("riskText");

                box.classList.remove("hidden");
                riskText.textContent = result.prediction + " RISK";
                riskText.className = "result-risk " + result.prediction.toLowerCase();

                document.getElementById("probabilityText").textContent =
                    result.probability + "%";

                document.getElementById("recommendationText").textContent =
                    result.recommendation;

                loadChart();
            } catch (error) {
                alert(error.message);
            } finally {
                button.disabled = false;
                button.textContent = "Predict Maintenance Risk";
            }
        });
    }

    loadChart();
});

async function loadChart() {
    const canvas = document.getElementById("riskChart");
    if (!canvas) return;

    try {
        const response = await fetch("/api/stats");
        const data = await response.json();

        if (window.riskChartInstance) {
            window.riskChartInstance.destroy();
        }

        window.riskChartInstance = new Chart(canvas, {
            type: "doughnut",
            data: {
                labels: data.labels,
                datasets: [{
                    data: data.values,
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: "bottom"
                    }
                }
            }
        });
    } catch (error) {
        console.error("Could not load chart:", error);
    }
}
