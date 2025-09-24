/**
 * Game Over Animation Handler
 * Initializes and manages the shake animation for the game over screen
 */
document.addEventListener('DOMContentLoaded', function () {
    /**
     * Adds and removes the shake animation class from the game over container
     * Animation is removed after completion to allow for potential replay
     */
    function initializeShakeAnimation() {
        // Get reference to the main game over container
        const gameoverContainer = document.querySelector('.game-over-container');

        // Add shake animation class
        gameoverContainer.classList.add('shake');

        // Remove animation class after completion
        // Timeout matches the animation duration in CSS
        setTimeout(() => {
            gameoverContainer.classList.remove('shake');
        }, 500);  // 500ms matches CSS animation duration
    }

    // Initialize the animation when DOM is ready
    initializeShakeAnimation();
});