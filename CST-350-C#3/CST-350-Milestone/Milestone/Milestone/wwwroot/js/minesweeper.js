/**
 * Minesweeper Game Implementation
 * 
 * This file contains the core game logic for the Minesweeper game, including:
 * - Game state management and initialization
 * - Board interaction handlers (clicks, right-clicks)
 * - Save/load game functionality
 * - Timer and mine counter management
 * - Cell revelation and flag placement logic
 */

document.addEventListener('DOMContentLoaded', () => {
    /**
     * Core Game Variables
     * gameBoard: Main game board element containing all cells
     * gameId: Unique identifier for current game session
     * remainingMines: Counter for unflagged mines
     * gameTimer: Reference to the interval timer for cleanup
     * autoSaveInterval: Reference to the automatic save interval
     * startTime: Timestamp when game began, used for scoring
     * isGameOver: Flag to prevent actions after game ends
     */
    const gameBoard = document.getElementById('gameBoard');
    const gameId = gameBoard.dataset.gameId;
    let remainingMines = parseInt(gameBoard.dataset.mines);
    let gameTimer;
    let autoSaveInterval;
    let startTime = new Date();
    let isGameOver = false;

    console.log('Game initialization - ID:', gameId, 'Total Mines:', remainingMines);

    /**
     * Restores a previously saved game state from serialized data
     * 
     * This function handles:
     * - Reading the initial state from the gameBoard's data attributes
     * - Restoring revealed cells with their correct numbers/mines
     * - Restoring flagged cells
     * - Updating the mine counter to reflect restored flags
     * - Maintaining game consistency after reload
     * 
     * The restoration process ensures that:
     * 1. All revealed cells show their correct state (empty, number, or mine)
     * 2. All flags are restored to their exact positions
     * 3. The mine counter accurately reflects the number of remaining mines
     * 4. The visual state of the board matches the saved game state
     */
    function restoreGameState() {
        try {
            // Attempt to retrieve saved state data
            const initialStateJson = gameBoard.dataset.initialState;
            if (!initialStateJson) {
                console.log('No saved state found - starting new game');
                return;
            }

            // Parse the saved state data
            const initialState = JSON.parse(initialStateJson);
            console.log('Restoring saved game state:', initialState);

            // Track flags for mine counter adjustment
            let flagCount = 0;

            // Process each cell from the saved state
            initialState.forEach(cellState => {
                // Find the corresponding DOM element for this cell
                const cell = document.querySelector(
                    `.cell[data-row="${cellState.row}"][data-col="${cellState.column}"]`
                );

                if (cell) {
                    // Restore revealed cells
                    if (cellState.isRevealed) {
                        cell.classList.add('revealed');
                        if (cellState.isMine) {
                            // Restore revealed mines
                            cell.classList.add('mine');
                            cell.textContent = '💣';
                        } else if (cellState.neighborCount > 0) {
                            // Restore number cells
                            cell.textContent = cellState.neighborCount;
                        }
                    }

                    // Restore flagged cells
                    if (cellState.isFlagged) {
                        cell.classList.add('flagged');
                        cell.textContent = '🚩';
                        flagCount++;
                    }
                }
            });

            // Update the mine counter to account for restored flags
            remainingMines -= flagCount;
            updateMineCounter();

        } catch (error) {
            console.error('Failed to restore game state:', error);
            console.error('Stack trace:', error.stack);
        }
    }

    /**
     * Timer Management System
     * 
     * These functions handle the game timer display and updates:
     * - startTimer: Initializes and starts the time tracking
     * - updateTimer: Updates the timer display every second
     * 
     * The timer:
     * - Displays in MM:SS format
     * - Updates every second
     * - Used for scoring calculations
     * - Starts when game begins
     * - Stops when game ends
     */
    function startTimer() {
        gameTimer = setInterval(updateTimer, 1000);
        console.log('Game timer started');
    }

    /**
     * Updates the game timer display
     * 
     * Calculates elapsed time since game start and formats it as MM:SS
     * - Converts total seconds to minutes and remaining seconds
     * - Adds leading zeros for consistent formatting
     * - Updates the timer element in the DOM
     */
    function updateTimer() {
        const elapsed = Math.floor((new Date() - startTime) / 1000);
        const minutes = Math.floor(elapsed / 60).toString().padStart(2, '0');
        const seconds = (elapsed % 60).toString().padStart(2, '0');
        document.getElementById('timer').textContent = `${minutes}:${seconds}`;
    }

    /**
     * Mine Counter Management
     * 
     * Updates the mine counter display with remaining unflagged mines
     * - Formats number with leading zeros (e.g., "007")
     * - Updates whenever flags are placed or removed
     * - Helps player track remaining mines
     * 
     * @requires Element with class 'mine-counter' to exist in DOM
     */
    function updateMineCounter() {
        const counter = document.querySelector('.mine-counter');
        if (counter) {
            counter.textContent = remainingMines.toString().padStart(3, '0');
            console.log('Mine counter updated:', remainingMines);
        }
    }

    /**
     * Adjacent Cells Calculator
     * 
     * Returns an array of all valid adjacent cells for a given position
     * Used for both chord reveals and number calculations
     * 
     * @param {number} row - Row coordinate of the center cell
     * @param {number} col - Column coordinate of the center cell
     * @returns {Array} Array of adjacent cell DOM elements
     * 
     * Behavior:
     * - Checks all 8 surrounding positions (diagonal included)
     * - Handles edge and corner cases (returns fewer cells)
     * - Skips the center cell itself
     * - Only returns valid cells within the game board
     */
    function getAdjacentCells(row, col) {
        const cells = [];
        // Check all 8 surrounding positions
        for (let i = -1; i <= 1; i++) {
            for (let j = -1; j <= 1; j++) {
                // Skip the center cell
                if (i === 0 && j === 0) continue;

                // Find adjacent cell in DOM
                const adjacentCell = document.querySelector(
                    `.cell[data-row="${row + i}"][data-col="${col + j}"]`
                );

                // Only add if cell exists (handles board edges)
                if (adjacentCell) cells.push(adjacentCell);
            }
        }
        return cells;
    }

    /**
     * Auto-Save System
     * 
     * Automatically saves the current game state to prevent progress loss
     * 
     * Triggers:
     * - Every 30 seconds during gameplay
     * - When switching tabs
     * - Before page unload (if possible)
     * 
     * @returns {Promise<void>} Resolves when save is complete
     * @throws {Error} If save operation fails
     */
    async function autoSaveGame() {
        try {
            // Prepare game state data
            const formData = new FormData();
            formData.append('gameId', gameId);

            // Send save request to server
            const response = await fetch('/Game/SaveGame', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error('Failed to auto-save game');
            }
            console.log('Auto-save completed successfully');
        } catch (error) {
            console.error('Auto-save failed:', error);
            console.error('Stack trace:', error.stack);
        }
    }

    /**
     * Initializes the auto-save interval timer
     * 
     * Sets up periodic auto-saving every 30 seconds while:
     * - Game is in progress (not over)
     * - Player is still playing
     * 
     * Cleans up:
     * - Stops when game ends
     * - Prevents unnecessary saves
     */
    function startAutoSave() {
        autoSaveInterval = setInterval(async () => {
            if (!isGameOver) {
                await autoSaveGame();
            } else {
                clearInterval(autoSaveInterval);
                console.log('Auto-save stopped - game over');
            }
        }, 30000); // 30 second intervals
        console.log('Auto-save system initialized');
    }
    /**
     * Manual Save Game Handler
     * 
     * Handles explicit save requests when player clicks the save button
     * - Creates and sends save request to server
     * - Provides user feedback on save status
     * - Handles error cases gracefully
     * 
     * @listens click on element with id 'saveGameBtn'
     * @returns {Promise<void>} Resolves when save operation completes
     */
    document.getElementById('saveGameBtn').addEventListener('click', async function () {
        try {
            const formData = new FormData();
            formData.append('gameId', gameId);

            const response = await fetch('/Game/SaveGame', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                const errorText = await response.text();
                throw new Error(errorText || 'Failed to save game');
            }

            const result = await response.json();
            if (result.success) {
                alert('Game saved successfully!');
            } else {
                alert('Failed to save game. Please try again.');
            }
        } catch (error) {
            console.error('Save game error:', error);
            alert('An error occurred while saving the game. Please try again.');
        }
    });

    /**
     * Cell Click Handler
     * 
     * Processes left-click actions on cells:
     * - Reveals clicked cell if not flagged
     * - Handles mine hits
     * - Triggers cascade reveals for empty cells
     * - Updates game state based on server response
     * 
     * @param {MouseEvent} event - The click event object
     * @returns {Promise<void>} Resolves when cell reveal is complete
     */
    async function handleCellClick(event) {
        try {
            if (isGameOver) return;

            const cell = event.target;
            if (cell.classList.contains('revealed') || cell.classList.contains('flagged')) return;

            const row = parseInt(cell.dataset.row);
            const col = parseInt(cell.dataset.col);

            // Request cell reveal from server
            const response = await fetch('/Game/RevealCell', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    Row: row,
                    Col: col,
                    GameId: gameId
                })
            });

            if (!response.ok) {
                throw new Error(`Server returned ${response.status}`);
            }

            // Process server response
            const result = await response.json();
            if (result.revealedCells) {
                result.revealedCells.forEach(cellInfo => {
                    const targetCell = document.querySelector(
                        `.cell[data-row="${cellInfo.row}"][data-col="${cellInfo.column}"]`
                    );
                    if (targetCell) {
                        targetCell.classList.add('revealed');
                        if (cellInfo.isMine) {
                            targetCell.classList.add('mine');
                            targetCell.textContent = '💣';
                        } else if (cellInfo.neighborCount > 0) {
                            targetCell.textContent = cellInfo.neighborCount;
                        }
                    }
                });

                if (result.isGameOver) {
                    handleGameOver(result);
                }
            }
        } catch (error) {
            console.error('Cell click error:', error);
        }
    }

    /**
     * Right Click Handler
     * 
     * Manages flag placement and removal:
     * - Toggles flags on unrevealedcells
     * - Updates mine counter
     * - Prevents flagging of revealed cells
     * - Enforces maximum flag limit
     * 
     * @param {MouseEvent} event - The right-click event object
     */
    function handleRightClick(event) {
        event.preventDefault();
        if (isGameOver) return;

        const cell = event.target;
        if (cell.classList.contains('revealed')) return;

        // Toggle flag state
        if (cell.classList.contains('flagged')) {
            // Remove flag
            cell.classList.remove('flagged');
            cell.textContent = '';
            remainingMines++;
            cell.classList.remove('cell-pressed');
        } else if (remainingMines > 0) {
            // Add flag if we haven't used all flags
            cell.classList.add('flagged');
            cell.textContent = '🚩';
            remainingMines--;
            cell.classList.add('cell-pressed');
        }

        updateMineCounter();
    }

    /**
     * Mouse Down Handler
     * 
     * Initializes the peek functionality:
     * - Shows adjacent cells when right-clicking a revealed number
     * - Provides visual feedback for chord reveal preparation
     * - Only activates on valid numbered cells
     * 
     * @param {MouseEvent} event - The mousedown event object
     */
    function handleMouseDown(event) {
        if (event.button === 2) { // Right mouse button
            const cell = event.target;
            if (!cell.classList.contains('revealed') ||
                !cell.textContent ||
                cell.textContent === '🚩' ||
                cell.textContent === '💣') {
                return;
            }

            cell.classList.add('cell-pressed');
            const row = parseInt(cell.dataset.row);
            const col = parseInt(cell.dataset.col);
            const adjacentCells = getAdjacentCells(row, col);

            adjacentCells.forEach(adjCell => {
                if (!adjCell.classList.contains('flagged') &&
                    !adjCell.classList.contains('revealed')) {
                    adjCell.classList.add('peek');
                    adjCell.classList.add('cell-pressed');
                }
            });
        }
    }

    /**
     * Mouse Up Handler (Chord Reveal)
     * 
     * Handles chord reveal operations:
     * - Validates flag count matches cell number
     * - Reveals unflagged adjacent cells
     * - Processes potential game over conditions
     * - Cleans up peek effects
     * 
     * @param {MouseEvent} event - The mouseup event object
     * @returns {Promise<void>} Resolves when chord reveal completes
     */
    async function handleMouseUp(event) {
        if (event.button === 2) {
            const cell = event.target;

            // Clean up peek effects
            document.querySelectorAll('.peek, .cell-pressed').forEach(cell => {
                cell.classList.remove('peek');
                cell.classList.remove('cell-pressed');
            });

            // Validate cell eligibility for chord reveal
            if (!cell.classList.contains('revealed') ||
                !cell.textContent ||
                cell.textContent === '🚩' ||
                cell.textContent === '💣') {
                return;
            }

            const row = parseInt(cell.dataset.row);
            const col = parseInt(cell.dataset.col);
            const number = parseInt(cell.textContent);

            const adjacentCells = getAdjacentCells(row, col);
            const flagCount = adjacentCells.filter(adjCell =>
                adjCell.classList.contains('flagged')).length;

            // Only proceed if flags match the number
            if (flagCount === number) {
                const cellsToReveal = adjacentCells.filter(adjCell =>
                    !adjCell.classList.contains('flagged') &&
                    !adjCell.classList.contains('revealed'));

                for (const adjCell of cellsToReveal) {
                    const adjRow = parseInt(adjCell.dataset.row);
                    const adjCol = parseInt(adjCell.dataset.col);

                    try {
                        // Request cell reveal from server
                        const response = await fetch('/Game/RevealCell', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({
                                Row: adjRow,
                                Col: adjCol,
                                GameId: gameId
                            })
                        });

                        if (!response.ok) {
                            throw new Error(`Server returned ${response.status}`);
                        }

                        const result = await response.json();
                        processRevealResult(result);

                        if (result.isGameOver) {
                            handleGameOver(result);
                            break;
                        }
                    } catch (error) {
                        console.error('Chord reveal error:', error);
                    }
                }
            }
        }
    }

    /**
     * Process Reveal Result
     * 
     * Helper function to handle cell reveal responses:
     * - Updates revealed cells in the UI
     * - Handles mine reveals
     * - Shows adjacent mine counts
     * 
     * @param {Object} result - The server response containing revealed cells
     */
    function processRevealResult(result) {
        if (result.revealedCells) {
            result.revealedCells.forEach(cellInfo => {
                const targetCell = document.querySelector(
                    `.cell[data-row="${cellInfo.row}"][data-col="${cellInfo.column}"]`
                );
                if (targetCell) {
                    targetCell.classList.add('revealed');
                    if (cellInfo.isMine) {
                        targetCell.classList.add('mine');
                        targetCell.textContent = '💣';
                    } else if (cellInfo.neighborCount > 0) {
                        targetCell.textContent = cellInfo.neighborCount;
                    }
                }
            });
        }
    }

    /**
     * Mouse Leave Handler
     * 
     * Cleans up peek effects when mouse leaves a cell:
     * - Removes peek visual effects
     * - Prevents stuck visual states
     * 
     * @param {MouseEvent} event - The mouseleave event object
     */
    function handleMouseLeave() {
        document.querySelectorAll('.peek').forEach(cell => {
            cell.classList.remove('peek');
        });
    }

    /**
     * Game Over Handler
     * 
     * Manages end-of-game procedures:
     * - Stops timers and intervals
     * - Calculates final score
     * - Sends game completion to server
     * - Redirects to appropriate end screen
     * 
     * @param {Object} result - The game over result data
     * @returns {Promise<void>} Resolves when end game processing completes
     */
    async function handleGameOver(result) {
        isGameOver = true;
        clearInterval(gameTimer);
        clearInterval(autoSaveInterval);

        const timeElapsed = Math.floor((new Date() - startTime) / 1000);
        const score = calculateScore(timeElapsed, remainingMines);
        const finalTime = document.getElementById('timer').textContent;

        const params = new URLSearchParams({
            gameId: gameId,
            isVictory: result.isVictory,
            score: score,
            time: finalTime
        }).toString();

        try {
            await fetch(`/Game/EndGame?${params}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' }
            });
            window.location.href = `/Game/EndGame?${params}`;
        } catch (error) {
            console.error('Game over error:', error);
        }
    }

    /**
     * Score Calculator
     * 
     * Calculates final game score based on:
     * - Time taken to complete
     * - Remaining mines
     * - Base score value
     * 
     * @param {number} timeElapsed - Time taken in seconds
     * @param {number} remainingMines - Number of unflagged mines
     * @returns {number} The calculated score
     */
    function calculateScore(timeElapsed, remainingMines) {
        const baseScore = 1000;
        const timeDeduction = timeElapsed * 2;
        const mineBonus = remainingMines * 50;
        return Math.max(0, baseScore - timeDeduction + mineBonus);
    }

    // Set up cell event listeners
    document.querySelectorAll('.cell').forEach(cell => {
        cell.addEventListener('click', handleCellClick);
        cell.addEventListener('contextmenu', handleRightClick);
        cell.addEventListener('mousedown', handleMouseDown);
        cell.addEventListener('mouseup', handleMouseUp);
        cell.addEventListener('mouseleave', handleMouseLeave);

        // Check for initial states
        if (cell.dataset.revealed === 'true') {
            cell.classList.add('revealed');
        }
        if (cell.dataset.flagged === 'true') {
            cell.classList.add('flagged');
            cell.textContent = '🚩';
        }
    });

    // Global mouse event cleanup
    document.querySelector('.game-board').addEventListener('mouseleave', () => {
        document.querySelectorAll('.peek, .cell-pressed').forEach(cell => {
            cell.classList.remove('peek');
            cell.classList.remove('cell-pressed');
        });
    });

    // Global mouseup cleanup
    window.addEventListener('mouseup', (event) => {
        if (event.button === 2) {
            document.querySelectorAll('.peek, .cell-pressed').forEach(cell => {
                cell.classList.remove('peek');
                cell.classList.remove('cell-pressed');
            });
        }
    });

    // Auto-save events
    window.addEventListener('beforeunload', async function (e) {
        if (!isGameOver) {
            e.preventDefault();
            e.returnValue = 'You have an ongoing game. The game will be automatically saved.';
            await autoSaveGame();
        }
    });

    document.addEventListener('visibilitychange', function () {
        if (document.visibilityState === 'hidden' && !isGameOver) {
            autoSaveGame();
        }
    });

    // Initialize game
    restoreGameState();
    startTimer();
    startAutoSave();
    updateMineCounter();
});