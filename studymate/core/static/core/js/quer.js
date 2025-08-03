$(document).ready(function() {
            $("#chatbotContainer").hide();
            
            // Toggle chatbot
            $("#chatbotIcon").click(function() {
                toggleChatbot();
            });
            
            $("#closeChat").click(function() {
                closeChatbot();
            });

            function toggleChatbot() {
                if ($("#chatbotContainer").is(":visible")) {
                    closeChatbot();
                } else {
                    openChatbot();
                }
            }

            function openChatbot() {
                $("#chatbotContainer").show();
                setTimeout(() => {
                    $("#chatbotContainer").addClass("show");
                }, 10);
                $("#floatingText").fadeOut();
                $("#ikonic").hide();
                $("#closeIcon").show();
                $("#chatbotIcon").addClass("active");
                $("#chatbotInput").focus();
            }

            function closeChatbot() {
                $("#chatbotContainer").removeClass("show");
                setTimeout(() => {
                    $("#chatbotContainer").hide();
                }, 300);
                $("#floatingText").fadeIn();
                $("#ikonic").show();
                $("#closeIcon").hide();
                $("#chatbotIcon").removeClass("active");
            }

            // Handle user input
            function handleUserInput() {
                var message = $("#chatbotInput").val().trim();
                if (message === "") return;
                
                $("#chatbotInput").val("");
                displayUserMessage(message);
                
                // Show typing indicator
                showTypingIndicator();
                
                // Process message after a delay for more natural feel
                setTimeout(() => {
                    hideTypingIndicator();
                    processUserMessage(message);
                }, 1500);
            }

            function showTypingIndicator() {
                var typingHtml = '<div class="chatbot-message typing-indicator" id="typingIndicator">' +
                    '<span style="opacity: 0.7; font-size: 13px;">StudyMate is typing</span>' +
                    '<div class="typing-dots">' +
                    '<div class="typing-dot"></div>' +
                    '<div class="typing-dot"></div>' +
                    '<div class="typing-dot"></div>' +
                    '</div></div>';
                $("#chatbotBody").append(typingHtml);
                scrollToBottom();
            }

            function hideTypingIndicator() {
                $("#typingIndicator").remove();
            }

            $("#chatbotInput").keypress(function(event) {
                if (event.which == 13) {
                    handleUserInput();
                }
            });

            $("#sendButton").click(handleUserInput);

            function displayBotMessage(message) {
                var botMessage = '<div class="chatbot-message chatbot-bot">' + message + '</div>';
                $("#chatbotBody").append(botMessage);
                scrollToBottom();
            }

            function displayUserMessage(message) {
                var userMessage = '<div class="chatbot-message chatbot-user"><div class="message-bubble">' + message + '</div></div>';
                $("#chatbotBody").append(userMessage);
                scrollToBottom();
            }

            function scrollToBottom() {
                var chatbotBody = document.getElementById("chatbotBody");
                chatbotBody.scrollTop = chatbotBody.scrollHeight;
            }

            function processUserMessage(message) {
                message = message.toLowerCase();

                // Academic assistance keywords
                if (message.includes("study plan") || message.includes("study schedule") || message.includes("planning")) {
                    displayBotMessage(chatbotMessages["study-plan"]);
                    return;
                }

                if (message.includes("motivation") || message.includes("motivated") || message.includes("inspire") || message.includes("encourage")) {
                    displayBotMessage(chatbotMessages["motivation"]);
                    return;
                }

                if (message.includes("time management") || message.includes("manage time") || message.includes("organize")) {
                    displayBotMessage(chatbotMessages["time-management"]);
                    return;
                }

                if (message.includes("goal") || message.includes("target") || message.includes("objective")) {
                    displayBotMessage(chatbotMessages["goals"]);
                    return;
                }

                if (message.includes("focus") || message.includes("concentration") || message.includes("distracted")) {
                    displayBotMessage(chatbotMessages["focus"]);
                    return;
                }

                if (message.includes("stress") || message.includes("anxiety") || message.includes("worried") || message.includes("overwhelmed")) {
                    displayBotMessage(chatbotMessages["stress"]);
                    return;
                }

                if (message.includes("note") || message.includes("notes") || message.includes("note-taking")) {
                    displayBotMessage(chatbotMessages["note-taking"]);
                    return;
                }

                if (message.includes("exam") || message.includes("test") || message.includes("quiz") || message.includes("assessment")) {
                    displayBotMessage(chatbotMessages["exam-prep"]);
                    return;
                }

                if (message.includes("productive") || message.includes("productivity") || message.includes("efficient")) {
                    displayBotMessage(chatbotMessages["productivity"]);
                    return;
                }

                if (message.includes("reading") || message.includes("comprehension") || message.includes("textbook")) {
                    displayBotMessage(chatbotMessages["reading"]);
                    return;
                }

                if (message.includes("memory") || message.includes("remember") || message.includes("forget") || message.includes("memorize")) {
                    displayBotMessage(chatbotMessages["memory"]);
                    return;
                }

                if (message.includes("procrastination") || message.includes("procrastinating") || message.includes("lazy") || message.includes("delay")) {
                    displayBotMessage(chatbotMessages["procrastination"]);
                    return;
                }

                if (message.includes("research") || message.includes("sources") || message.includes("reference")) {
                    displayBotMessage(chatbotMessages["research"]);
                    return;
                }

                if (message.includes("writing") || message.includes("essay") || message.includes("paper") || message.includes("assignment")) {
                    displayBotMessage(chatbotMessages["writing"]);
                    return;
                }

                if (message.includes("group study") || message.includes("study group") || message.includes("collaboration")) {
                    displayBotMessage(chatbotMessages["collaboration"]);
                    return;
                }

                if (message.includes("habit") || message.includes("routine") || message.includes("consistency")) {
                    displayBotMessage(chatbotMessages["habits"]);
                    return;
                }

                // Greetings
                if (message.includes("hello") || message.includes("hi") || message.includes("hey") || 
                    message.includes("good morning") || message.includes("good afternoon") || message.includes("good evening")) {
                    displayBotMessage(chatbotMessages["hello"]);
                    return;
                }

                // Thanks
                if (message.includes("thank") || message.includes("thanks") || message.includes("appreciate") || 
                    message.includes("awesome") || message.includes("great") || message.includes("amazing")) {
                    displayBotMessage(chatbotMessages["thank"]);
                    return;
                }

                // Help
                if (message.includes("help") || message.includes("assist") || message.includes("support")) {
                    displayBotMessage(chatbotMessages["help"]);
                    return;
                }

                // Identity
                if (message.includes("who are you") || message.includes("your name") || message.includes("what are you")) {
                    displayBotMessage(chatbotMessages["name"]);
                    return;
                }

                // Default response
                var responses = [
                    "That's a great question! While I may not have specific information about that topic, I'm here to help with study strategies, goal setting, time management, and academic motivation. What specific study challenge are you facing?",
                    "I'm focused on helping you succeed academically! Could you tell me more about your current study goals or any challenges you're experiencing with learning?",
                    "Let me help you with your academic journey! What aspect of studying or learning would you like to improve? I can assist with planning, motivation, techniques, and more!"
                ];
                
                var randomResponse = responses[Math.floor(Math.random() * responses.length)];
                displayBotMessage(randomResponse);
            }
        });