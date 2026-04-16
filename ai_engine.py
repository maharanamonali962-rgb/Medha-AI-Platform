def generate_roadmap(goal):
    roadmap_data = {
        "AI Engineer": [
            "Learn Python",
            "Learn Data Structures",
            "Machine Learning",
            "Deep Learning",
            "Projects + Internship"
        ],
        "Web Developer": [
            "HTML, CSS, JS",
            "React",
            "Backend (Node/Flask)",
            "Database",
            "Deploy Projects"
        ]
    }

    return roadmap_data.get(goal, ["Custom roadmap will be generated"])


def generate_questions():
    return [
        {"q": "What is AI?", "a": "Artificial Intelligence"},
        {"q": "What is ML?", "a": "Machine Learning"}
    ]