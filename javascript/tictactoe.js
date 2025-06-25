// Simple Tic Tac Toe game logic and UI in JavaScript

const board = Array(9).fill(' ');
let currentPlayer = 'X';
let winner = null;

function checkWinner() {
    const winPatterns = [
        [0,1,2],[3,4,5],[6,7,8], // rows
        [0,3,6],[1,4,7],[2,5,8], // cols
        [0,4,8],[2,4,6]          // diags
    ];
    for (const [a, b, c] of winPatterns) {
        if (board[a] !== ' ' && board[a] === board[b] && board[a] === board[c]) {
            return board[a];
        }
    }
    return board.includes(' ') ? null : 'draw';
}

function makeMove(pos) {
    if (board[pos] === ' ' && !winner) {
        board[pos] = currentPlayer;
        winner = checkWinner();
        updateUI();
        if (!winner && currentPlayer === 'O') {
            botMove();
        }
    }
}

function botMove() {
    // 1. Cherche à gagner
    for (let i = 0; i < 9; i++) {
        if (board[i] === ' ') {
            board[i] = 'O';
            if (checkWinner() === 'O') {
                winner = 'O';
                updateUI();
                return;
            }
            board[i] = ' ';
        }
    }
    // 2. Bloque l'adversaire
    for (let i = 0; i < 9; i++) {
        if (board[i] === ' ') {
            board[i] = 'X';
            if (checkWinner() === 'X') {
                board[i] = 'O';
                winner = checkWinner();
                updateUI();
                return;
            }
            board[i] = ' ';
        }
    }
    // 3. Sinon, joue aléatoirement
    const empty = board.map((v, i) => v === ' ' ? i : null).filter(i => i !== null);
    if (empty.length > 0) {
        const move = empty[Math.floor(Math.random() * empty.length)];
        board[move] = 'O';
        winner = checkWinner();
        updateUI();
    }
}

function updateUI() {
    for (let i = 0; i < 9; i++) {
        document.getElementById('cell'+i).textContent = board[i];
    }
    const status = document.getElementById('status');
    currentPlayer = (currentPlayer === 'X' && !winner) ? 'O' : 'X';
    if (winner === 'draw') {
        status.textContent = "c'est un match nul!";
    } else if (winner) {
        status.textContent = `Le joueur ${winner} a gagné!`;
    } else {
        status.textContent = `Au joueur ${currentPlayer} de jouer`;
    }
}

// Setup UI
window.onload = function() {
    const boardDiv = document.getElementById('board');
    for (let i = 0; i < 9; i++) {
        // wrap button creation in a div
        const btn = document.createElement('button');
        btn.id = 'cell'+i;
        btn.textContent = ' ';
        btn.onclick = () => makeMove(i);
        const btnWrapper = document.createElement('div');
        btnWrapper.appendChild(btn);
        boardDiv.appendChild(btnWrapper);
        if ((i+1)%3 === 0) boardDiv.appendChild(document.createElement('br'));
    }
};