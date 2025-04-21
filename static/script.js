document.addEventListener("DOMContentLoaded", function() {
    let counters = document.querySelectorAll("span[id^='count']");

    let observerOptions = {
        root: null,  // Uses the viewport
        threshold: 0.5,  // Trigger when 50% of the element is visible
    };

    function runCounter(entry) {
        if (entry.isIntersecting) {
            let element = entry.target;
            let targetCount = parseInt(element.getAttribute("data-count"), 10);
            let currentCount = 0;

            function updateCounter() {
                if (currentCount <= targetCount) {
                    element.innerText = currentCount + "+";
                    currentCount++;
                    setTimeout(updateCounter, 50);
                }
            }

            updateCounter();
            observer.unobserve(element);  // Stop observing once counter runs
        }
    }

    let observer = new IntersectionObserver((entries) => {
        entries.forEach(runCounter);
    }, observerOptions);

    counters.forEach(counter => {
        observer.observe(counter);
    });
});





