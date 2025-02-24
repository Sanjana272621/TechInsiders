// Sample course data
const courses = [
    {
        id: 1,
        title: "Arduino UNO",
        description: "Learn the basics and tinker on your own!",
        category: "tech",
        image: "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcSnXtaJAFC-B_DOHuY9vY3VFtEkddiP5Q9wblZPvGSEf46yIWcKHkor0VeaFphXU6ga6P4B45U8WHHs4t872dwXREnfrHScflEsLbnvkWBrbhkdPSy5oEd5&usqp=CAE",
        duration: "8 weeks",
        level: "Beginner"
    },
    {
        id: 2,
        title: "Beginners' Tennis Course",
        description: "Become a Pro!",
        category: "sport",
        image: "https://plus.unsplash.com/premium_photo-1666913667082-c1fecc45275d?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dGVubmlzfGVufDB8fDB8fHww",
        duration: "2 weeks",
        level: "Beginner"
    },
    // Add more courses as needed
];

// DOM Elements
const courseGrid = document.getElementById('courseGrid');
const searchInput = document.getElementById('courseSearch');
const categoryFilter = document.getElementById('categoryFilter');

// Render courses
function renderCourses(coursesToRender) {
    courseGrid.innerHTML = coursesToRender.map(course => `
        <div class="course-card">
            <div class="course-image" style="background-image: url('${course.image}')"></div>
            <div class="course-content">
                <h3>${course.title}</h3>
                <p>${course.description}</p>
                <div class="course-meta">
                    <span>${course.duration}</span>
                    <span>${course.level}</span>
                </div>
                <a href="#" class="cool-button">Go to Course</a>
            </div>
        </div>
    `).join('');
}

// Filter courses
function filterCourses() {
    const searchTerm = searchInput.value.toLowerCase();
    const categoryTerm = categoryFilter.value;
    
    const filtered = courses.filter(course => {
        const matchesSearch = course.title.toLowerCase().includes(searchTerm) ||
                            course.description.toLowerCase().includes(searchTerm);
        const matchesCategory = !categoryTerm || course.category === categoryTerm;
        return matchesSearch && matchesCategory;
    });
    
    renderCourses(filtered);
}

// Event listeners
searchInput.addEventListener('input', filterCourses);
categoryFilter.addEventListener('change', filterCourses);

// Initial render
renderCourses(courses);
