// Concise StudyMate Chatbot - Covering All Student Life Aspects

var chatbotMessages = {
    "study-plan": [
        "Let's create your study plan! 📚 Start with 25-minute focused sessions (Pomodoro), list your subjects by priority, and schedule daily review time. What subjects are you working on?",
        "Study planning made simple: Break big topics into chunks, set daily goals, and use a calendar. The key is consistency over perfection! Need help with a specific subject?"
    ],
    
    "motivation": [
        "Feeling unmotivated? Remember your 'why' and celebrate small wins! 🌟 Try the 2-minute rule - just start for 2 minutes. What's your main goal right now?",
        "Motivation comes and goes, but systems stay! Create a study routine, track progress visually, and reward yourself for showing up. You've got this! 💪"
    ],
    
    "time-management": [
        "Time management hack: Use time-blocking! 📅 Schedule specific hours for study, breaks, and fun. Prioritize urgent + important tasks first. What's eating up your time?",
        "Try this: List 3 must-do tasks daily, batch similar activities, and say no to time-wasters. Quality over quantity always wins! ⏰"
    ],
    
    "goals": [
        "Make your goals SMART: Specific, Measurable, Achievable, Relevant, Time-bound! 🎯 Break big goals into weekly milestones. What's your main goal?",
        "Goals without plans are wishes! Write them down, track progress, and adjust as needed. Start small, stay consistent. What do you want to achieve?"
    ],
    
    "focus": [
        "Can't focus? Try this: Remove distractions, use a timer, take breaks every 25 minutes. 🧘 Your phone = biggest enemy! What's distracting you most?",
        "Focus hack: Single-task only, create a dedicated study space, and use background noise if it helps. Practice makes perfect! 🎯"
    ],
    
    "stress": [
        "Feeling stressed? Take deep breaths (4-4-4-4 count), go for a walk, or talk to someone. 🧘‍♀️ Sleep 7-9 hours - non-negotiable! What's stressing you out?",
        "Stress is normal but manageable! Break overwhelming tasks into tiny steps, practice self-compassion, and remember: progress > perfection. 💚"
    ],
    
    "procrastination": [
        "Procrastinating? Just start for 5 minutes - that's it! 🚀 Often starting is the hardest part. Change your environment and eliminate temptations.",
        "Beat procrastination: Break tasks into micro-steps, use deadlines, and reward yourself for starting (not finishing). What are you avoiding?"
    ],
    
    "money": [
        "Student budget tips: Track expenses, cook at home, buy used textbooks, and look for student discounts everywhere! 💰 Need specific budgeting help?",
        "Money struggles? Try the 50/30/20 rule: 50% needs, 30% wants, 20% savings. Look for part-time work or scholarships. Every dollar counts! 💸"
    ],
    
    "relationships": [
        "Relationship issues? Communication is key! 💬 Be honest about your feelings, listen actively, and respect boundaries. Want to talk about it?",
        "Friends or family drama? Sometimes you need space to focus on yourself. Surround yourself with people who support your growth! 🌱"
    ],
    
    "health": [
        "Health first! 💪 Exercise 20 minutes daily, eat brain foods (nuts, fish, fruits), stay hydrated, and prioritize sleep. Small changes = big results!",
        "Feeling unwell? Rest when sick, eat nutritious meals, and don't skip medical checkups. Your body is your most important tool! 🏥"
    ],
    
    "anxiety": [
        "Anxiety is tough but beatable! 💙 Try the 5-4-3-2-1 technique: name 5 things you see, 4 you hear, 3 you touch, 2 you smell, 1 you taste.",
        "Anxious thoughts? Challenge them: Is this realistic? What would I tell a friend? Practice mindfulness and seek support when needed. 🫂"
    ],
    
    "loneliness": [
        "Feeling lonely? Join clubs, study groups, or volunteer! 🤝 Quality connections matter more than quantity. Start with small interactions daily.",
        "Loneliness happens to everyone. Reach out to old friends, make new ones through shared interests, and be kind to yourself. You matter! ❤️"
    ],
    
    "confidence": [
        "Build confidence by celebrating small wins and facing fears gradually! 🌟 Practice positive self-talk and remember past successes. What makes you doubt yourself?",
        "Confidence grows with action! Set small challenges, learn new skills, and stop comparing yourself to others. You're unique and valuable! ✨"
    ],
    
    "habits": [
        "Building habits? Start tiny (2 minutes), stack onto existing routines, and track progress! 📊 Focus on one habit at a time. What habit do you want?",
        "Good habits = future success! Make it obvious, attractive, easy, and satisfying. Bad habits? Make them opposite. Consistency beats perfection! 🔄"
    ],
    
    "career": [
        "Career confused? Explore your interests, network with professionals, and gain experience through internships! 🚀 What field interests you?",
        "Career planning: Identify your strengths, research job markets, build relevant skills, and create a LinkedIn profile. Start now, not later! 💼"
    ],
    
    "family": [
        "Family issues? Set boundaries, communicate clearly, and remember you can't control others - only your reactions. 👨‍👩‍👧‍👦 Need to talk about it?",
        "Family pressure? Stay true to your values while respecting theirs. Sometimes agreeing to disagree is okay. Your mental health matters! 💚"
    ],
    
    "depression": [
        "Feeling down? Reach out to counseling services, exercise regularly, maintain routines, and don't isolate yourself. 💙 Professional help is available!",
        "Depression is real and treatable. Talk to trusted people, practice self-care, and consider therapy. You deserve support and happiness! 🌈"
    ],
    
    "sleep": [
        "Sleep troubles? No screens 1 hour before bed, keep room cool and dark, and stick to a schedule! 😴 Quality sleep = better grades and mood.",
        "Can't sleep? Try relaxation techniques, avoid caffeine after 2pm, and create a bedtime routine. Sleep is not optional - it's essential! 🛏️"
    ],
    
    "exam-prep": [
        "Exam coming up? Start early, use practice tests, study with others, and get good sleep before the test! 📝 What subject are you preparing for?",
        "Exam strategy: Review notes daily, create flashcards, teach concepts to others, and stay calm during the test. You've got this! 🎯"
    ],
    
    "social-media": [
        "Social media overwhelming? Set time limits, unfollow negative accounts, and use it intentionally! 📱 Real life > virtual life always.",
        "Social media tips: Curate your feed positively, don't compare yourself to others, and take regular breaks. Your mental health is priority! 🧠"
    ],
    
    "roommates": [
        "Roommate drama? Set clear expectations, communicate respectfully, and compromise when possible! 🏠 Mutual respect is key to harmony.",
        "Living with others is tricky! Establish boundaries, share responsibilities fairly, and address issues early. Good communication prevents conflicts! 🤝"
    ],

    // Enhanced conversational responses
    "hello": [
        "Hey there! 👋 I'm StudyMate, your go-to support for everything student life! From studies to stress, goals to relationships - I'm here to help! What's on your mind?",
        "Hello! 🌟 Ready to tackle whatever student life throws at you? I'm here for academics, personal challenges, goals, and everything in between! How can I help?"
    ],
    
    "thank": [
        "You're so welcome! 😊 Remember, asking for help is a sign of strength, not weakness. I'm always here when you need support! Keep being awesome! ✨",
        "Anytime! 💫 Your success and wellbeing matter to me. Feel free to come back whenever you need a boost or have questions. You've got this!"
    ],
    
    "help": [
        "I'm here for ALL aspects of student life! 📚 Academics, stress, relationships, money, health, career planning, personal challenges - you name it! What do you need support with?",
        "Think of me as your student life toolkit! 🛠️ I help with studies, personal growth, life skills, and everything in between. What's your biggest challenge right now?"
    ],
    
    "name": [
        "I'm StudyMate - your all-in-one student support companion! 🤖✨ I'm here for academics, personal challenges, life skills, and everything student life brings. Think of me as your caring, always-available friend!",
        "Hey! I'm StudyMate, designed to help students thrive in ALL areas of life! 🌟 From homework to heartbreak, budgets to burnout - I've got your back!"
    ]
};

