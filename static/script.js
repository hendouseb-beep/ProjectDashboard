document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".card");
  const total = cards.length;
  document.getElementById("total-count").textContent = total;

  const counts = { "En cours": 0, "Terminé": 0, "En attente": 0, "Retardé": 0 };
  cards.forEach(c => counts[c.dataset.status]++);

  document.getElementById("en-cours-count").textContent = counts["En cours"];
  document.getElementById("termine-count").textContent = counts["Terminé"];
  document.getElementById("attente-count").textContent = counts["En attente"];
  document.getElementById("retarde-count").textContent = counts["Retardé"];

  const filter = document.getElementById("statusFilter");
  filter.addEventListener("change", e => {
    const val = e.target.value;
    cards.forEach(c => {
      if (val === "Tous" || c.dataset.status === val) {
        c.style.display = "block";
      } else {
        c.style.display = "none";
      }
    });
  });
});
