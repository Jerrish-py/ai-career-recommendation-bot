def get_user_choice(prompt, options):
    """
    Displays a prompt with options and gets validated user input.
    """
    print(prompt)
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    print()  # Extra space after options
    while True:
        choice = input("Your choice (number): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            print()  # Extra space after input
            return options[int(choice) - 1]
        else:
            print("Oops! Invalid input, please enter a valid number.\n")


def main():
    print("="*60)
    print("👋 Welcome to the AI Career Recommendation Bot!")
    print("Let's find your perfect tech career based on your interests.\n")
    print("="*60 + "\n")

    print("Before we start, let's clarify two terms:")
    print("• Hardware: The physical parts of a computer system (like CPU, motherboard).")
    print("• Software: Programs and applications that run on hardware.\n")

    domain = get_user_choice(
        "Do you prefer working with hardware or software?",
        ["Hardware", "Software"]
    )

    hardware_careers = ["IoT Engineer", "Hardware Engineer", "Network Engineer"]
    software_careers = [
        "AI Engineer", "Virtual Reality Developer", "Blockchain Developer",
        "Cloud Computing Engineer", "Cybersecurity Analyst", "Software Developer"
    ]

    scores = {}
    if domain == "Hardware":
        for career in hardware_careers:
            scores[career] = 0
    else:
        for career in software_careers:
            scores[career] = 0

    if domain == "Software":
        q1 = get_user_choice(
            "\n1) What excites you the most?",
            ["Building intelligent machines", "Creating interactive worlds",
             "Developing secure systems", "Managing cloud infrastructure",
             "Building distributed applications", "Writing software applications"]
        )

        if q1 == "Building intelligent machines":
            scores["AI Engineer"] += 3
        elif q1 == "Creating interactive worlds":
            scores["Virtual Reality Developer"] += 3
        elif q1 == "Developing secure systems":
            scores["Cybersecurity Analyst"] += 3
        elif q1 == "Managing cloud infrastructure":
            scores["Cloud Computing Engineer"] += 3
        elif q1 == "Building distributed applications":
            scores["Blockchain Developer"] += 3
        elif q1 == "Writing software applications":
            scores["Software Developer"] += 3

        q2 = get_user_choice(
            "2) Which skill do you want to improve?",
            ["Machine Learning", "3D Modeling", "Network Security", "Cloud Services", "Cryptography", "Programming"]
        )

        if q2 == "Machine Learning":
            scores["AI Engineer"] += 2
        elif q2 == "3D Modeling":
            scores["Virtual Reality Developer"] += 2
        elif q2 == "Network Security":
            scores["Cybersecurity Analyst"] += 2
        elif q2 == "Cloud Services":
            scores["Cloud Computing Engineer"] += 2
        elif q2 == "Cryptography":
            scores["Blockchain Developer"] += 2
        elif q2 == "Programming":
            scores["Software Developer"] += 2

        q3 = get_user_choice(
            "3) What kind of projects do you enjoy?",
            ["Data analysis and AI models", "Game and simulation development",
             "Protecting information and privacy", "Deploying and managing servers",
             "Cryptocurrency and smart contracts", "Building web and mobile apps"]
        )
        if q3 == "Data analysis and AI models":
            scores["AI Engineer"] += 2
        elif q3 == "Game and simulation development":
            scores["Virtual Reality Developer"] += 2
        elif q3 == "Protecting information and privacy":
            scores["Cybersecurity Analyst"] += 2
        elif q3 == "Deploying and managing servers":
            scores["Cloud Computing Engineer"] += 2
        elif q3 == "Cryptocurrency and smart contracts":
            scores["Blockchain Developer"] += 2
        elif q3 == "Building web and mobile apps":
            scores["Software Developer"] += 2

        q4 = get_user_choice(
            "4) Which technology trend fascinates you the most?",
            ["Artificial Intelligence", "Virtual Reality", "Cybersecurity",
             "Cloud Computing", "Blockchain", "Software Development"]
        )
        if q4 == "Artificial Intelligence":
            scores["AI Engineer"] += 1
        elif q4 == "Virtual Reality":
            scores["Virtual Reality Developer"] += 1
        elif q4 == "Cybersecurity":
            scores["Cybersecurity Analyst"] += 1
        elif q4 == "Cloud Computing":
            scores["Cloud Computing Engineer"] += 1
        elif q4 == "Blockchain":
            scores["Blockchain Developer"] += 1
        elif q4 == "Software Development":
            scores["Software Developer"] += 1

        q5 = get_user_choice(
            "5) How do you prefer to work?",
            ["Research and innovation", "Creative design", "Problem-solving and defense",
             "Infrastructure management", "Distributed systems", "Coding and debugging"]
        )
        if q5 == "Research and innovation":
            scores["AI Engineer"] += 1
        elif q5 == "Creative design":
            scores["Virtual Reality Developer"] += 1
        elif q5 == "Problem-solving and defense":
            scores["Cybersecurity Analyst"] += 1
        elif q5 == "Infrastructure management":
            scores["Cloud Computing Engineer"] += 1
        elif q5 == "Distributed systems":
            scores["Blockchain Developer"] += 1
        elif q5 == "Coding and debugging":
            scores["Software Developer"] += 1

    else:  # Hardware domain questions
        q1 = get_user_choice(
            "\n1) Which of these interests you the most?",
            ["Designing IoT devices", "Building computer hardware",
             "Setting up networks", "Developing embedded systems",
             "Hardware troubleshooting"]
        )

        if q1 == "Designing IoT devices":
            scores["IoT Engineer"] += 3
        elif q1 == "Building computer hardware":
            scores["Hardware Engineer"] += 3
        elif q1 == "Setting up networks":
            scores["Network Engineer"] += 3
        elif q1 == "Developing embedded systems":
            scores["IoT Engineer"] += 2
        elif q1 == "Hardware troubleshooting":
            scores["Hardware Engineer"] += 2

        q2 = get_user_choice(
            "2) Which skill would you like to develop?",
            ["Circuit design", "Sensor technology", "Network configuration",
             "Firmware programming", "Hardware diagnostics"]
        )

        if q2 == "Circuit design":
            scores["Hardware Engineer"] += 2
        elif q2 == "Sensor technology":
            scores["IoT Engineer"] += 2
        elif q2 == "Network configuration":
            scores["Network Engineer"] += 2
        elif q2 == "Firmware programming":
            scores["IoT Engineer"] += 2
        elif q2 == "Hardware diagnostics":
            scores["Hardware Engineer"] += 1

        q3 = get_user_choice(
            "3) What kind of projects do you enjoy?",
            ["Smart home devices", "Computer assembly",
             "Network infrastructure", "Embedded systems",
             "Hardware repair"]
        )

        if q3 == "Smart home devices":
            scores["IoT Engineer"] += 2
        elif q3 == "Computer assembly":
            scores["Hardware Engineer"] += 2
        elif q3 == "Network infrastructure":
            scores["Network Engineer"] += 2
        elif q3 == "Embedded systems":
            scores["IoT Engineer"] += 2
        elif q3 == "Hardware repair":
            scores["Hardware Engineer"] += 1

        q4 = get_user_choice(
            "4) Which technology fascinates you?",
            ["Internet of Things", "Computer Hardware", "Networking Protocols",
             "Embedded Systems", "Troubleshooting"]
        )

        if q4 == "Internet of Things":
            scores["IoT Engineer"] += 1
        elif q4 == "Computer Hardware":
            scores["Hardware Engineer"] += 1
        elif q4 == "Networking Protocols":
            scores["Network Engineer"] += 1
        elif q4 == "Embedded Systems":
            scores["IoT Engineer"] += 1
        elif q4 == "Troubleshooting":
            scores["Hardware Engineer"] += 1

        q5 = get_user_choice(
            "5) How do you prefer to work?",
            ["Hands-on device building", "Design and testing", "Network management",
             "Programming embedded systems", "Repair and maintenance"]
        )

        if q5 == "Hands-on device building":
            scores["IoT Engineer"] += 1
        elif q5 == "Design and testing":
            scores["Hardware Engineer"] += 1
        elif q5 == "Network management":
            scores["Network Engineer"] += 1
        elif q5 == "Programming embedded systems":
            scores["IoT Engineer"] += 1
        elif q5 == "Repair and maintenance":
            scores["Hardware Engineer"] += 1

    recommended_career = max(scores, key=scores.get)
    
    print("="*60)
    print(f"🎉 Congratulations! Based on your answers, a career as a {recommended_career} suits you best!")
    print("This path aligns well with your interests and skills. Go for it! 🚀\n")
    print("Thank you for using the AI Career Recommendation Bot. I hope this will be useful for you!")
    print("Keep learning and exploring — your future is bright! ✨")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
input("Press Enter to exit")
