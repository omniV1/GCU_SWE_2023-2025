document.addEventListener('DOMContentLoaded', function () {
    /**
     * Creates and animates confetti particles
     */
    function createConfetti() {
        const colors = ['#22c55e', '#16a34a', '#fbbf24', '#f87171'];
        const confettiCount = 50;

        for (let i = 0; i < confettiCount; i++) {
            setTimeout(() => {
                const confetti = document.createElement('div');
                confetti.className = 'confetti';
                confetti.style.left = `${Math.random() * 100}vw`;
                confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
                confetti.style.width = '10px';
                confetti.style.height = '10px';
                confetti.style.position = 'fixed';
                confetti.style.animation = 'confetti 2s linear forwards';

                document.body.appendChild(confetti);

                // Remove confetti after animation
                confetti.addEventListener('animationend', () => confetti.remove());
            }, i * 50); // Stagger confetti creation
        }
    }

    // Initialize confetti when page loads
    createConfetti();
});