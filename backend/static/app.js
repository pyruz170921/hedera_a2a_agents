// Botón de prueba de conexión
document.getElementById("ping").addEventListener("click", async () => {
    const res = await fetch("/");
    const text = await res.text();
    document.getElementById("output").textContent = text;
});

// Envío del formulario de PaymentIntent
document.getElementById("paymentForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = Object.fromEntries(new FormData(e.target));
    const res = await fetch("/payments/create", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
    });
    const data = await res.json();
    document.getElementById("paymentResult").textContent = JSON.stringify(data, null, 2);
});
