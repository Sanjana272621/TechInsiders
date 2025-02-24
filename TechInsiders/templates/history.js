// Sample learning history data
const learningHistory = [
    {
        id: 1,
        date: "February 20, 2025",
        title: "Completed Arduino UNO",
        description: "Completed all quizzes and mastered Arduino UNO basics",
        achievement: "",
        grade: "A+"
    },
    {
        id: 2,
        date: "February 15, 2025",
        title: "Completed Tennis Course",
        description: "Learnt basics of Tennis ",
        achievement: "",
        grade: "A"
    },
    // Add more history items as needed
];

// DOM Elements
const timelineContainer = document.getElementById('learningTimeline');

// Render timeline
function renderTimeline() {
    timelineContainer.innerHTML = learningHistory.map(item => `
        <div class="timeline-item">
            <span class="achievement-badge">${item.achievement}</span>
            <div class="timeline-date">${item.date}</div>
            <h3 class="timeline-title">${item.title}</h3>
            <p class="timeline-description">${item.description}</p>
            <div class="timeline-grade">Grade: ${item.grade}</div>
        </div>
    `).join('');
}

// Initial render
renderTimeline();
