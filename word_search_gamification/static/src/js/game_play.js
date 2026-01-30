/** @odoo-module **/

import { Component, onMounted, onWillUnmount, useState } from "@odoo/owl";

// Simple vanilla JS implementation
(function() {
    'use strict';

    let gameState = {
        gameId: 0,
        words: [],
        foundWords: [],
        score: 0,
        startTime: 0,
        isSelecting: false,
        selectedCells: [],
        timerInterval: null,
        attemptSaved: false
    };

    function initGame() {
        // Wait for DOM to be ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', setupGame);
        } else {
            setupGame();
        }
    }

    function setupGame() {
        const gameIdEl = document.getElementById('game-id');
        const wordsDataEl = document.getElementById('words-data');
        
        if (!gameIdEl || !wordsDataEl) {
            console.error('Game elements not found');
            return;
        }

        gameState.gameId = parseInt(gameIdEl.value);
        gameState.words = JSON.parse(wordsDataEl.value);
        gameState.startTime = Date.now();
        
        // Start timer
        startTimer();
        
        // Bind cell events
        bindCellEvents();
        
        // Bind button events
        bindButtonEvents();
    }

    function startTimer() {
        gameState.timerInterval = setInterval(() => {
            const elapsed = Math.floor((Date.now() - gameState.startTime) / 1000);
            const minutes = Math.floor(elapsed / 60);
            const seconds = elapsed % 60;
            const timerEl = document.getElementById('timer');
            if (timerEl) {
                timerEl.textContent = 
                    `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
            }
        }, 1000);
    }

    function bindCellEvents() {
        const cells = document.querySelectorAll('.grid-cell');
        
        cells.forEach(cell => {
            cell.addEventListener('mousedown', (e) => {
                e.preventDefault();
                gameState.isSelecting = true;
                gameState.selectedCells = [];
                selectCell(cell);
            });
            
            cell.addEventListener('mouseenter', (e) => {
                if (gameState.isSelecting) {
                    selectCell(cell);
                }
            });
        });
        
        document.addEventListener('mouseup', () => {
            if (gameState.isSelecting) {
                gameState.isSelecting = false;
                checkWord();
            }
        });
    }

    function selectCell(cell) {
        // Allow selection even if already found (for shared letters)
        if (gameState.selectedCells.includes(cell)) return;
        
        cell.classList.add('selected');
        gameState.selectedCells.push(cell);
    }

    function clearSelection() {
        gameState.selectedCells.forEach(cell => {
            if (!cell.classList.contains('found')) {
                cell.classList.remove('selected');
            }
        });
        gameState.selectedCells = [];
    }

    function checkWord() {
        if (gameState.selectedCells.length === 0) return;
        
        // Get the word from selected cells
        const selectedWord = gameState.selectedCells
            .map(cell => cell.textContent.trim())
            .join('');
        
        // Check both forward and backward
        const wordIndex = gameState.words.findIndex(word => {
            return (word === selectedWord || 
                    word === selectedWord.split('').reverse().join('')) &&
                   !gameState.foundWords.includes(word);
        });
        
        if (wordIndex !== -1) {
            // Word found!
            const foundWord = gameState.words[wordIndex];
            markWordFound(foundWord, wordIndex);
        } else {
            // Wrong word - clear selection after brief delay
            setTimeout(() => {
                clearSelection();
            }, 200);
        }
    }

    function markWordFound(word, wordIndex) {
        // Mark cells as found
        gameState.selectedCells.forEach(cell => {
            cell.classList.remove('selected');
            cell.classList.add('found');
        });
        
        // Update score
        gameState.score += word.length * 10;
        const scoreEl = document.getElementById('score');
        if (scoreEl) {
            scoreEl.textContent = gameState.score;
        }
        
        // Update found words
        gameState.foundWords.push(word);
        const foundCountEl = document.getElementById('found-count');
        if (foundCountEl) {
            foundCountEl.textContent = gameState.foundWords.length;
        }
        
        // Mark word in list - try both by ID and by data attribute
        const wordElById = document.getElementById(`word-${wordIndex}`);
        const wordElByData = document.querySelector(`.word-item[data-word="${word}"]`);
        
        if (wordElById) {
            wordElById.classList.add('found');
        } else if (wordElByData) {
            wordElByData.classList.add('found');
        }
        
        // Clear selection
        gameState.selectedCells = [];
        
        // Check if game is complete
        if (gameState.foundWords.length === gameState.words.length) {
            completeGame();
        }
    }

    function completeGame() {
        clearInterval(gameState.timerInterval);
        
        const timeSpent = Math.floor((Date.now() - gameState.startTime) / 1000);
        
        // Show success message
        const overlay = document.createElement('div');
        overlay.className = 'success-overlay';
        overlay.innerHTML = `
            <div class="success-message">
                <h2>🎉 ¡Felicitaciones! 🎉</h2>
                <h3>¡Encontraste todas las palabras!</h3>
                <div class="stats">
                    <p><strong>⏱️ Tiempo:</strong> ${Math.floor(timeSpent / 60)}:${String(timeSpent % 60).padStart(2, '0')}</p>
                    <p><strong>🎯 Puntuación:</strong> ${gameState.score}</p>
                </div>
                <button class="btn btn-primary mt-3" id="close-success">Continuar</button>
            </div>
        `;
        
        document.body.appendChild(overlay);
        
        document.getElementById('close-success').addEventListener('click', () => {
            overlay.remove();
        });
        
        // Auto-save the attempt
        saveAttempt(timeSpent, gameState.score, true);
    }

    function saveAttempt(timeSpent, score, completed) {
        // Evitar guardar múltiples veces
        if (gameState.attemptSaved) {
            console.log('Attempt already saved, skipping...');
            return;
        }
        
        gameState.attemptSaved = true;
        
        console.log('Saving attempt with:', {
            game_id: gameState.gameId,
            time_spent: timeSpent,
            score: score,
            completed: completed,
            found_words: gameState.foundWords
        });
        
        fetch('/word_search/save_attempt', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                jsonrpc: "2.0",
                method: "call",
                params: {
                    game_id: gameState.gameId,
                    time_spent: timeSpent,
                    score: score,
                    completed: completed,
                    found_words: gameState.foundWords
                }
            })
        }).then(response => response.json())
          .then(data => {
              console.log('Attempt saved successfully:', data);
              if (data.error) {
                  console.error('Error from server:', data.error);
              }
          })
          .catch(error => {
              console.error('Error saving attempt:', error);
          });
    }

    function bindButtonEvents() {
        const resetBtn = document.getElementById('reset-game');
        if (resetBtn) {
            resetBtn.addEventListener('click', () => {
                location.reload();
            });
        }
        
        const saveBtn = document.getElementById('save-attempt');
        if (saveBtn) {
            saveBtn.addEventListener('click', () => {
                const timeSpent = Math.floor((Date.now() - gameState.startTime) / 1000);
                const completed = gameState.foundWords.length === gameState.words.length;
                
                saveAttempt(timeSpent, gameState.score, completed);
                
                setTimeout(() => {
                    window.location.href = '/web#action=word_search_gamification.action_word_search_game';
                }, 500);
            });
        }
    }

    // Initialize when script loads
    initGame();

})();
