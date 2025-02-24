// Sample data for active courses
const activeCourses = [
    {
        id: 1,
        title: "Basic Arduino UNO",
        progress: 75,
        totalModules: 12,
        completedModules: 9
    },
    {
        id: 2,
        title: "Beginners' Tennis Course",
        progress: 60,
        totalModules: 10,
        completedModules: 6
    },
    {
        id: 3,
        title: "UI/UX Design Fundamentals",
        progress: 30,
        totalModules: 8,
        completedModules: 2
    }
];

// Sample data for skills
const skills = [
    {
        name: "Arduino UNO",
        level: "Advanced",
        percentage: 90
    },
    {
        name: "Sensor Technology",
        level: "Intermediate",
        percentage: 75
    },
    {
        name: "Lawn Sports",
        level: "Beginner",
        percentage: 45
    },
    {
        name: "UI Design",
        level: "Intermediate",
        percentage: 65
    }
];

// Sample data for achievements
const achievements = [
    {
        icon: "🏆",
        title: "Course Champion",
        description: "Completed Arduino UNO with distinction",
        date: "February 20, 2025"
    },
    {
        icon: "⭐",
        title: "Rising Star",
        description: "Completed 5 courses in 30 days",
        date: "February 15, 2025"
    },
    {
        icon: "🎨",
        title: "Creative Master",
        description: "Published first digital art portfolio",
        date: "February 10, 2025"
    }
];

// DOM Elements
const activeCoursesList = document.getElementById('activeCoursesList');
const skillsGrid = document.getElementById('skillsGrid');
const achievementsGrid = document.getElementById('achievementsGrid');

// Render active courses
function renderActiveCourses() {
    activeCoursesList.innerHTML = activeCourses.map(course => `
        <div class="course-progress-card">
            <h3>${course.title}</h3>
            <div class="course-progress-bar">
                <div class="progress-fill" style="width: ${course.progress}%"></div>
            </div>
            <div class="course-progress-info">
                <span>${course.progress}% complete</span>
            </div>
        </div>
    `).join('');
}

// Render skills
function renderSkills() {
    skillsGrid.innerHTML = skills.map(skill => `
        <div class="skill-card">
            <h3>${skill.name}</h3>
            <div class="skill-level">${skill.percentage}%</div>
            <p>${skill.level}</p>
        </div>
    `).join('');
}

// Render achievements
function renderAchievements() {
    achievementsGrid.innerHTML = achievements.map(achievement => `
        <div class="achievement-card">
            <div class="achievement-icon">${achievement.icon}</div>
            <div class="achievement-info">
                <h3>${achievement.title}</h3>
                <p>${achievement.description}</p>
                <div class="achievement-date">${achievement.date}</div>
            </div>
        </div>
    `).join('');
}

// Initialize all renders
function initializeProgress() {
    renderActiveCourses();
    renderSkills();
    renderAchievements();
}

// Run on page load
document.addEventListener('DOMContentLoaded', initializeProgress);
