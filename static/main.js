const toggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelector("#nav-links");

if (toggle && navLinks) {
  toggle.addEventListener("click", () => {
    const isOpen = toggle.getAttribute("aria-expanded") === "true";
    toggle.setAttribute("aria-expanded", String(!isOpen));
    navLinks.classList.toggle("is-open", !isOpen);
  });

  navLinks.addEventListener("click", (event) => {
    if (event.target instanceof HTMLAnchorElement) {
      toggle.setAttribute("aria-expanded", "false");
      navLinks.classList.remove("is-open");
    }
  });
}

const counters = document.querySelectorAll("[data-counter]");

const parseTarget = (value) => {
  const match = value.match(/^\d+/);
  return match ? Number(match[0]) : null;
};

const animateCounter = (element) => {
  const original = element.dataset.counter;
  const target = parseTarget(original);
  if (!original || target === null || element.dataset.done === "true") return;

  element.dataset.done = "true";
  const suffix = original.replace(String(target), "");
  const duration = 900;
  const start = performance.now();

  const tick = (now) => {
    const progress = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    element.textContent = `${Math.round(target * eased)}${suffix}`;
    if (progress < 1) requestAnimationFrame(tick);
  };

  requestAnimationFrame(tick);
};

if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) animateCounter(entry.target);
      });
    },
    { threshold: 0.35 },
  );
  counters.forEach((counter) => observer.observe(counter));
} else {
  counters.forEach(animateCounter);
}