// Comprehensive keyword patterns covering all student life aspects
var keywordPatterns = {
    "study-plan": ["study plan", "study schedule", "planning", "organize studies", "study routine", "academic planning"],
    "motivation": ["motivation", "motivated", "inspire", "encourage", "drive", "losing interest", "demotivated", "uninspired", "give up"],
    "time-management": ["time management", "manage time", "organize", "schedule", "deadline", "busy", "overwhelmed", "productivity"],
    "goals": ["goal", "target", "objective", "aim", "ambition", "achievement", "accomplish", "dream"],
    "focus": ["focus", "concentration", "distracted", "attention", "can't concentrate", "easily distracted", "focus issues"],
    "stress": ["stress", "stressed", "anxiety", "worried", "overwhelmed", "pressure", "nervous", "panic", "anxious"],
    "procrastination": ["procrastination", "procrastinating", "lazy", "delay", "postpone", "putting off", "avoiding", "can't start"],
    "money": ["money", "budget", "financial", "broke", "expensive", "cost", "afford", "cash", "debt", "income", "job"],
    "relationships": ["relationship", "boyfriend", "girlfriend", "dating", "breakup", "love", "crush", "romantic", "partner"],
    "health": ["health", "sick", "illness", "doctor", "medical", "physical", "exercise", "fitness", "diet", "nutrition"],
    "anxiety": ["anxiety", "anxious", "panic", "worry", "nervous", "fear", "scared", "mental health"],
    "loneliness": ["lonely", "alone", "isolated", "friends", "social", "nobody understands", "no one cares"],
    "confidence": ["confidence", "self-esteem", "insecure", "doubt", "believe in myself", "not good enough", "imposter"],
    "habits": ["habit", "routine", "consistency", "daily practice", "building habits", "changing habits"],
    "career": ["career", "job", "work", "internship", "future", "major", "profession", "employment"],
    "family": ["family", "parents", "mom", "dad", "siblings", "home", "family problems", "family pressure"],
    "depression": ["depression", "depressed", "sad", "hopeless", "worthless", "suicidal", "dark thoughts"],
    "sleep": ["sleep", "tired", "insomnia", "can't sleep", "exhausted", "sleepy", "bedtime"],
    "exam-prep": ["exam", "test", "quiz", "assessment", "examination", "midterm", "final"],
    "social-media": ["social media", "instagram", "facebook", "twitter", "tiktok", "online", "internet addiction"],
    "roommates": ["roommate", "dorm", "living", "housing", "apartment", "residence"]
};

