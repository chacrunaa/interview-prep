// Shared retrieval-practice quiz widget for the Go-fundamentals lessons.
// Usage: new Quiz(document.getElementById('quiz-1'), {
//   prompt: 'Question text',
//   options: ['answer a', 'answer b', 'answer c'], // keep lengths close - no giveaways
//   correctIndex: 1,
//   feedback: { correct: 'text on success', incorrect: 'text on failure' }
// });
class Quiz {
  constructor(root, { prompt, options, correctIndex, feedback = {} }) {
    this.root = root;
    this.correctIndex = correctIndex;
    this.answered = false;
    root.classList.add('quiz');
    root.innerHTML = `
      <div class="q-prompt">${prompt}</div>
      <div class="q-options"></div>
      <div class="q-feedback" role="status"></div>
    `;
    const optsEl = root.querySelector('.q-options');
    const feedbackEl = root.querySelector('.q-feedback');
    options.forEach((text, i) => {
      const btn = document.createElement('button');
      btn.className = 'q-opt';
      btn.type = 'button';
      btn.textContent = text;
      btn.addEventListener('click', () => {
        if (this.answered) return;
        this.answered = true;
        const buttons = optsEl.querySelectorAll('button');
        buttons.forEach((b) => (b.disabled = true));
        if (i === correctIndex) {
          btn.classList.add('correct');
          feedbackEl.textContent = feedback.correct || 'Верно.';
          feedbackEl.style.color = 'var(--good)';
        } else {
          btn.classList.add('incorrect');
          buttons[correctIndex].classList.add('correct');
          feedbackEl.textContent = feedback.incorrect || 'Неверно — правильный вариант подсвечен.';
          feedbackEl.style.color = 'var(--bad)';
        }
      });
      optsEl.appendChild(btn);
    });
  }
}