// Enhanced greeting and response patterns
var greetingPatterns = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening", "what's up", "howdy"];
var thankPatterns = ["thank", "thanks", "appreciate", "awesome", "great", "amazing", "helpful"];
var helpPatterns = ["help", "assist", "support", "guidance", "advice", "what can you do"];
var identityPatterns = ["who are you", "your name", "what are you", "about you"];

// Enhanced message processing
function processUserMessage(message) {
    message = message.toLowerCase().trim();
    
    // Check for greetings
    if (greetingPatterns.some(pattern => message.includes(pattern))) {
        displayBotMessage(getRandomResponse("hello"));
        return;
    }
    
    // Check for thanks
    if (thankPatterns.some(pattern => message.includes(pattern))) {
        displayBotMessage(getRandomResponse("thank"));
        return;
    }
    
    // Check for help requests
    if (helpPatterns.some(pattern => message.includes(pattern))) {
        displayBotMessage(getRandomResponse("help"));
        return;
    }
    
    // Check for identity questions
    if (identityPatterns.some(pattern => message.includes(pattern))) {
        displayBotMessage(getRandomResponse("name"));
        return;
    }
    
    // Topic matching with scoring
    let bestMatch = null;
    let bestScore = 0;
    
    for (let topic in keywordPatterns) {
        let score = 0;
        let patterns = keywordPatterns[topic];
        
        for (let pattern of patterns) {
            if (message.includes(pattern)) {
                score += pattern.length;
                if (message === pattern) score += 10;
            }
        }
        
        if (score > bestScore) {
            bestScore = score;
            bestMatch = topic;
        }
    }
    
    if (bestMatch && bestScore > 0) {
        displayBotMessage(getRandomResponse(bestMatch));
        return;
    }
    
    // Contextual responses for unmatched queries
    displayBotMessage(getContextualResponse(message));
}

// Get random response from array
function getRandomResponse(topic) {
    let responses = chatbotMessages[topic];
    if (Array.isArray(responses)) {
        return responses[Math.floor(Math.random() * responses.length)];
    }
    return responses;
}

// Smart contextual responses
function getContextualResponse(message) {
    if (message.includes("how") || message.includes("what") || message.includes("why")) {
        return "Great question! 🤔 I'm here to help with all things student life - academics, personal challenges, relationships, health, money, career planning, and more! What specific area can I support you with?";
    }
    
    if (message.includes("can't") || message.includes("difficult") || message.includes("hard") || message.includes("struggle")) {
        return "I hear you - student life can be challenging! 💪 But you're not alone. Whether it's academic, personal, or life skills, we can tackle it together. What's the main challenge you're facing?";
    }
    
    if (message.includes("feel") || message.includes("feeling")) {
        return "Your feelings are completely valid! 💙 Student life brings ups and downs. I can help with stress, motivation, relationships, confidence, and more. Want to share what's going on?";
    }
    
    // Default responses
    var contextualResponses = [
        "I'm here for whatever student life throws at you! 🌟 Academics, personal stuff, relationships, money, health - you name it! What's on your mind today?",
        "Student life is full of challenges, but you don't have to face them alone! 🤝 I'm here to help with studies, personal growth, and everything in between. What can I support you with?",
        "Every student's journey is unique! ✨ Whether you need academic help, life advice, or just someone to listen, I'm here. What would you like to talk about?"
    ];
    
    return contextualResponses[Math.floor(Math.random() * contextualResponses.length)];
}

